"""Convert Module-1 resource markdown into styled HTML reading pages.

Source-of-truth: the .md files. Run this script to regenerate the .html
artefacts whenever the markdown changes.

Design: matches M1 Lab Guide aesthetic — light reading background, navy
hero, Inter / JetBrains Mono, card-based body. Reads cleanly on screen
and prints cleanly to PDF.
"""

from __future__ import annotations

import re
from pathlib import Path

import markdown as md

MODULES_DIR = Path(__file__).resolve().parent
REPO_ROOT = MODULES_DIR.parent

# (source_md_path, output_html_filename, badge, h1, tagline, accent_hex)
PAGES = [
    (
        MODULES_DIR / "Module 1 - Frameworks Reference Card.md",
        MODULES_DIR / "Module 1 - Frameworks Reference Card.html",
        "Module 1 — Reference Card",
        "Frameworks Reference Card",
        "Every framework Module 1 introduces, in one page. Keep it open while you build.",
        "#a78bfa",
    ),
    (
        MODULES_DIR / "Module 1 - Glossary.md",
        MODULES_DIR / "Module 1 - Glossary.html",
        "Module 1 — Glossary",
        "Glossary",
        "Every term used in Module 1, defined the way we use it — not the way Wikipedia does.",
        "#fde68a",
    ),
    (
        MODULES_DIR / "Module 1 - Notes (Shareable).md",
        MODULES_DIR / "Module 1 - Notes (Shareable).html",
        "Module 1 — Shareable Notes",
        "Shareable Notes",
        "The long-form companion to the deck. Read it before the session, refer back to it after.",
        "#f9a8d4",
    ),
    (
        MODULES_DIR / "Module 1 - Pre-Read.md",
        MODULES_DIR / "Module 1 - Pre-Read.html",
        "Module 1 — Pre-Read",
        "Pre-Read",
        "What to set up before Module 1, and the mental model to bring with you.",
        "#6ee7b7",
    ),
    (
        REPO_ROOT / "Final Project - Requirements and Scenario Guide.md",
        REPO_ROOT / "Final Project - Requirements and Scenario Guide.html",
        "Capstone — Final Project Brief",
        "Final Project · Requirements and Scenario Guide",
        "Scenarios, deliverables, rubric, timeline. The single source of truth for the certification capstone.",
        "#60a5fa",
    ),
]

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · Vibe Coding</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: 'Inter', -apple-system, sans-serif; background: #f5f5f7; min-height: 100vh; padding: 40px 20px 80px; color: #1a1a2e; -webkit-font-smoothing: antialiased; }}
  .page {{ max-width: 880px; margin: 0 auto; }}

  /* Breadcrumb */
  .breadcrumb {{ font-size: 12px; font-weight: 600; color: #6b7280; margin-bottom: 14px; text-transform: uppercase; letter-spacing: 0.06em; }}
  .breadcrumb a {{ color: #3B6FE0; text-decoration: none; }}
  .breadcrumb a:hover {{ text-decoration: underline; }}

  /* Hero */
  .header {{ text-align: center; margin-bottom: 40px; padding: 44px 32px; background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%); border-radius: 16px; color: white; }}
  .badge {{ display: inline-block; font-size: 11px; font-weight: 700; color: {accent}; text-transform: uppercase; letter-spacing: 0.12em; background: rgba(96,165,250,0.12); border: 1px solid rgba(96,165,250,0.3); padding: 6px 16px; border-radius: 20px; margin-bottom: 14px; }}
  .header h1 {{ font-size: 36px; font-weight: 900; margin-bottom: 12px; line-height: 1.15; letter-spacing: -0.015em; }}
  .header p {{ font-size: 15px; color: #94a3b8; line-height: 1.6; max-width: 640px; margin: 0 auto; }}

  /* Body content card */
  .content {{ background: #fff; border-radius: 14px; box-shadow: 0 2px 16px rgba(0,0,0,0.06); padding: 44px 52px; }}

  /* Headings */
  .content h1, .content h2, .content h3, .content h4 {{ font-weight: 800; color: #1a1a2e; line-height: 1.25; letter-spacing: -0.01em; }}
  .content > h1:first-child, .content > h2:first-child {{ margin-top: 0; }}
  .content h1 {{ font-size: 30px; margin: 44px 0 16px; padding-bottom: 12px; border-bottom: 2px solid #e5e7eb; }}
  .content h2 {{ font-size: 24px; margin: 40px 0 14px; padding-bottom: 10px; border-bottom: 1px solid #e5e7eb; }}
  .content h3 {{ font-size: 19px; margin: 32px 0 12px; color: #1e293b; }}
  .content h4 {{ font-size: 16px; margin: 24px 0 8px; color: #334155; }}

  /* Body text */
  .content p {{ font-size: 15px; line-height: 1.75; color: #374151; margin-bottom: 16px; }}
  .content p strong {{ color: #1a1a2e; font-weight: 700; }}
  .content p em {{ color: #1e293b; font-style: italic; }}

  /* Lists */
  .content ul, .content ol {{ margin: 8px 0 18px; padding-left: 26px; }}
  .content li {{ font-size: 15px; line-height: 1.7; color: #374151; margin-bottom: 6px; }}
  .content li strong {{ color: #1a1a2e; }}
  .content ul ul, .content ol ol, .content ul ol, .content ol ul {{ margin: 4px 0 4px; }}

  /* Inline code */
  .content code {{ font-family: 'JetBrains Mono', monospace; font-size: 13px; background: #f1f5f9; color: #be185d; padding: 2px 7px; border-radius: 5px; border: 1px solid #e2e8f0; }}

  /* Code blocks */
  .content pre {{ background: #0d1117; color: #c9d1d9; padding: 18px 22px; border-radius: 10px; overflow-x: auto; margin: 18px 0; font-family: 'JetBrains Mono', monospace; font-size: 13px; line-height: 1.65; }}
  .content pre code {{ background: transparent; color: inherit; padding: 0; border: none; font-size: 13px; }}

  /* Blockquotes */
  .content blockquote {{ background: #eff6ff; border-left: 4px solid #3B6FE0; padding: 14px 22px; margin: 18px 0; border-radius: 0 10px 10px 0; }}
  .content blockquote p {{ font-size: 15px; color: #1e3a8a; margin: 0; line-height: 1.7; }}
  .content blockquote p strong {{ color: #0c2360; }}
  .content blockquote em {{ color: #1e40af; }}

  /* Tables */
  .table-wrap {{ overflow-x: auto; margin: 20px 0; border: 1px solid #e5e7eb; border-radius: 10px; }}
  .content table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
  .content table th {{ background: #1e293b; color: #fff; font-weight: 700; text-align: left; padding: 12px 16px; font-size: 12px; text-transform: uppercase; letter-spacing: 0.06em; }}
  .content table td {{ padding: 12px 16px; border-top: 1px solid #e5e7eb; vertical-align: top; color: #374151; line-height: 1.65; }}
  .content table tr:nth-child(even) td {{ background: #fafbfc; }}
  .content table strong {{ color: #1a1a2e; }}
  .content table code {{ font-size: 12px; }}

  /* Horizontal rule */
  .content hr {{ border: none; height: 1px; background: linear-gradient(90deg, transparent, #cbd5e1 20%, #cbd5e1 80%, transparent); margin: 32px 0; }}

  /* Links */
  .content a {{ color: #3B6FE0; text-decoration: none; border-bottom: 1px solid rgba(59,111,224,0.3); }}
  .content a:hover {{ border-bottom-color: #3B6FE0; }}

  /* Definition-list-ish rendering of "**Term**\\nDefinition" pattern (Glossary) */
  .content p strong:only-child {{ display: block; margin-top: 8px; color: #1a1a2e; font-size: 16px; }}

  /* Footer nav */
  .footer-nav {{ margin-top: 36px; padding: 24px 28px; background: #fff; border-radius: 12px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); display: flex; align-items: center; justify-content: space-between; gap: 18px; flex-wrap: wrap; }}
  .footer-nav .fn-back {{ font-size: 13px; color: #6b7280; }}
  .footer-nav .fn-back a {{ color: #3B6FE0; text-decoration: none; font-weight: 600; }}
  .footer-nav .fn-back a:hover {{ text-decoration: underline; }}
  .footer-nav .fn-siblings {{ display: flex; gap: 8px; flex-wrap: wrap; }}
  .footer-nav .fn-sibling {{ font-size: 12px; color: #6b7280; background: #f1f5f9; padding: 7px 14px; border-radius: 999px; text-decoration: none; border: 1px solid #e2e8f0; font-weight: 600; }}
  .footer-nav .fn-sibling:hover {{ background: #e2e8f0; color: #1a1a2e; }}
  .footer-nav .fn-sibling.current {{ background: #1e293b; color: #fff; border-color: #1e293b; }}

  .footer-note {{ text-align: center; margin-top: 22px; padding: 14px; font-size: 12px; color: #94a3b8; line-height: 1.6; }}
  .footer-note a {{ color: #64748b; text-decoration: none; }}
  .footer-note a:hover {{ color: #3B6FE0; }}

  @media (max-width: 720px) {{
    .content {{ padding: 28px 22px; }}
    .header {{ padding: 32px 22px; }}
    .header h1 {{ font-size: 26px; }}
    .content h1 {{ font-size: 24px; }}
    .content h2 {{ font-size: 20px; }}
  }}

  @media print {{
    body {{ background: #fff; padding: 0; }}
    .breadcrumb, .footer-nav, .footer-note {{ display: none; }}
    .header {{ background: #0f172a !important; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
    .content {{ box-shadow: none; padding: 24px 0; }}
  }}
</style>
</head>
<body>

<div class="page">

  <div class="breadcrumb"><a href="Module 1 - Slides.html">← Module 1 · Execute Vibe Coding Velocity</a></div>

  <div class="header">
    <div class="badge">{badge}</div>
    <h1>{h1}</h1>
    <p>{tagline}</p>
  </div>

  <div class="content">
"""

FOOTER = """  </div>

  <div class="footer-nav">
    <div class="fn-back"><a href="Module 1 - Slides.html">← Back to Module 1 deck</a></div>
    <div class="fn-siblings">
      <a class="fn-sibling{is_frameworks}" href="Module 1 - Frameworks Reference Card.html">Frameworks Card</a>
      <a class="fn-sibling{is_glossary}" href="Module 1 - Glossary.html">Glossary</a>
      <a class="fn-sibling{is_notes}" href="Module 1 - Notes (Shareable).html">Shareable Notes</a>
      <a class="fn-sibling{is_preread}" href="Module 1 - Pre-Read.html">Pre-Read</a>
      <a class="fn-sibling{is_final}" href="../Final Project - Requirements and Scenario Guide.html">Final Project Brief</a>
    </div>
  </div>

  <div class="footer-note">
    Source of truth: <code>{source_name}</code> · regenerate with <code>python3 Modules/_gen_resource_pages.py</code>
  </div>

</div>

</body>
</html>
"""


def render_markdown(text: str) -> str:
    """Convert markdown text to HTML with tables, fenced code, and attr-list."""
    html = md.markdown(
        text,
        extensions=["tables", "fenced_code", "attr_list", "sane_lists"],
        output_format="html",
    )
    html = re.sub(
        r"<table>", '<div class="table-wrap"><table>', html
    )
    html = html.replace("</table>", "</table></div>")
    html = re.sub(r"\]\((?P<href>[^)]+)\.md\b", lambda m: f"]({m.group('href')}.html", html)
    return html


def _sib(is_current: bool) -> str:
    return " current" if is_current else ""


def main() -> None:
    for src, dst, badge, h1, tagline, accent in PAGES:
        if not src.exists():
            print(f"SKIP (missing): {src}")
            continue
        body = render_markdown(src.read_text(encoding="utf-8"))
        head = HEAD.format(title=h1, badge=badge, h1=h1, tagline=tagline, accent=accent)
        footer = FOOTER.format(
            source_name=src.name,
            is_frameworks=_sib(dst.name == "Module 1 - Frameworks Reference Card.html"),
            is_glossary=_sib(dst.name == "Module 1 - Glossary.html"),
            is_notes=_sib(dst.name == "Module 1 - Notes (Shareable).html"),
            is_preread=_sib(dst.name == "Module 1 - Pre-Read.html"),
            is_final=_sib(dst.name == "Final Project - Requirements and Scenario Guide.html"),
        )
        dst.write_text(head + body + footer, encoding="utf-8")
        print(f"WROTE: {dst.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
