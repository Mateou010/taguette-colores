"""Generate synthetic input for the optional PDF integration test."""
import argparse
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(args.output), pagesize=A4)
    pdf.setFont('Helvetica', 18)
    pdf.drawString(50, 785, 'Prueba de colores por codigo')
    pdf.setFont('Helvetica', 12)
    lines = [
        'Amarillo identifica una idea.', 'Verde identifica una voz.',
        'Azul identifica el contexto.', 'Violeta identifica una pregunta.',
        'Rosa identifica un hallazgo.', 'Naranja identifica una oportunidad.',
        'Este fragmento tiene dos codigos superpuestos.',
    ]
    for i, text in enumerate(lines):
        pdf.drawString(50, 735 - i * 36, text)
    pdf.save()


if __name__ == '__main__':
    main()
