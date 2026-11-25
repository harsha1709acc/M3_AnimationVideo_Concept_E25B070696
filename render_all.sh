#!/usr/bin/env bash
# render_all.sh — Full pipeline: verify -> render -> concat -> mux voiceover -> check
# ──────────────────────────────────────────────────────────────────────────
# Usage:
#   chmod +x render_all.sh
#   ./render_all.sh           # 1080p final (1920x1080, 30fps, synced voiceover)
#   ./render_all.sh --draft   # 720p fast draft (1280x720, 30fps, synced voiceover)

set -e

export PATH="/Library/TeX/texbin:$HOME/Library/Python/3.9/bin:/opt/homebrew/bin:$PATH"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CODE_DIR="$SCRIPT_DIR/E25B070696_Code"
REPO_ROOT="$SCRIPT_DIR"
VOICEOVER="$CODE_DIR/voiceover.mp3"

if [[ "$1" == "--draft" ]]; then
  QUALITY_FLAG="-qm"
  FPS="30"
  MEDIA_SUBDIR="720p30"
  OUT_FILE="$REPO_ROOT/E25B070696_Video_DRAFT_720p.mp4"
  echo "━━━ DRAFT MODE (720p, 30fps) ━━━"
else
  QUALITY_FLAG="-qh"
  FPS="30"
  MEDIA_SUBDIR="1080p30"
  OUT_FILE="$REPO_ROOT/E25B070696_Video.mp4"
  echo "━━━ FINAL MODE (1080p, 30fps) ━━━"
fi

echo ""
echo "▶ Step 0: Verifying mathematics..."
cd "$CODE_DIR"
python3 verify_math.py
echo ""

echo "▶ Step 1: Rendering Manim scenes..."
SCENES=(
  "scene1_hook.py:Scene1Hook"
  "scene2_concepts.py:Scene2Concepts"
  "scene3_intuition.py:Scene3Intuition"
  "scene4_example.py:Scene4Example"
  "scene5_interpret.py:Scene5Interpret"
  "scene6_summary.py:Scene6Summary"
)

TMP_DIR="$CODE_DIR/media/_concat_tmp"
mkdir -p "$TMP_DIR"
CONCAT_FILE="$TMP_DIR/concat.txt"
: > "$CONCAT_FILE"

for ENTRY in "${SCENES[@]}"; do
  FILE="${ENTRY%%:*}"
  MOD="${FILE%.py}"
  CLASS="${ENTRY##*:}"
  echo "  Rendering $CLASS from $FILE ..."
  manim "$FILE" "$CLASS" $QUALITY_FLAG --fps "$FPS" --media_dir "$CODE_DIR/media"
  VID_PATH="$CODE_DIR/media/videos/$MOD/$MEDIA_SUBDIR/${CLASS}.mp4"
  if [[ ! -f "$VID_PATH" ]]; then
    echo "ERROR: Expected rendered file not found: $VID_PATH"
    exit 1
  fi
  echo "file '$VID_PATH'" >> "$CONCAT_FILE"
  echo "  ✓ $CLASS done"
done
echo ""

echo "▶ Step 2: Concatenating scenes..."
SILENT_VID="$TMP_DIR/silent_concat.mp4"
ffmpeg -y -f concat -safe 0 -i "$CONCAT_FILE" -c:v libx264 -pix_fmt yuv420p -preset fast -crf 18 -an "$SILENT_VID"

VID_DUR=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$SILENT_VID")
echo "  Concatenated video duration: $VID_DUR s"

if [[ -f "$VOICEOVER" ]]; then
  echo "▶ Step 3: Syncing student voiceover ($VOICEOVER)..."
  AUD_DUR=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$VOICEOVER")
  ATEMPO=$(python3 -c "print(round(float('$AUD_DUR') / float('$VID_DUR'), 6))")
  echo "  Audio duration: $AUD_DUR s | Video duration: $VID_DUR s | atempo=$ATEMPO"
  ffmpeg -y -i "$SILENT_VID" -i "$VOICEOVER" \
    -c:v copy \
    -filter:a "atempo=$ATEMPO" \
    -c:a aac -b:a 192k \
    -map 0:v:0 -map 1:a:0 \
    -shortest \
    "$OUT_FILE"
else
  echo "▶ Step 3: No voiceover.mp3 found — keeping silent video."
  mv "$SILENT_VID" "$OUT_FILE"
fi
echo ""

echo "▶ Step 4: Generating Storyboard.pdf..."
python3 storyboard_gen.py
echo ""

echo "▶ Step 5: Verifying final video with ffprobe..."
ffprobe -v error -show_entries format=duration -show_entries stream=codec_type,codec_name,width,height,r_frame_rate -of default=noprint_wrappers=1 "$OUT_FILE"

DURATION=$(ffprobe -v error \
  -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1 \
  "$OUT_FILE" 2>/dev/null)

MINS=$(python3 -c "print(int(float('$DURATION')//60))")
SECS=$(python3 -c "print(round(float('$DURATION')%60,1))")
echo "  Total duration: ${MINS}m ${SECS}s ($DURATION s)"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Pipeline complete!"
echo "  Output video : $OUT_FILE"
echo "  Storyboard   : $REPO_ROOT/Storyboard.pdf"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
