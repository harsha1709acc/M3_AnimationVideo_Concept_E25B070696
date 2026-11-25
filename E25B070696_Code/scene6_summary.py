"""
scene6_summary.py — Scene 6: Summary & Credits  (target: ~26 seconds)
───────────────────────────────────────────────────────────────────────
Three key takeaways, references, and AI-tool disclosure.
No background music credit, no AI voice-over mention (student records VO).
Every beat is continuously animated; no static hold exceeds ~4 s.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from manim import *
from constants import *


class Scene6Summary(Scene):
    """
    Scene 6 — Summary & Credits
    Storyboard timing: 4:36 – 5:02  (~26 s)
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── BEAT 1 (~12.5 s): Three Key Takeaways ────────────────────────────
        summary_title = Text("Three Key Takeaways", font_size=HEADING_FS, color=PIVOT_COLOR, weight=BOLD)
        self.play(Write(summary_title), run_time=0.8)
        self.play(summary_title.animate.to_edge(UP, buff=0.5), run_time=0.5)

        def takeaway_card(number: str, text: str, num_color) -> VGroup:
            num = Text(number, font_size=HEADING_FS, color=num_color, weight=BOLD)
            msg = Text(text, font_size=SMALL_FS, color=WHITE, line_spacing=1.3)
            msg.next_to(num, RIGHT, buff=0.4, aligned_edge=UP)
            group = VGroup(num, msg)
            bg = RoundedRectangle(
                width=group.width + 0.65,
                height=group.height + 0.4,
                corner_radius=0.15,
                color=num_color,
                fill_opacity=0.1,
                stroke_width=1.5,
            ).move_to(group.get_center())
            return VGroup(bg, group)

        t1 = takeaway_card(
            "1.",
            "Row operations preserve the solution set\n— every operation is reversible.",
            ROW_SOURCE_COLOR,
        )
        t2 = takeaway_card(
            "2.",
            "Eliminate below each pivot, left to right,\nto reach Row-Echelon Form.",
            PIVOT_COLOR,
        )
        t3 = takeaway_card(
            "3.",
            "Back-substitute from the bottom row up\nto solve for every unknown.",
            ROW_CHANGE_COLOR,
        )

        cards = VGroup(t1, t2, t3).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        cards.next_to(summary_title, DOWN, buff=0.45).center()

        for card in [t1, t2, t3]:
            self.play(FadeIn(card, shift=RIGHT * 0.4), run_time=0.7)
            self.wait(1.6)
            self.play(Indicate(card, color=PIVOT_COLOR, scale_factor=1.02), run_time=0.6)

        self.wait(1.5)
        self.play(FadeOut(cards), run_time=0.5)

        # ── BEAT 2 (~6 s): References ────────────────────────────────────────
        refs_title = Text("References", font_size=BODY_FS, color=SUBTITLE_COLOR, weight=BOLD)
        refs_title.next_to(summary_title, DOWN, buff=0.45)

        refs = VGroup(
            Text("[1] Strang, G. (2016). Introduction to Linear Algebra, 5th ed. Wellesley-Cambridge.", font_size=TINY_FS, color=WHITE),
            Text("[2] Anton, H. & Rorres, C. Elementary Linear Algebra, 11th ed. Wiley.", font_size=TINY_FS, color=WHITE),
            Text("[3] Lay, D. Linear Algebra and Its Applications, 5th ed. Pearson.", font_size=TINY_FS, color=WHITE),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        refs.next_to(refs_title, DOWN, buff=0.4).center()

        self.play(Write(refs_title), run_time=0.5)
        self.play(FadeIn(refs[0], shift=UP * 0.15), run_time=0.6)
        self.play(FadeIn(refs[1], shift=UP * 0.15), run_time=0.6)
        self.play(FadeIn(refs[2], shift=UP * 0.15), run_time=0.6)
        self.wait(2.5)

        # ── BEAT 3 (~7.5 s): Closing Credits & AI Disclosure ─────────────────
        self.play(FadeOut(refs_title), FadeOut(refs), run_time=0.5)

        disclosure = Text(
            "AI tools (Google Antigravity / Gemini) were used to help write\n"
            "the animation code and narration script text;\n"
            "the voice-over is recorded by the student, and all mathematics was verified by the student.",
            font_size=TINY_FS,
            color=SUBTITLE_COLOR,
            line_spacing=1.4,
        )
        student_line = Text(
            "Harshavardhan Rambha  ·  E25B070696",
            font_size=SMALL_FS,
            color=PIVOT_COLOR,
            weight=BOLD,
        )
        course_line = Text(
            "M3 Linear Algebra & Calculus — Internal Assessment",
            font_size=TINY_FS,
            color=WHITE,
        )

        credits_lines = VGroup(disclosure, student_line, course_line).arrange(DOWN, buff=0.45).center()

        self.play(FadeIn(disclosure, shift=UP * 0.2), run_time=0.9)
        self.wait(2.2)
        self.play(FadeIn(student_line, shift=UP * 0.15), FadeIn(course_line, shift=UP * 0.15), run_time=1.0)
        self.wait(3.8)

        self.play(
            FadeOut(summary_title),
            FadeOut(credits_lines),
            run_time=0.9,
        )
        self.wait(0.3)
