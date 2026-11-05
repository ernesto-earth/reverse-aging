from io import BytesIO

from PIL import Image
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A5
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


OUTPUT = "/Users/ernesto/Documents/Codex/2026-09-14/f/outputs/morgenroutine-a5.pdf"
ART = "/Users/ernesto/Documents/Codex/2026-09-14/f/work/pdfs/sketchnote-routine-v2.png"


def register_fonts():
    pdfmetrics.registerFont(TTFont("RoutineSans", "/System/Library/Fonts/Supplemental/Arial.ttf"))
    pdfmetrics.registerFont(TTFont("RoutineSans-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))
    pdfmetrics.registerFont(TTFont("RoutineSketch", "/System/Library/Fonts/Supplemental/Chalkduster.ttf"))


def paragraph(c, text, style, x, y_top, width, max_height=80 * mm):
    p = Paragraph(text, style)
    _, h = p.wrap(width, max_height)
    p.drawOn(c, x, y_top - h)
    return h


def crop_reader(source, box):
    cropped = source.crop(box)
    stream = BytesIO()
    cropped.save(stream, format="PNG")
    stream.seek(0)
    return ImageReader(stream), cropped.width, cropped.height


def draw_crop(c, source, box, x, y, w, h):
    reader, iw, ih = crop_reader(source, box)
    scale = min(w / iw, h / ih)
    dw, dh = iw * scale, ih * scale
    c.drawImage(reader, x + (w - dw) / 2, y + (h - dh) / 2, dw, dh, mask="auto")


def sketch_line(c, x1, y1, x2, y2, color, width=1.8):
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.line(x1, y1, x2, y2)
    c.setLineWidth(max(0.6, width * 0.45))
    c.line(x1 + 1.1, y1 - 1.4, x2 - 0.8, y2 - 1.0)


def main():
    register_fonts()
    page_w, page_h = A5
    c = canvas.Canvas(OUTPUT, pagesize=A5)
    c.setTitle("Fünf Anker für einen guten Tag")
    c.setAuthor("Persönliche Routinen-Sketchnote")

    ink = HexColor("#132D3D")
    paper = HexColor("#FBF7ED")
    teal = HexColor("#08A7A5")
    teal_dark = HexColor("#087F80")
    teal_pale = HexColor("#E4F3F0")
    yellow = HexColor("#F6B719")
    yellow_pale = HexColor("#FFF1BE")
    gray = HexColor("#52636B")
    soft_line = HexColor("#C6D5D5")

    c.setFillColor(paper)
    c.rect(0, 0, page_w, page_h, stroke=0, fill=1)

    margin = 8.5 * mm
    content_w = page_w - 2 * margin
    header_h = 28 * mm

    # Irregular chalkboard header.
    c.setFillColor(ink)
    header_path = c.beginPath()
    header_path.moveTo(0, page_h)
    header_path.lineTo(page_w, page_h)
    header_path.lineTo(page_w, page_h - header_h + 2 * mm)
    header_path.lineTo(page_w * 0.66, page_h - header_h)
    header_path.lineTo(page_w * 0.31, page_h - header_h + 1.4 * mm)
    header_path.lineTo(0, page_h - header_h - 0.6 * mm)
    header_path.close()
    c.drawPath(header_path, stroke=0, fill=1)

    c.setFont("RoutineSketch", 8.2)
    c.setFillColor(yellow)
    c.drawString(margin, page_h - 10.0 * mm, "MEIN MORGEN. MEIN RHYTHMUS.")
    c.setFont("RoutineSketch", 18.2)
    c.setFillColor(white)
    c.drawString(margin, page_h - 20.2 * mm, "5 ANKER FÜR EINEN GUTEN TAG")
    sketch_line(c, margin, page_h - 23.6 * mm, margin + 87 * mm, page_h - 23.6 * mm, yellow, 2.4)
    c.setFont("RoutineSans", 7.0)
    c.setFillColor(HexColor("#D9E8EA"))
    c.drawRightString(page_w - margin, page_h - 25.0 * mm, "einfach  |  klar  |  wiederholbar")

    title_style = ParagraphStyle(
        "step-title",
        fontName="RoutineSans-Bold",
        fontSize=9.25,
        leading=10.6,
        textColor=ink,
        alignment=TA_LEFT,
    )
    body_style = ParagraphStyle(
        "step-body",
        fontName="RoutineSans",
        fontSize=7.35,
        leading=8.65,
        textColor=gray,
        alignment=TA_LEFT,
    )
    footer_head = ParagraphStyle(
        "footer-head",
        fontName="RoutineSans-Bold",
        fontSize=7.1,
        leading=8.2,
        textColor=ink,
        alignment=TA_LEFT,
    )
    footer_body = ParagraphStyle(
        "footer-body",
        fontName="RoutineSans",
        fontSize=6.35,
        leading=7.55,
        textColor=gray,
        alignment=TA_LEFT,
    )

    source = Image.open(ART).convert("RGB")
    crops = [
        (135, 0, 865, 275),
        (80, 270, 950, 615),
        (90, 590, 940, 925),
        (130, 930, 915, 1235),
        (95, 1235, 955, 1536),
    ]

    steps = [
        (
            "WASSER - SOFORT",
            "Ein großes Glas direkt nach dem Aufwachen. Kaffee bewusst später - erst trinken, kurz ankommen, dann genießen. <b>Tipp:</b> Glas abends sichtbar bereitstellen.",
        ),
        (
            "TAGESLICHT + MORGENSPAZIERGANG",
            "Mindestens 30 Minuten draußen. Zügig, aber noch gesprächsfähig. Wenn 30 Minuten zu viel sind: kürzer starten und regelmäßig steigern.",
        ),
        (
            "TRAINING - 15 BIS 30 MINUTEN",
            "Theraband, Kniebeugen, Liegestütze (Wand/Tisch/Boden) und Plank rotieren. 2-3 kräftige Einheiten pro Woche; sonst leicht oder mobil. <b>Technik vor Tempo.</b>",
        ),
        (
            "PROTEIN - ÜBER DEN TAG",
            "Auf 2 Mahlzeiten verteilen: Fisch, Fleisch, Eier, Joghurt, Hülsenfrüchte; Nüsse ergänzend. Menge an Bedarf anpassen.",
        ),
        (
            "AKTIV DENKEN - LAUFEND",
            "Täglich fordern: lesen + notieren, lernen, schreiben, musizieren, planen oder diskutieren. Schwierigkeit leicht steigern - nicht nur passiv konsumieren.",
        ),
    ]

    rows_top = page_h - header_h - 4.3 * mm
    row_h = 26.6 * mm
    gap = 1.7 * mm
    number_x = margin + 6.0 * mm
    text_x = margin + 15.5 * mm
    image_w = 42 * mm
    image_x = page_w - margin - image_w
    text_w = image_x - text_x - 2.2 * mm

    # Hand-drawn vertical route through the five anchors.
    sketch_line(
        c,
        number_x,
        rows_top - 10 * mm,
        number_x,
        rows_top - 4 * (row_h + gap) - 17 * mm,
        soft_line,
        1.4,
    )

    for i, ((heading, body), crop) in enumerate(zip(steps, crops)):
        y = rows_top - (i + 1) * row_h - i * gap
        fill = teal_pale if i % 2 == 0 else yellow_pale
        c.setFillColor(fill)
        c.roundRect(text_x - 2.2 * mm, y + 2.2 * mm, text_w + 3.0 * mm, row_h - 4.4 * mm, 3.2 * mm, stroke=0, fill=1)

        c.setFillColor(yellow if i in (0, 3) else teal)
        c.setStrokeColor(ink)
        c.setLineWidth(1.3)
        c.circle(number_x, y + row_h / 2, 4.7 * mm, stroke=1, fill=1)
        c.setFont("RoutineSketch", 10.2)
        c.setFillColor(ink if i in (0, 3) else white)
        c.drawCentredString(number_x, y + row_h / 2 - 3.6, str(i + 1))

        head_h = paragraph(c, heading, title_style, text_x, y + row_h - 4.0 * mm, text_w)
        paragraph(c, body, body_style, text_x, y + row_h - 4.0 * mm - head_h - 0.8 * mm, text_w)

        draw_crop(c, source, crop, image_x, y + 1.2 * mm, image_w, row_h - 2.4 * mm)
        sketch_line(c, image_x + 1 * mm, y + 2.0 * mm, image_x + 39 * mm, y + 2.0 * mm, yellow if i % 2 else teal, 1.0)

    # Closing layer: consistency and recovery.
    footer_y = 8.3 * mm
    footer_h = 23.0 * mm
    c.setFillColor(white)
    c.setStrokeColor(soft_line)
    c.setLineWidth(0.8)
    c.roundRect(margin, footer_y, content_w, footer_h, 3.4 * mm, stroke=1, fill=1)
    split_x = margin + content_w / 2
    c.line(split_x, footer_y + 4 * mm, split_x, footer_y + footer_h - 4 * mm)

    left_x = margin + 4 * mm
    right_x = split_x + 4 * mm
    col_w = content_w / 2 - 8 * mm
    paragraph(c, "KONSTANZ VOR PERFEKTION", footer_head, left_x, footer_y + footer_h - 4 * mm, col_w)
    paragraph(
        c,
        "An schwachen Tagen verkleinern: 1 Glas, 10 Minuten draußen, 1 Übung, 1 Proteinquelle, 1 Denkaufgabe. Wiederholung schlägt den perfekten Plan.",
        footer_body,
        left_x,
        footer_y + footer_h - 12.3 * mm,
        col_w,
    )
    paragraph(c, "SCHLAF + REGENERATION", footer_head, right_x, footer_y + footer_h - 4 * mm, col_w)
    paragraph(
        c,
        "Möglichst fester Schlafrhythmus. Harte Krafteinheiten nicht täglich - Erholung ist ein fester Teil der Routine.",
        footer_body,
        right_x,
        footer_y + footer_h - 12.3 * mm,
        col_w,
    )

    c.setFillColor(teal_dark)
    c.circle(page_w - 7.2 * mm, 6.0 * mm, 1.15 * mm, stroke=0, fill=1)
    c.setFillColor(yellow)
    c.circle(page_w - 10.6 * mm, 6.0 * mm, 1.15 * mm, stroke=0, fill=1)
    c.setFont("RoutineSans", 5.3)
    c.setFillColor(HexColor("#718087"))
    c.drawString(margin, 4.6 * mm, "Persönliche Routinen-Sketchnote | A5")

    c.showPage()
    c.save()


if __name__ == "__main__":
    main()
