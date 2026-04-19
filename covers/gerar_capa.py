from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
img = Image.new("RGB", (W, H), "#1A1A2E")
draw = ImageDraw.Draw(img)

# Fontes
fonts_dir = "C:/Windows/Fonts/"
def font(name, size):
    for f in [name, "arial.ttf", "calibri.ttf"]:
        try:
            return ImageFont.truetype(fonts_dir + f, size)
        except:
            pass
    return ImageFont.load_default()

f_title   = font("georgiab.ttf", 72)
f_title2  = font("georgiab.ttf", 68)
f_badge   = font("arialbd.ttf",  16)
f_sub     = font("arial.ttf",    22)
f_footer  = font("arialbd.ttf",  18)
f_footer2 = font("arial.ttf",    14)

NAVY   = "#1A1A2E"
GOLD   = "#D4A017"
GOLD2  = "#F0C84A"
WHITE  = "#FFFFFF"
WHITE6 = "#99A0AF"

# ── grid sutil ──────────────────────────────
for y in range(0, H, 105):
    draw.line([(0, y), (W, y)], fill="#FFFFFF10", width=1)
for x in range(0, W, 200):
    draw.line([(x, 0), (x, H)], fill="#FFFFFF10", width=1)

# ── círculo dourado decorativo ───────────────
for r, a in [(300, 18), (210, 14), (130, 10)]:
    draw.ellipse([(950 - r, 315 - r), (950 + r, 315 + r)], fill=None,
                 outline=f"#D4A017{a:02X}", width=2)
# glow sutil
for dr in range(0, 80, 8):
    alpha = max(4, 18 - dr // 4)
    draw.ellipse([(950 - 80 + dr, 315 - 80 + dr), (950 + 80 - dr, 315 + 80 - dr)],
                 fill=f"#D4A017{alpha:02X}")

# ── prédios decorativos (direita) ────────────
def building(x, y, w, h, color, wins_cols=2, wins_rows=8):
    draw.rectangle([(x, y), (x + w, y + h)], fill=color)
    ww, wh, gap = 14, 10, 10
    for row in range(wins_rows):
        for col in range(wins_cols):
            wx = x + gap + col * (ww + gap)
            wy = y + 16 + row * (wh + 8)
            if wy + wh < y + h - 20:
                c = "#D4A0174D" if (row + col) % 3 == 0 else "#1A1A2E"
                draw.rectangle([(wx, wy), (wx + ww, wy + wh)], fill=c, outline="#1A1A2E22", width=1)

building(860, 100, 80, 410, "#D4A01730", wins_cols=2, wins_rows=13)
building(960, 160, 65, 350, "#D4A01720", wins_cols=2, wins_rows=10)
building(1040, 200, 55, 310, "#D4A01718", wins_cols=1, wins_rows=9)
building(1105, 240, 45, 270, "#D4A01714", wins_cols=1, wins_rows=8)
draw.rectangle([(840, 508), (1200, 516)], fill="#D4A01740")

# ── barra lateral dourada ────────────────────
draw.rounded_rectangle([(80, 165), (88, 455)], radius=4, fill=GOLD)

# ── badge "DICAS SEJAAN" ─────────────────────
badge_text = "  DICAS SEJAAN  "
bbox = draw.textbbox((0, 0), badge_text, font=f_badge)
bw = bbox[2] - bbox[0] + 32
draw.rounded_rectangle([(112, 165), (112 + bw, 205)], radius=18, fill=GOLD)
draw.text((112 + 16, 165 + 8), badge_text.strip(), font=f_badge, fill=NAVY)

# ── título ───────────────────────────────────
draw.text((112, 230), "5 Direitos e", font=f_title, fill=WHITE)
draw.text((112, 312), "Deveres do", font=f_title, fill=WHITE)
draw.text((112, 394), "Condômino", font=f_title2, fill=GOLD)

# ── subtítulo ────────────────────────────────
draw.rectangle([(80, 470), (780, 545)], fill="#1A1A2E")
draw.text((112, 476), "O que todo morador precisa saber para uma", font=f_sub, fill=WHITE6)
draw.text((112, 508), "convivência harmoniosa no condomínio.", font=f_sub, fill=WHITE6)

# ── rodapé ───────────────────────────────────
draw.rectangle([(0, 560), (W, 562)], fill="#D4A01766")
draw.rectangle([(0, 562), (W, H)], fill="#D4A01714")
draw.text((112, 585), "SEJAAN", font=f_footer, fill=GOLD)
draw.text((212, 587), "Administradora", font=f_footer2, fill="#FFFFFF55")
draw.text((1088, 587), "sejaanadministradora.com.br", font=f_footer2, fill="#FFFFFF44")

# ── pontos decorativos ───────────────────────
for i, a in enumerate([255, 160, 100, 60, 30]):
    cx = 112 + i * 18
    r = 4
    draw.ellipse([(cx - r, 545 - r), (cx + r, 545 + r)], fill=f"#D4A017{a:02X}")

out = os.path.join(os.path.dirname(__file__), "dicas-direitos-deveres.png")
img.save(out, "PNG", optimize=True)
print(f"Imagem salva: {out}")
