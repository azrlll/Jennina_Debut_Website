from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Load exact_2026
im = Image.open('scratch/exact_2026.png').convert('RGB')
arr = np.array(im)

# Clean the area of '6' (x=73..98, y=8..40)
# We can use the parchment texture from x=60..72 or average texture
clean_patch = im.copy()
# Sample parchment texture from right around it (e.g. y=0..8 or x=70..75)
# In fact, let's clone parchment texture from x=45..68, y=10..38 (between 0 and 2) or nearby
bg_sample = arr[10:39, 45:68].copy()
arr[10:39, 74:97] = bg_sample

# Create image from cleaned array
clean_im = Image.fromarray(arr)

# Render '7'
font = ImageFont.truetype('assets/fonts/font_4.woff2', 40)
# Let's render '7' onto an RGBA mask to get exact antialiasing
mask = Image.new('L', (40, 40), 0)
draw_mask = ImageDraw.Draw(mask)
draw_mask.text((0, 0), "7", font=font, fill=255)

# Find bounding box of rendered 7
mask_arr = np.array(mask)
my, mx = np.where(mask_arr > 0)
print(f"Rendered 7 box in mask: x=[{mx.min()}, {mx.max()}], y=[{my.min()}, {my.max()}]")
# Crop mask to tightly fit the glyph
tight_mask = mask.crop((mx.min(), my.min(), mx.max() + 1, my.max() + 1))
print(f"Tight 7 size: {tight_mask.size}")

# Top of original 2026 was at y=10, bottom was at y=38
# Position tight_mask at x=76, y=10
glyph_color = Image.new('RGB', tight_mask.size, (59, 82, 53))
clean_im.paste(glyph_color, (76, 10), tight_mask)
clean_im.save('scratch/exact_2027_test.png')
print("Saved scratch/exact_2027_test.png!")
