"""
latex_compat.py — MathTex fallback wrapper for environments without LaTeX
──────────────────────────────────────────────────────────────────────────
Import this module BEFORE importing from manim in any scene file when
LaTeX is not available. It monkeypatches MathTex to fall back to Text.

Usage:
    import latex_compat   # at top of scene file, before 'from manim import *'
    from manim import *
"""

import os
import subprocess
import sys

def _latex_available() -> bool:
    """Return True if pdflatex (or latex) is on PATH."""
    for cmd in ["pdflatex", "/Library/TeX/texbin/pdflatex", "latex"]:
        try:
            r = subprocess.run([cmd, "--version"],
                               capture_output=True, timeout=3)
            if r.returncode == 0:
                return True
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass
    return False

LATEX_OK = _latex_available()

if not LATEX_OK:
    # Add BasicTeX to PATH if it's installed but not on PATH yet
    tex_paths = [
        "/Library/TeX/texbin",
        "/usr/local/texlive/2024/bin/universal-darwin",
        "/usr/local/texlive/2023/bin/universal-darwin",
    ]
    for p in tex_paths:
        if os.path.isdir(p):
            os.environ["PATH"] = p + ":" + os.environ.get("PATH", "")
            LATEX_OK = _latex_available()
            if LATEX_OK:
                break

if not LATEX_OK:
    print("⚠️  latex_compat: pdflatex not found — MathTex will fall back to Text.")
    print("   Install BasicTeX: brew install --cask basictex")
    print("   Then: sudo tlmgr install standalone preview doublestroke relsize rsfs")
    print()
else:
    print(f"✅  latex_compat: LaTeX found at PATH.")
