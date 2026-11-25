# constants.py — Shared colour constants, font sizes, and config for all Manim scenes
# ─────────────────────────────────────────────────────────────────────────────
# This file is imported by every scene file. Edit colours here to restyle
# the entire video at once.

from manim import *

# ── Background ────────────────────────────────────────────────────────────────
BG_COLOR         = "#1a1a2e"   # Dark navy — applied to every scene

# ── Colour palette (colour-coding for Gaussian elimination) ───────────────────
PIVOT_COLOR      = "#FFD700"   # Gold     — pivot element in a matrix
ROW_CHANGE_COLOR = "#4FC3F7"   # Sky blue — the row being modified  (Rᵢ)
ROW_SOURCE_COLOR = "#81C784"   # Green    — the row used to eliminate (Rⱼ)
SEPARATOR_COLOR  = "#FF8A65"   # Coral    — augmented matrix "|" separator
SOLUTION_COLOR   = "#CE93D8"   # Lavender — final solution highlight
ANNOTATION_COLOR = "#FF8A65"   # Coral    — step annotation text
VERIFY_COLOR     = "#A5D6A7"   # Mint     — correct / verified entries
ERROR_COLOR      = "#EF9A9A"   # Soft red — no-solution / warning
TITLE_COLOR      = WHITE
SUBTITLE_COLOR   = "#B0BEC5"   # Cool grey

# ── Typography scale ──────────────────────────────────────────────────────────
TITLE_FS   = 56   # Opening title
HEADING_FS = 44   # Section headings
BODY_FS    = 36   # Body text
SMALL_FS   = 28   # Labels, annotations
TINY_FS    = 22   # Fine print / credits
