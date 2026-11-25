"""
scene1_hook.py — Scene 1: Hook / Context  (target: ~38 seconds)
────────────────────────────────────────────────────────────────
Poses the question "How do we solve 3 equations in 3 unknowns
systematically, the way a computer does?" and shows the messy
system alongside a visual staircase hint.
Every beat is continuously animated; no static hold exceeds ~4 s.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from manim import *
from constants import *


class Scene1Hook(Scene):
    """
    Scene 1 — Hook / Context
    Storyboard timing: 0:00 – 0:38  (~38 s)
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── BEAT 1 (~7.5 s): Opening Frame (Title, Concept, Name & ID) ───────
        title = Text(
            "Gaussian Elimination",
            font_size=TITLE_FS,
            color=TITLE_COLOR,
            weight=BOLD,
        )
        subtitle = Text(
            "Solving 3×3 Linear Systems Systematically",
            font_size=SMALL_FS,
            color=SUBTITLE_COLOR,
        ).next_to(title, DOWN, buff=0.4)

        byline = Text(
            "Harshavardhan Rambha  ·  E25B070696",
            font_size=TINY_FS,
            color=PIVOT_COLOR,
        ).next_to(subtitle, DOWN, buff=0.35)

        course = Text(
            "M3 Linear Algebra & Calculus — Internal Assessment",
            font_size=TINY_FS,
            color=SUBTITLE_COLOR,
        ).next_to(byline, DOWN, buff=0.18)

        title_group = VGroup(title, subtitle, byline, course).center()

        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.8)
        self.play(FadeIn(byline, shift=UP * 0.1), FadeIn(course, shift=UP * 0.1), run_time=0.7)
        self.wait(1.8)
        self.play(Indicate(title, color=PIVOT_COLOR, scale_factor=1.04), run_time=0.9)
        self.wait(1.3)
        self.play(FadeOut(title_group), run_time=0.6)

        # ── BEAT 2 (~9.5 s): The Central Question ────────────────────────────
        question = Text(
            "How do we solve 3 equations\nin 3 unknowns systematically,\nthe way a computer does?",
            font_size=HEADING_FS - 4,
            color=TITLE_COLOR,
            line_spacing=1.4,
            t2c={"systematically": PIVOT_COLOR, "computer": ROW_SOURCE_COLOR},
        ).center()

        q_box = SurroundingRectangle(question, color=ROW_CHANGE_COLOR, buff=0.35, corner_radius=0.15)
        q_box.set_stroke(opacity=0.6, width=2)

        self.play(Write(question), run_time=2.2)
        self.wait(1.5)
        self.play(Create(q_box), run_time=1.0)
        self.wait(2.2)
        self.play(Indicate(question, scale_factor=1.03, color=PIVOT_COLOR), run_time=1.0)
        self.wait(1.0)
        self.play(FadeOut(question), FadeOut(q_box), run_time=0.6)

        # ── BEAT 3 (~11.5 s): Introduce Our 3×3 System ───────────────────────
        sys_label = Text("Our 3×3 Linear System:", font_size=BODY_FS, color=SUBTITLE_COLOR)
        sys_label.to_edge(UP, buff=0.7)

        eq1 = MathTex(r"x + 2y + z &= 8", font_size=BODY_FS, color=WHITE)
        eq2 = MathTex(r"2x + 3y + 4z &= 20", font_size=BODY_FS, color=WHITE)
        eq3 = MathTex(r"3x + 7y + 2z &= 23", font_size=BODY_FS, color=WHITE)

        eqs = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        brace_eqs = MathTex(r"\left\{", font_size=BODY_FS * 2.5, color=PIVOT_COLOR)
        brace_eqs.next_to(eqs, LEFT, buff=0.15)
        system_group = VGroup(brace_eqs, eqs).center().shift(UP * 0.6)

        self.play(Write(sys_label), run_time=0.6)
        self.play(Write(brace_eqs), run_time=0.4)
        self.play(Write(eq1), run_time=0.9)
        self.wait(0.8)
        self.play(Write(eq2), run_time=0.9)
        self.wait(0.8)
        self.play(Write(eq3), run_time=0.9)
        self.wait(1.5)

        unknowns_note = Text(
            "3 equations, 3 unknowns (x, y, z) — all tangled together",
            font_size=SMALL_FS - 2,
            color=ROW_CHANGE_COLOR,
        ).next_to(system_group, DOWN, buff=0.55)
        self.play(FadeIn(unknowns_note, shift=UP * 0.15), run_time=0.7)
        self.wait(2.5)
        self.play(FadeOut(unknowns_note), run_time=0.5)

        # ── BEAT 4 (~9.5 s): Hint at the Staircase & Goal ────────────────────
        hint_label = Text(
            "We will reshape this into a staircase → then solve bottom-up!",
            font_size=SMALL_FS - 2,
            color=ANNOTATION_COLOR,
        ).to_edge(DOWN, buff=0.8)

        step1 = Square(side_length=0.45, color=PIVOT_COLOR, fill_opacity=0.75).shift(LEFT * 1.1 + UP * 0.5)
        step2 = Square(side_length=0.45, color=ROW_CHANGE_COLOR, fill_opacity=0.75).shift(LEFT * 0.2 + UP * 0.0)
        step3 = Square(side_length=0.45, color=ROW_SOURCE_COLOR, fill_opacity=0.75).shift(RIGHT * 0.7 + DOWN * 0.5)
        stair_arr1 = Arrow(step1.get_bottom(), step2.get_left(), color=WHITE, buff=0.05, stroke_width=2)
        stair_arr2 = Arrow(step2.get_bottom(), step3.get_left(), color=WHITE, buff=0.05, stroke_width=2)
        staircase = VGroup(step1, step2, step3, stair_arr1, stair_arr2).next_to(hint_label, UP, buff=0.35)

        self.play(system_group.animate.shift(UP * 0.4), run_time=0.5)
        self.play(FadeIn(hint_label, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(step1, scale=0.6), run_time=0.5)
        self.play(Create(stair_arr1), FadeIn(step2, scale=0.6), run_time=0.6)
        self.play(Create(stair_arr2), FadeIn(step3, scale=0.6), run_time=0.6)
        self.wait(2.2)

        goal_chip = Text(
            "Target answer: (x, y, z) = (1, 2, 3)",
            font_size=SMALL_FS - 2,
            color=SOLUTION_COLOR,
        ).next_to(staircase, RIGHT, buff=0.6)
        self.play(Write(goal_chip), run_time=1.0)
        self.wait(4.0)

        self.play(
            FadeOut(sys_label),
            FadeOut(system_group),
            FadeOut(hint_label),
            FadeOut(staircase),
            FadeOut(goal_chip),
            run_time=0.8,
        )
        self.wait(0.3)
