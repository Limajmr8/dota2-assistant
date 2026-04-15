#!/usr/bin/env python3
"""
Build a single clean PDF from the 4 NPSC markdown deliverables (no external deps).
"""

from pathlib import Path
from typing import List, Tuple


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "NPSC_Crack_Kit.pdf"
QUALITY_GATE = ROOT / "pdf_build_quality_gate.md"
PRODUCT_TITLE = "NPSC CRACK KIT"
WRAP_CHARS_BODY = 86
WRAP_CHARS_HEADING = 70
INPUT_FILES: List[Tuple[str, Path]] = [
    ("Deliverable 1 - 260 Questions", ROOT / "npsc_260_questions.md"),
    ("Deliverable 2 - 90-Day Study Strategy", ROOT / "npsc_study_strategy.md"),
    ("Deliverable 3 - ChatGPT Quiz Prompts", ROOT / "npsc_chatgpt_quiz_prompts.md"),
    ("Deliverable 4 - Product + Sales Copy", ROOT / "npsc_product_readme.md"),
]


PAGE_WIDTH = 595
PAGE_HEIGHT = 842
MARGIN_LEFT = 50
MARGIN_RIGHT = 50
MARGIN_TOP = 60
MARGIN_BOTTOM = 60
QUALITY_GATE_REQUIRED_MARKERS = [
    "Gate status: READY",
    "- [x] No missing sections in source files",
    "- [x] No duplicated headings or duplicate blocks that create noisy PDF output",
    "- [x] Offer/copy is current and not stale vs active funnel messaging and price tier",
]


def _escape_pdf_text(s: str) -> str:
    return (
        s.replace("\\", "\\\\")
        .replace("(", "\\(")
        .replace(")", "\\)")
        .replace("\n", " ")
        .replace("\r", " ")
        .replace("\t", " ")
        .replace("\x00", "")
    )


def _wrap_text(text: str, max_chars: int) -> List[str]:
    text = " ".join(text.split())
    if not text:
        return [""]
    words = text.split(" ")
    lines: List[str] = []
    current = words[0]
    for word in words[1:]:
        candidate = f"{current} {word}"
        if len(candidate) <= max_chars:
            current = candidate
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


def _to_text_blocks(md_text: str) -> List[Tuple[str, int]]:
    """
    Convert markdown to list of (line_text, font_size).
    """
    blocks: List[Tuple[str, int]] = []
    for raw in md_text.splitlines():
        line = raw.rstrip()
        if not line:
            blocks.append(("", 11))
            continue
        if line.startswith("# "):
            blocks.append((line[2:].strip(), 18))
            continue
        if line.startswith("## "):
            blocks.append((line[3:].strip(), 14))
            continue
        if line.startswith("### "):
            blocks.append((line[4:].strip(), 12))
            continue
        if line.startswith("- "):
            line = f"• {line[2:].strip()}"
        blocks.append((line, 11))
    return blocks


