from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Load Cinzel-Bold
# In PDF: size is 19.0 pt on 595.5pt width
# At 1241px width, scale is 1241 / 595.5 = 2.083963
# So font size in pixels = 19.0 * 2.083963 = 39.595 -> around 39 or 40 px!
font_size = 40
font = ImageFont.truetype('assets/fonts/font_4.woff2', font_size)

# Let's inspect the original crop
im_crop = Image.open('scratch/year_2026_crop_0.png')
w, h = im_crop.size

# Let's test drawing "2027" and compare character widths
canvas = Image.new('RGB', (300, 100), (240, 238, 232))
draw = ImageDraw.Draw(canvas)
draw.text((20, 20), "2027", font=font, fill=(59, 82, 53))
canvas.save('scratch/test_draw_2027.png')

# Let's also check the exact bounding box of "2026" inside im_crop
arr = np.array(im_crop)
dark_mask = (arr[:, :, 0] < 120) & (arr[:, :, 1] < 120) & (arr[:, :, 2] < 120)
y_idx, x_idx = np.where(dark_mask)
print(f"Original 2026 box inside crop: x=[{x_idx.min()}, {x_idx.max()}], y=[{y_idx.min()}, {y_idx.max()}]")
print(f"Original 2026 width={x_idx.max() - x_idx.min() + 1}, height={y_idx.max() - y_idx.min() + 1}")

# What is the box for the '6'? (the last character)
# Usually x > 115 in this crop
x_6 = x_idx[x_idx > (x_idx.min() + 70)]
y_6 = y_idx[x_idx > (x_idx.min() + 70)]
print(f"Original '6' box inside crop: x=[{x_6.min()}, {x_6.max()}], y=[{y_6.min()}, {y_6.max()}]")
print(f"Original '6' width={x_6.max() - x_6.min() + 1}, height={y_6.max() - y_6.min() + 1}")
