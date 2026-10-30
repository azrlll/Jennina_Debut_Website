import fitz
from PIL import Image

pdf_path = r'C:\Users\KEVIN CHRISTOPHER\.gemini\antigravity\brain\b4e57cab-2651-486a-a820-1d9d96787cfc\.user_uploaded\media_1793351379928_ebcb633b.pdf'
doc = fitz.open(pdf_path)
page = doc[0]

# Standard render at 1241x1755 (scale = 1241 / 595.5 = 2.083963056)
zoom = 1241 / 595.5
mat = fitz.Matrix(zoom, zoom)
pix = page.get_pixmap(matrix=mat, alpha=False)
pix.save('scratch/raw_pdf_render_1241.png')
print(f"Rendered raw PDF at {pix.width}x{pix.height}")
