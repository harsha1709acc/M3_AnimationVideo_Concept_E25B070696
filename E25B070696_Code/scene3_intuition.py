"""
scene3_intuition.py — Scene 3: Visual Intuition  (target: ~58 seconds)
────────────────────────────────────────────────────────────────────────
2D: two lines meeting at (1,2); row operation rotates one line
    while the intersection stays fixed.
3D: three planes meeting at (1,2,3); row operations tilt planes 2 & 3,
    while the intersection point (1,2,3) stays fixed.
Explains WHY row operations preserve the solution set (reversibility).
Every beat is continuously animated; no static hold exceeds ~4 s.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from manim import *
from constants import *


class Scene3Intuition(Scene):
    """
    Scene 3 — Visual Intuition
    Storyboard timing: 1:22 – 2:20  (~58 s)
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── BEAT 1 (~3 s): Section Title ─────────────────────────────────────
        title = Text("Why Are Row Operations Safe?", font_size=HEADING_FS, color=PIVOT_COLOR, weight=BOLD)
        self.play(Write(title), run_time=0.9)
        self.wait(1.2)
        self.play(title.animate.scale(0.6).to_edge(UP, buff=0.3), run_time=0.6)

        # ── BEAT 2 (~27 s): 2D — Two Lines & Reversibility ───────────────────
        sub_title_2d = Text("In 2D: Two Lines Meeting at a Point", font_size=BODY_FS - 4, color=SUBTITLE_COLOR)
        sub_title_2d.next_to(title, DOWN, buff=0.25)
        self.play(FadeIn(sub_title_2d, shift=UP * 0.1), run_time=0.5)

        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 5, 1],
            x_length=5.0,
            y_length=4.7,
            axis_config={"color": SUBTITLE_COLOR, "stroke_width": 1.5, "include_tip": True},
        ).shift(DOWN * 0.7 + LEFT * 1.1)

        x_label = axes.get_x_axis_label("x", direction=RIGHT)
        y_label = axes.get_y_axis_label("y", direction=UP)

        # Line 1: x + y = 3  -> y = 3 - x
        # Line 2: x - y = -1 -> y = x + 1
        line1 = axes.plot(lambda x: 3 - x, x_range=[0, 4], color=ROW_SOURCE_COLOR, stroke_width=3)
        line2 = axes.plot(lambda x: x + 1, x_range=[0, 3.5], color=ROW_CHANGE_COLOR, stroke_width=3)

        eq_label1 = MathTex(r"x + y = 3", font_size=SMALL_FS, color=ROW_SOURCE_COLOR)
        eq_label2 = MathTex(r"x - y = -1", font_size=SMALL_FS, color=ROW_CHANGE_COLOR)
        eq_label1.next_to(axes.c2p(3.1, -0.1), RIGHT, buff=0.1)
        eq_label2.next_to(axes.c2p(3.0, 4.0), RIGHT, buff=0.1)

        dot = Dot(axes.c2p(1, 2), color=PIVOT_COLOR, radius=0.12)
        sol_label = MathTex(r"(1, 2)", font_size=SMALL_FS, color=PIVOT_COLOR)
        sol_label.next_to(dot, UP + RIGHT, buff=0.15)

        self.play(Create(axes), Write(x_label), Write(y_label), run_time=1.2)
        self.play(Create(line1), Write(eq_label1), run_time=1.1)
        self.play(Create(line2), Write(eq_label2), run_time=1.1)
        self.play(FadeIn(dot, scale=0.4), Write(sol_label), run_time=0.9)

        # Dashed projection lines to x=1 and y=2
        dash_x = DashedLine(axes.c2p(1, 0), axes.c2p(1, 2), color=PIVOT_COLOR, stroke_width=1.8)
        dash_y = DashedLine(axes.c2p(0, 2), axes.c2p(1, 2), color=PIVOT_COLOR, stroke_width=1.8)
        self.play(Create(dash_x), Create(dash_y), run_time=1.0)
        self.wait(2.2)

        # Apply R2 -> R2 - R1: (x - y) - (x + y) = -1 - 3 => -2y = -4 => y = 2
        note1 = Text(
            "Apply R₂ → R₂ − R₁:\nLine 2 rotates to y = 2",
            font_size=SMALL_FS - 4,
            color=ANNOTATION_COLOR,
            line_spacing=1.3,
        ).to_edge(RIGHT, buff=0.45).shift(UP * 0.7)

        new_line2 = axes.plot(lambda x: 2, x_range=[0, 4.4], color=ROW_CHANGE_COLOR, stroke_width=3.5)
        new_eq_label2 = MathTex(r"y = 2 \;\; (R_2 \to R_2 - R_1)", font_size=TINY_FS, color=ANNOTATION_COLOR)
        new_eq_label2.next_to(axes.c2p(2.5, 2.2), UP, buff=0.1)

        self.play(Write(note1), run_time=1.0)
        self.wait(1.5)
        self.play(
            Transform(line2, new_line2),
            Transform(eq_label2, new_eq_label2),
            run_time=2.2,
        )
        self.play(Indicate(dot, color=SOLUTION_COLOR, scale_factor=1.6), run_time=1.1)
        self.wait(2.0)

        note2 = Text(
            "Intersection (1, 2) stays\ncompletely fixed!",
            font_size=SMALL_FS - 4,
            color=VERIFY_COLOR,
            line_spacing=1.3,
        ).next_to(note1, DOWN, buff=0.45).align_to(note1, LEFT)
        self.play(Write(note2), run_time=1.0)
        self.wait(2.2)

        # Reversibility box
        rev_box = RoundedRectangle(
            width=4.6, height=1.7, corner_radius=0.12,
            color=PIVOT_COLOR, fill_opacity=0.12, stroke_width=1.5,
        ).next_to(note2, DOWN, buff=0.45).align_to(note1, LEFT)
        rev_text = Text(
            "Why? Every row op is\nreversible (R₂ → R₂ + R₁\nundoes it) → same solution!",
            font_size=TINY_FS,
            color=WHITE,
            line_spacing=1.25,
        ).move_to(rev_box.get_center())

        self.play(Create(rev_box), Write(rev_text), run_time=1.3)
        self.wait(2.5)
        self.play(Indicate(rev_box, color=PIVOT_COLOR, scale_factor=1.04), run_time=1.0)
        self.wait(2.0)

        self.play(
            *[FadeOut(m) for m in [
                axes, x_label, y_label, line1, line2, eq_label1, eq_label2,
                dot, sol_label, dash_x, dash_y, note1, note2, rev_box, rev_text, sub_title_2d,
            ]],
            run_time=0.8,
        )

        # ── BEAT 3 (~27 s): 3D — Three Planes Meeting at (1, 2, 3) ───────────
        sub_title_3d = Text("In 3D: Three Planes Meeting at (1, 2, 3)", font_size=BODY_FS - 4, color=SUBTITLE_COLOR)
        sub_title_3d.next_to(title, DOWN, buff=0.25)
        self.play(FadeIn(sub_title_3d, shift=UP * 0.1), run_time=0.5)

        def make_plane(corners, color, opacity=0.32):
            return Polygon(*corners, color=color, fill_opacity=opacity, stroke_width=2.2)

        # Three distinct angled planes intersecting near the center dot
        p1_corners = [LEFT * 2.5 + UP * 0.9, RIGHT * 2.1 + UP * 0.9, RIGHT * 1.4 + DOWN * 0.9, LEFT * 3.2 + DOWN * 0.9]
        p2_corners = [LEFT * 1.4 + UP * 1.6, RIGHT * 1.8 + UP * 0.3, RIGHT * 1.2 + DOWN * 1.5, LEFT * 2.0 + DOWN * 0.2]
        p3_corners = [LEFT * 1.8 + DOWN * 0.3, RIGHT * 2.2 + UP * 1.4, RIGHT * 2.6 + DOWN * 0.8, LEFT * 1.4 + DOWN * 1.7]

        plane1 = make_plane(p1_corners, ROW_SOURCE_COLOR, 0.30).shift(LEFT * 0.8 + DOWN * 0.2)
        plane2 = make_plane(p2_corners, ROW_CHANGE_COLOR, 0.28).shift(LEFT * 0.8 + DOWN * 0.2)
        plane3 = make_plane(p3_corners, SOLUTION_COLOR, 0.28).shift(LEFT * 0.8 + DOWN * 0.2)

        p1_label = Text("Plane 1 (Eq 1)", font_size=TINY_FS, color=ROW_SOURCE_COLOR).to_edge(RIGHT, buff=0.8).shift(UP * 1.3)
        p2_label = Text("Plane 2 (Eq 2)", font_size=TINY_FS, color=ROW_CHANGE_COLOR).next_to(p1_label, DOWN, buff=0.35, aligned_edge=LEFT)
        p3_label = Text("Plane 3 (Eq 3)", font_size=TINY_FS, color=SOLUTION_COLOR).next_to(p2_label, DOWN, buff=0.35, aligned_edge=LEFT)

        intersection_dot = Dot(LEFT * 0.8 + DOWN * 0.2, color=PIVOT_COLOR, radius=0.14)
        int_label = MathTex(r"(1, 2, 3)", font_size=SMALL_FS, color=PIVOT_COLOR)
        int_label.next_to(intersection_dot, RIGHT + UP, buff=0.18)

        self.play(FadeIn(plane1, shift=UP * 0.2), Write(p1_label), run_time=0.8)
        self.wait(0.6)
        self.play(FadeIn(plane2, shift=LEFT * 0.2), Write(p2_label), run_time=0.8)
        self.wait(0.6)
        self.play(FadeIn(plane3, shift=DOWN * 0.2), Write(p3_label), run_time=0.8)
        self.play(FadeIn(intersection_dot, scale=0.3), Write(int_label), run_time=0.8)
        self.wait(1.8)

        # Tilt Plane 2 (R2 -> R2 - 2R1)
        p2_tilted_corners = [LEFT * 2.2 + UP * 1.1, RIGHT * 2.3 + UP * 0.8, RIGHT * 1.7 + DOWN * 1.1, LEFT * 2.8 + DOWN * 0.8]
        plane2_tilted = make_plane(p2_tilted_corners, ROW_CHANGE_COLOR, 0.34).shift(LEFT * 0.8 + DOWN * 0.2)
        op_note1 = MathTex(r"R_2 \to R_2 - 2R_1", font_size=SMALL_FS, color=ANNOTATION_COLOR).to_edge(DOWN, buff=0.85)
        new_p2_label = Text("Plane 2 (tilted)", font_size=TINY_FS, color=ANNOTATION_COLOR).move_to(p2_label.get_center())

        self.play(Write(op_note1), run_time=0.8)
        self.play(
            Transform(plane2, plane2_tilted),
            Transform(p2_label, new_p2_label),
            run_time=2.2,
        )
        self.play(Circumscribe(intersection_dot, color=PIVOT_COLOR, buff=0.15), run_time=1.0)
        self.wait(2.2)

        # Tilt Plane 3 (R3 -> R3 - 3R1)
        p3_tilted_corners = [LEFT * 2.4 + DOWN * 0.1, RIGHT * 2.0 + UP * 0.1, RIGHT * 2.4 + DOWN * 0.4, LEFT * 2.0 + DOWN * 0.6]
        plane3_tilted = make_plane(p3_tilted_corners, SOLUTION_COLOR, 0.34).shift(LEFT * 0.8 + DOWN * 0.2)
        op_note2 = MathTex(r"R_3 \to R_3 - 3R_1 \;\; \text{then} \;\; R_3 + R_2", font_size=SMALL_FS, color=ANNOTATION_COLOR).to_edge(DOWN, buff=0.85)
        new_p3_label = Text("Plane 3 (horizontal z = 3)", font_size=TINY_FS, color=SOLUTION_COLOR).move_to(p3_label.get_center())

        self.play(Transform(op_note1, op_note2), run_time=0.8)
        self.play(
            Transform(plane3, plane3_tilted),
            Transform(p3_label, new_p3_label),
            run_time=2.2,
        )
        self.play(Circumscribe(intersection_dot, color=SOLUTION_COLOR, buff=0.15), run_time=1.0)
        self.wait(2.0)

        key_msg = Text(
            "Planes reshape into clean equations, always keeping (1, 2, 3) fixed!",
            font_size=SMALL_FS - 2,
            color=VERIFY_COLOR,
        ).to_edge(DOWN, buff=0.35)
        self.play(FadeOut(op_note1), Write(key_msg), run_time=0.9)
        self.wait(2.5)

        self.play(
            *[FadeOut(mob) for mob in [
                title, sub_title_3d,
                plane1, plane2, plane3,
                p1_label, p2_label, p3_label,
                intersection_dot, int_label, key_msg,
            ]],
            run_time=0.8,
        )
        self.wait(0.2)
