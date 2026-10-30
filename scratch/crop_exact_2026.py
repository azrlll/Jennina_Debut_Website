from PIL import Image
import numpy as np

# In PDF coordinates:
# rect for '2026' was: Rect(269.24249267578125, 547.5574340820312, 316.656494140625, 573.0807495117188)
# At 1241 x 1756, scale_x = 1241 / 595.5 = 2.083963, scale_y = 1756 / 842.25 = 2.0848916
# Let's crop EXACTLY this box:
im = Image.open('scratch/raw_pdf_render_1241.png')
sx = 1241 / 595.5
sy = 1756 / 842.25
x0 = int(269.24 * sx)
y0 = int(547.55 * sy)
x1 = int(316.66 * sx)
y1 = int(573.08 * sy)
print(f"Exact '2026' pixel coordinates in 1241x1756 image: ({x0}, {y0}, {x1}, {y1})")

crop_exact = im.crop((x0, y0, x1, y1))
crop_exact.save('scratch/exact_2026.png')
print(f"exact_2026.png saved with size: {crop_exact.size}")