def _validate_quality_gate(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(
            f"Missing PDF quality gate file: {path}\n"
            "Create/complete pdf_build_quality_gate.md before running the build."
        )
    content = path.read_text(encoding="utf-8")
    missing_markers = [marker for marker in QUALITY_GATE_REQUIRED_MARKERS if marker not in content]
    if missing_markers:
        raise RuntimeError(
            "PDF quality gate is incomplete. Missing required checklist marker(s):\n- "
            + "\n- ".join(missing_markers)
            + "\nComplete pdf_build_quality_gate.md before running the build."
        )


def build_pdf(output_path: Path) -> None:
    pages: List[str] = []
    current_page_ops: List[str] = []
    y = PAGE_HEIGHT - MARGIN_TOP

    def add_new_page() -> None:
        nonlocal current_page_ops, y
        if current_page_ops:
            pages.append("\n".join(current_page_ops))
        current_page_ops = []
        y = PAGE_HEIGHT - MARGIN_TOP

    def write_line(text: str, size: int = 11) -> None:
        nonlocal y
        line_height = size + 4
        if y - line_height < MARGIN_BOTTOM:
            add_new_page()
        font = "Helvetica-Bold" if size >= 14 else "Helvetica"
        escaped = _escape_pdf_text(text)
        current_page_ops.append(
            f"BT /{font} {size} Tf 1 0 0 1 {MARGIN_LEFT} {y} Tm ({escaped}) Tj ET"
        )
        y -= line_height

    # Cover
    write_line(PRODUCT_TITLE, 24)
    write_line("Compiled Study + Sales Package", 14)
    y -= 10
    for title, _ in INPUT_FILES:
        write_line(f"• {title}", 12)
    add_new_page()

    # Content
    for title, path in INPUT_FILES:
        write_line("-" * 48, 11)
        write_line(title, 16)
        write_line(f"Source: {path.name}", 10)
        y -= 6
        content = path.read_text(encoding="utf-8")
        for line, size in _to_text_blocks(content):
            # Character wrap limits tuned for A4 page width and current font sizes.
            max_chars = WRAP_CHARS_BODY if size <= 11 else WRAP_CHARS_HEADING
            wrapped = _wrap_text(line, max_chars)
            for wline in wrapped:
                write_line(wline, size)
        y -= 8
        add_new_page()

    if current_page_ops:
        pages.append("\n".join(current_page_ops))

    # Build PDF objects
    objects: List[bytes] = []

    def add_obj(obj_text: str) -> int:
        objects.append(obj_text.encode("latin-1", errors="replace"))
        return len(objects)

    font_helv_id = add_obj("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    font_helv_bold_id = add_obj("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")

    content_ids: List[int] = []
    page_ids: List[int] = []

    for page_ops in pages:
        stream = page_ops.encode("latin-1", errors="replace")
        content_obj = (
            f"<< /Length {len(stream)} >>\nstream\n".encode("latin-1")
            + stream
            + b"\nendstream"
        )
        objects.append(content_obj)
        content_id = len(objects)
        content_ids.append(content_id)

        page_obj = (
            "<< /Type /Page /Parent {PAGES_ID} 0 R /MediaBox [0 0 595 842] "
            f"/Resources << /Font << /Helvetica {font_helv_id} 0 R /Helvetica-Bold {font_helv_bold_id} 0 R >> >> "
            f"/Contents {content_id} 0 R >>"
        )
        page_id = add_obj(page_obj)
        page_ids.append(page_id)

    kids = " ".join(f"{pid} 0 R" for pid in page_ids)
    pages_obj_id = add_obj(f"<< /Type /Pages /Kids [{kids}] /Count {len(page_ids)} >>")
    catalog_id = add_obj(f"<< /Type /Catalog /Pages {pages_obj_id} 0 R >>")

    # Replace {PAGES_ID}
    for i, obj in enumerate(objects):
        if b"{PAGES_ID}" in obj:
            objects[i] = obj.replace(b"{PAGES_ID}", str(pages_obj_id).encode("latin-1"))

    # Write final PDF
    out = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for idx, obj in enumerate(objects, start=1):
        offsets.append(len(out))
        out.extend(f"{idx} 0 obj\n".encode("latin-1"))
        out.extend(obj)
        out.extend(b"\nendobj\n")

    xref_start = len(out)
    out.extend(f"xref\n0 {len(objects)+1}\n".encode("latin-1"))
    out.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        out.extend(f"{offset:010d} 00000 n \n".encode("latin-1"))
    out.extend(
        (
            "trailer\n"
            f"<< /Size {len(objects)+1} /Root {catalog_id} 0 R >>\n"
            "startxref\n"
            f"{xref_start}\n"
            "%%EOF\n"
        ).encode("latin-1")
    )
    output_path.write_bytes(out)


if __name__ == "__main__":
    _validate_quality_gate(QUALITY_GATE)
    missing = [str(src) for _, src in INPUT_FILES if not src.exists()]
    if missing:
        raise FileNotFoundError(
            "Missing required source file(s).\nExpected paths:\n- "
            + "\n- ".join(missing)
            + "\nPlease ensure all markdown files are present in the repository root before building the PDF."
        )
    build_pdf(OUTPUT)
    print(f"Built PDF: {OUTPUT}")
