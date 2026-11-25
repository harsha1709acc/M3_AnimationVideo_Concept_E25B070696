# matrix_helpers.py — Reusable Manim helpers for matrix display & row-operation animations
# ─────────────────────────────────────────────────────────────────────────────
# Every scene imports from this module. All helpers accept and return
# standard Manim mobjects so they compose naturally with other animations.

from manim import *
from constants import (
    BG_COLOR, PIVOT_COLOR, ROW_CHANGE_COLOR, ROW_SOURCE_COLOR,
    SEPARATOR_COLOR, ANNOTATION_COLOR, SOLUTION_COLOR, BODY_FS, SMALL_FS
)


# ════════════════════════════════════════════════════════════════════════════
#  AugmentedMatrixMob
#  A VGroup that renders an augmented matrix [A | b] with:
#    • colour-coded rows
#    • a vertical separator line before the last column
#    • helpers to highlight individual rows or cells
# ════════════════════════════════════════════════════════════════════════════
class AugmentedMatrixMob(VGroup):
    """
    Parameters
    ----------
    rows : list[list[str]]
        Each inner list is a row of the FULL augmented matrix, e.g.
        [["1", "2", "1", "8"], ["2", "3", "4", "20"], ...]
        The last element in each inner list is the RHS (b column).
    n_lhs : int
        Number of left-hand-side columns (default 3 for a 3×3 system).
    cell_width : float
        Horizontal spacing between columns.
    cell_height : float
        Vertical spacing between rows.
    font_size : int
        Font size for all entries.
    """

    def __init__(
        self,
        rows: list,
        n_lhs: int = 3,
        cell_width: float = 0.85,
        cell_height: float = 0.75,
        font_size: int = 36,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.n_rows = len(rows)
        self.n_cols = len(rows[0])
        self.n_lhs = n_lhs
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.font_size = font_size

        # ── Build entry mobjects on a centred grid ─────────────────────────
        self.entries = []          # 2-D list [row][col]  → Tex mobject
        y_center_offset = (self.n_rows - 1) / 2.0
        for r, row_data in enumerate(rows):
            row_mobs = []
            for c, val in enumerate(row_data):
                tex = MathTex(str(val), font_size=font_size, color=WHITE)
                tex.move_to(
                    RIGHT * c * cell_width
                    + DOWN * (r - y_center_offset) * cell_height
                )
                row_mobs.append(tex)
            self.entries.append(row_mobs)
            self.add(*row_mobs)

        # ── Brackets ─────────────────────────────────────────────────────────
        mat_height = (self.n_rows - 1) * cell_height + 0.55

        # Left bracket "[" : vertical spine on the left, ticks pointing right
        left_x = -0.42
        left_spine_t = UP * mat_height / 2 + RIGHT * left_x
        left_spine_b = DOWN * mat_height / 2 + RIGHT * left_x
        left_tick_t  = UP * mat_height / 2 + RIGHT * (left_x + 0.16)
        left_tick_b  = DOWN * mat_height / 2 + RIGHT * (left_x + 0.16)

        # Right bracket "]" : vertical spine on the right, ticks pointing left
        right_x = (self.n_cols - 1) * cell_width + 0.42
        right_spine_t = UP * mat_height / 2 + RIGHT * right_x
        right_spine_b = DOWN * mat_height / 2 + RIGHT * right_x
        right_tick_t  = UP * mat_height / 2 + RIGHT * (right_x - 0.16)
        right_tick_b  = DOWN * mat_height / 2 + RIGHT * (right_x - 0.16)

        def bracket_lines(spine_t, spine_b, tick_t, tick_b):
            return VGroup(
                Line(spine_t, spine_b, color=WHITE, stroke_width=2.5),  # vertical spine
                Line(spine_t, tick_t,  color=WHITE, stroke_width=2.5),  # top tick
                Line(spine_b, tick_b,  color=WHITE, stroke_width=2.5),  # bottom tick
            )

        self.left_bracket  = bracket_lines(left_spine_t,  left_spine_b,  left_tick_t,  left_tick_b)
        self.right_bracket = bracket_lines(right_spine_t, right_spine_b, right_tick_t, right_tick_b)
        self.add(self.left_bracket, self.right_bracket)

        # ── Augmented separator "|" ──────────────────────────────────────────
        sep_x = (n_lhs - 0.5) * cell_width
        self.separator = Line(
            UP * mat_height / 2 + RIGHT * sep_x,
            DOWN * mat_height / 2 + RIGHT * sep_x,
            color=SEPARATOR_COLOR,
            stroke_width=2.5,
        )
        self.add(self.separator)

        # Centre the whole group
        self.center()

    # ── Convenience methods ───────────────────────────────────────────────────

    def get_row(self, r: int) -> VGroup:
        """Return all entry mobjects in row r as a VGroup."""
        return VGroup(*self.entries[r])

    def get_cell(self, r: int, c: int):
        """Return the MathTex mobject at (r, c)."""
        return self.entries[r][c]

    def highlight_row(self, r: int, color) -> Animation:
        """Return an AnimationGroup that colours every entry in row r."""
        return AnimationGroup(
            *[entry.animate.set_color(color) for entry in self.entries[r]]
        )

    def reset_row_color(self, r: int) -> Animation:
        """Return an AnimationGroup that resets row r to WHITE."""
        return AnimationGroup(
            *[entry.animate.set_color(WHITE) for entry in self.entries[r]]
        )

    def highlight_cell(self, r: int, c: int, color) -> Animation:
        """Return an animation that colours a single cell."""
        return self.entries[r][c].animate.set_color(color)

    def scale_and_center(self, scene_width: float = 10.0):
        """Scale so the matrix fits within scene_width, then centre."""
        if self.width > scene_width:
            self.scale(scene_width / self.width)
        self.center()
        return self


# ════════════════════════════════════════════════════════════════════════════
#  row_op_animation
#  High-level helper: animates a single row-replacement operation
#  Rᵢ ← Rᵢ + k·Rⱼ  on an AugmentedMatrixMob in three beats:
#    1. Highlight Rⱼ (source, green) and Rᵢ (target, blue)
#    2. Flash annotation text
#    3. Transform entries of Rᵢ to new values
# ════════════════════════════════════════════════════════════════════════════
def row_op_animation(
    scene,
    mat: AugmentedMatrixMob,
    i: int,              # target row index (0-based)
    j: int,              # source row index (0-based)
    k: str,              # scalar as string, e.g. "-2"
    new_row: list,       # new string values for all entries of row i
    annotation_pos=None, # where to place the annotation label
):
    """
    Animate Rᵢ ← Rᵢ + k·Rⱼ on the given AugmentedMatrixMob.

    Parameters
    ----------
    scene      : Manim Scene (we call scene.play / scene.wait)
    mat        : AugmentedMatrixMob to operate on
    i          : target row (0-based)
    j          : source row (0-based)
    k          : scalar coefficient as a display string
    new_row    : list of string values for the new row i entries
    annotation_pos : UP * n position for the annotation; default above matrix
    """
    # ── 1. Build annotation label ────────────────────────────────────────────
    # Format: R₁ → R₁ + k·R₂  (using subscripts)
    sub_i = str(i + 1)
    sub_j = str(j + 1)
    if k.startswith("-"):
        op_str = rf"R_{sub_i} \to R_{sub_i} {k} R_{sub_j}"
    else:
        op_str = rf"R_{sub_i} \to R_{sub_i} + {k} R_{sub_j}"

    if annotation_pos is None:
        annotation_pos = mat.get_top() + UP * 0.6

    annotation = MathTex(op_str, font_size=SMALL_FS, color=ANNOTATION_COLOR)
    annotation.move_to(annotation_pos)

    # ── 2. Highlight source (green) then target (blue) ───────────────────────
    scene.play(
        mat.highlight_row(j, ROW_SOURCE_COLOR),
        run_time=0.4,
    )
    scene.play(
        mat.highlight_row(i, ROW_CHANGE_COLOR),
        Write(annotation),
        run_time=0.5,
    )
    scene.wait(0.6)

    # ── 3. Transform target row entries to new values ────────────────────────
    new_mobs = [
        MathTex(str(v), font_size=mat.font_size, color=ROW_CHANGE_COLOR)
        .move_to(mat.entries[i][c].get_center())
        for c, v in enumerate(new_row)
    ]
    scene.play(
        *[Transform(mat.entries[i][c], new_mobs[c]) for c in range(mat.n_cols)],
        run_time=0.7,
    )
    scene.wait(0.3)

    # ── 4. Reset colours and fade annotation ────────────────────────────────
    # Note: Transform() mutates mat.entries[i][c] in-place inside the VGroup,
    # so we keep the existing references rather than replacing them.
    scene.play(
        mat.reset_row_color(j),
        mat.reset_row_color(i),
        FadeOut(annotation),
        run_time=0.5,
    )


# ════════════════════════════════════════════════════════════════════════════
#  highlight_pivots
#  After elimination, flash each diagonal pivot in PIVOT_COLOR
# ════════════════════════════════════════════════════════════════════════════
def highlight_pivots(scene, mat: AugmentedMatrixMob, pivot_positions: list):
    """
    Flash the pivot cells gold.

    Parameters
    ----------
    pivot_positions : list of (row, col) tuples, e.g. [(0,0),(1,1),(2,2)]
    """
    anims = [
        mat.entries[r][c].animate.set_color(PIVOT_COLOR).scale(1.15)
        for r, c in pivot_positions
    ]
    scene.play(AnimationGroup(*anims, lag_ratio=0.3), run_time=1.2)
    scene.wait(0.5)


# ════════════════════════════════════════════════════════════════════════════
#  make_label_box
#  Convenience: coloured rounded rectangle + label text
# ════════════════════════════════════════════════════════════════════════════
def make_label_box(text: str, color, font_size: int = 28) -> VGroup:
    label = Text(text, font_size=font_size, color=WHITE)
    box   = SurroundingRectangle(label, color=color, buff=0.18, corner_radius=0.1)
    box.set_fill(color, opacity=0.25)
    return VGroup(box, label)
