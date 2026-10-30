import fitz
from PIL import Image

pdf_path = r'C:\Users\KEVIN CHRISTOPHER\.gemini\antigravity\brain\b4e57cab-2651-486a-a820-1d9d96787cfc\.user_uploaded\media_1793351379928_ebcb633b.pdf'
doc = fitz.open(pdf_path)
page = doc[0]

# Search for "2026" text rect
rects = page.search_for("2026")
print("Search for '2026' rects in PDF points:", rects)

im = Image.open('scratch/raw_pdf_render_1241.png')
w, h = im.size
scale_x = w / page.rect.width
scale_y = h / page.rect.height

for i, r in enumerate(rects):
    px_box = (
        int(r.x0 * scale_x) - 40,
        int(r.y0 * scale_y) - 20,
        int(r.x1 * scale_x) + 40,
        int(r.y1 * scale_y) + 20
    )
    print(f"Crop box for '2026': {px_box}")
    crop = im.crop(px_box)
    crop.save(f'scratch/year_2026_crop_{i}.png')
    print(f"Saved scratch/year_2026_crop_{i}.png (size: {crop.size})")
