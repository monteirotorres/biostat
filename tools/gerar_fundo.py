"""Recria o fundo (marca-d'água UFRJ · IBCCF) dos slides originais.
Gera assets/slides/fundo.png para usar como background dos slides."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import matplotlib

BASE = Path(__file__).parent.parent
FONTDIR = Path(matplotlib.__file__).parent / "mpl-data" / "fonts" / "ttf"
LOGO = BASE / "assets" / "ibccf-logo.png"
OUT = BASE / "assets" / "slides" / "fundo.png"

W, H = 2667, 1500          # 13.333 x 7.5 pol @ 200 dpi
BASECOLOR = (252, 249, 243)   # branco quente, como no original
WM = (214, 205, 187)          # cinza claro da marca-d'água

serif = ImageFont.truetype(str(FONTDIR / "DejaVuSerif.ttf"), 34)

base = Image.new("RGB", (W, H), BASECOLOR)

# camada de marca-d'água (texto repetido na diagonal)
layer = Image.new("RGBA", (W * 2, H * 2), (0, 0, 0, 0))
d = ImageDraw.Draw(layer)
text = "UFRJ   ·   IBCCF   ·   "
step_x, step_y = 360, 120
for j, y in enumerate(range(0, H * 2, step_y)):
    offset = (j % 2) * (step_x // 2)
    for x in range(-step_x, W * 2, step_x):
        d.text((x + offset, y), text, font=serif, fill=(*WM, 90))

# rotaciona e recorta o centro
layer = layer.rotate(28, resample=Image.BICUBIC, center=(W, H))
crop = layer.crop((W // 2, H // 2, W // 2 + W, H // 2 + H))
base.paste(crop, (0, 0), crop)

# logo IBCCF bem suave ao centro
if LOGO.exists():
    logo = Image.open(LOGO).convert("RGBA")
    lw = int(W * 0.42); lh = int(lw * logo.height / logo.width)
    logo = logo.resize((lw, lh), Image.LANCZOS)
    faint = Image.new("RGBA", logo.size, (0, 0, 0, 0))
    for x in range(logo.width):
        for y in range(logo.height):
            r, g, b, a = logo.getpixel((x, y))
            if a > 0:
                faint.putpixel((x, y), (r, g, b, int(a * 0.04)))
    base.paste(faint, ((W - lw) // 2, (H - lh) // 2), faint)

base.save(OUT)
print("Fundo salvo:", OUT.relative_to(BASE), base.size)
