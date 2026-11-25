"""
scene2_concepts.py — Scene 2: Concept Introduction  (target: ~44 seconds)
────────────────────────────────────────────────────────────────────────────
Defines: system of linear equations, augmented matrix [A|b],
the three elementary row operations, pivot, and row-echelon form.
States the learning objective on screen.
Every beat is continuously animated; no static hold exceeds ~4 s.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from manim import *
from constants import *
from matrix_helpers import AugmentedMatrixMob, make_label_box


class Scene2Concepts(Scene):
    """
    Scene 2 — Concept Introduction
    Storyboard timing: 0:38 – 1:22  (~44 s)
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── BEAT 1 (~8 s): Linear System Definition ──────────────────────────
        heading = Text(
            "Key Definitions",
            font_size=HEADING_FS,
            color=PIVOT_COLOR,
            weight=BOLD,
        ).to_edge(UP, buff=0.45)

        defn1_title = Text("1. Linear System (first-power unknowns only):", font_size=SMALL_FS, color=SUBTITLE_COLOR)
        defn1_eq = MathTex(
            r"a_{11}x + a_{12}y + a_{13}z &= b_1 \\",
            r"a_{21}x + a_{22}y + a_{23}z &= b_2 \\",
            r"a_{31}x + a_{32}y + a_{33}z &= b_3",
            font_size=SMALL_FS,
        )
        defn1_eq.set_color_by_tex("a_", WHITE).set_color_by_tex("b_", SOLUTION_COLOR)
        defn1 = VGroup(defn1_title, defn1_eq).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        defn1.next_to(heading, DOWN, buff=0.45).to_edge(LEFT, buff=0.9)

        self.play(Write(heading), run_time=0.6)
        self.play(FadeIn(defn1_title, shift=RIGHT * 0.2), run_time=0.5)
        self.play(Write(defn1_eq), run_time=1.4)
        self.wait(2.0)

        lin_note = Text("No x², xy, or sin(x) terms", font_size=TINY_FS, color=VERIFY_COLOR)
        lin_note.next_to(defn1_eq, RIGHT, buff=0.7)
        self.play(FadeIn(lin_note, shift=LEFT * 0.2), run_time=0.6)
        self.wait(2.0)
        self.play(FadeOut(lin_note), run_time=0.4)

        # ── BEAT 2 (~10 s): Augmented Matrix [A | b] ─────────────────────────
        aug_title = Text("2. Augmented Matrix  [A | b]:", font_size=SMALL_FS, color=SUBTITLE_COLOR)
        aug_title.next_to(defn1, DOWN, buff=0.45).align_to(defn1, LEFT)

        mat_rows = [
            ["1",  "2",  "1",  "8"],
            ["2",  "3",  "4",  "20"],
            ["3",  "7",  "2",  "23"],
        ]
        aug_mat = AugmentedMatrixMob(mat_rows, font_size=SMALL_FS, cell_width=0.8, cell_height=0.62)
        aug_mat.next_to(aug_title, DOWN, buff=0.3).align_to(aug_title, LEFT).shift(RIGHT * 0.4)

        self.play(FadeIn(aug_title, shift=UP * 0.1), run_time=0.5)
        self.play(Create(aug_mat), run_time=1.1)
        self.wait(1.2)

        a_brace = Brace(
            VGroup(*[aug_mat.entries[r][c] for r in range(3) for c in range(3)]),
            direction=DOWN, color=ROW_CHANGE_COLOR,
        )
        a_text = MathTex("A\\text{ (coefficients)}", font_size=TINY_FS, color=ROW_CHANGE_COLOR)
        a_text.next_to(a_brace, DOWN, buff=0.15)

        b_brace = Brace(
            VGroup(*[aug_mat.entries[r][3] for r in range(3)]),
            direction=DOWN, color=SOLUTION_COLOR,
        )
        b_text = MathTex("b\\text{ (RHS)}", font_size=TINY_FS, color=SOLUTION_COLOR)
        b_text.next_to(b_brace, DOWN, buff=0.15)

        self.play(GrowFromCenter(a_brace), Write(a_text), run_time=0.8)
        self.wait(1.2)
        self.play(GrowFromCenter(b_brace), Write(b_text), run_time=0.8)
        self.wait(1.5)
        self.play(Indicate(aug_mat.separator, color=SEPARATOR_COLOR, scale_factor=1.15), run_time=0.7)
        self.wait(1.2)
        self.play(
            FadeOut(a_brace), FadeOut(a_text), FadeOut(b_brace), FadeOut(b_text),
            FadeOut(defn1), FadeOut(aug_title), FadeOut(aug_mat),
            run_time=0.6,
        )

        # ── BEAT 3 (~12 s): Three Elementary Row Operations ──────────────────
        ops_heading = Text("3. The 3 Elementary Row Operations", font_size=BODY_FS, color=PIVOT_COLOR, weight=BOLD)
        ops_heading.next_to(heading, DOWN, buff=0.45)

        op1 = VGroup(
            make_label_box("Op 1: Swap", ROW_SOURCE_COLOR, font_size=SMALL_FS),
            MathTex(r"R_i \leftrightarrow R_j", font_size=SMALL_FS),
        ).arrange(RIGHT, buff=0.4)

        op2 = VGroup(
            make_label_box("Op 2: Scale", PIVOT_COLOR, font_size=SMALL_FS),
            MathTex(r"R_i \to k \cdot R_i \quad (k \neq 0)", font_size=SMALL_FS),
        ).arrange(RIGHT, buff=0.4)

        op3 = VGroup(
            make_label_box("Op 3: Replace", ROW_CHANGE_COLOR, font_size=SMALL_FS),
            MathTex(r"R_i \to R_i + k \cdot R_j", font_size=SMALL_FS),
        ).arrange(RIGHT, buff=0.4)

        why = Text(
            "Every operation is reversible → solution set is unchanged!",
            font_size=SMALL_FS - 2,
            color=VERIFY_COLOR,
        )

        ops_group = VGroup(op1, op2, op3, why).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        ops_group.next_to(ops_heading, DOWN, buff=0.45).center().shift(UP * 0.25)

        self.play(Write(ops_heading), run_time=0.6)
        self.play(FadeIn(op1, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(1.4)
        self.play(FadeIn(op2, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(1.4)
        self.play(FadeIn(op3, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(1.5)
        self.play(Indicate(op3, color=ROW_CHANGE_COLOR, scale_factor=1.04), run_time=0.7)
        self.play(Write(why), run_time=0.9)
        self.wait(2.0)

        # ── BEAT 4 (~6.5 s): Pivot & Row-Echelon Form ────────────────────────
        pivot_def = VGroup(
            Text("Pivot:", font_size=SMALL_FS, color=PIVOT_COLOR, weight=BOLD),
            Text("first non-zero entry in a row", font_size=SMALL_FS, color=WHITE),
        ).arrange(RIGHT, buff=0.3)

        ref_def = VGroup(
            Text("Row-Echelon Form:", font_size=SMALL_FS, color=ROW_CHANGE_COLOR, weight=BOLD),
            Text("each pivot is strictly right of the pivot above", font_size=SMALL_FS - 2, color=WHITE),
        ).arrange(RIGHT, buff=0.3)

        defs = VGroup(pivot_def, ref_def).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        defs.to_edge(DOWN, buff=0.65)

        self.play(FadeIn(pivot_def, shift=UP * 0.2), run_time=0.7)
        self.wait(1.8)
        self.play(FadeIn(ref_def, shift=UP * 0.2), run_time=0.7)
        self.wait(2.5)

        self.play(FadeOut(ops_heading), FadeOut(ops_group), FadeOut(defs), run_time=0.6)

        # ── BEAT 5 (~8.5 s): Learning Objective ──────────────────────────────
        obj_box_bg = RoundedRectangle(
            width=12.6, height=3.0,
            corner_radius=0.2,
            color=PIVOT_COLOR,
            fill_opacity=0.12,
            stroke_width=2,
        ).center()

        obj_label = Text("Learning Objective", font_size=SMALL_FS, color=PIVOT_COLOR, weight=BOLD)
        obj_label.next_to(obj_box_bg, UP, buff=0.15)

        obj_line1 = Text(
            "By the end of this video, the viewer will be able to explain\n"
            "how Gaussian elimination turns a 3×3 linear system into",
            font_size=SMALL_FS - 3,
            color=WHITE,
            line_spacing=1.35,
        )
        obj_line2 = Text(
            "echelon form and solves it by back-substitution,\n"
            "and why the row operations never change the solution.",
            font_size=SMALL_FS - 3,
            color=VERIFY_COLOR,
            line_spacing=1.35,
        )
        obj_text = VGroup(obj_line1, obj_line2).arrange(DOWN, buff=0.2).move_to(obj_box_bg.get_center())

        self.play(Create(obj_box_bg), Write(obj_label), run_time=0.7)
        self.play(Write(obj_line1), run_time=1.4)
        self.wait(1.5)
        self.play(Write(obj_line2), run_time=1.6)
        self.wait(4.3)

        self.play(
            FadeOut(heading), FadeOut(obj_box_bg), FadeOut(obj_label), FadeOut(obj_text),
            run_time=0.8,
        )
        self.wait(0.2)
