import fitz
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

pdf_path = r'C:\Users\KEVIN CHRISTOPHER\.gemini\antigravity\brain\b4e57cab-2651-486a-a820-1d9d96787cfc\.user_uploaded\media_1793351379928_ebcb633b.pdf'
if not os.path.exists(pdf_path):
    pdf_path = r'reference\DEBUT INVITATION.pdf'

doc = fitz.open(pdf_path)
page = doc[0]

# Remove only the ghost watermarks X16 (white cursive Jennina) and X19 (gold 18)
# Keep X28 (the green 5) COMPLETELY UNTOUCHED!
for xref, name, parent, bbox in page.get_xobjects():
    if name in ['X16', 'X19']:
        s = doc.xref_stream(xref).decode('latin1')
        b1 = s.find('BT')
        e1 = s.find('ET') + 2
        if b1 != -1 and e1 != -1:
            doc.update_stream(xref, (s[:b1] + ' ' * (e1 - b1) + s[e1:]).encode('latin1'))
            print(f'Cleaned watermark {name}')

# Render page 0 at high resolution
zoom = 1241 / page.rect.width
pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
full_img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
print(f'Rendered full page: {full_img.size}')

# Coordinates for 2026 patch
sx = full_img.width / page.rect.width
sy = full_img.height / page.rect.height
x0 = int(269.24 * sx)
y0 = int(547.55 * sy)
x1 = int(316.66 * sx)
y1 = int(573.08 * sy)
print(f'Year crop rect: ({x0}, {y0}, {x1}, {y1})')

# Crop year patch
patch = np.array(full_img.crop((x0, y0, x1, y1)))

# Dark mask for digit 6 (x >= 73)
dark_6 = (patch[:, :, 0] < 150) & (patch[:, :, 1] < 150) & (patch[:, :, 2] < 150)
dark_6[:, :73] = False
mask_6 = (dark_6.astype(np.uint8)) * 255

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
mask_dilated = cv2.dilate(mask_6, kernel, iterations=2)

# Seamless inpainting with OpenCV Telea
inpainted = cv2.inpaint(patch, mask_dilated, 3, cv2.INPAINT_TELEA)

# Render official 7 in Cinzel-Bold
im_patch = Image.fromarray(inpainted)
font = ImageFont.truetype('assets/fonts/font_4.woff2', 40)
mask_7 = Image.new('L', (50, 50), 0)
draw_7 = ImageDraw.Draw(mask_7)
draw_7.text((0, 0), '7', font=font, fill=255)

m_arr = np.array(mask_7)
my, mx = np.where(m_arr > 0)
tight_7 = mask_7.crop((mx.min(), my.min(), mx.max() + 1, my.max() + 1))

glyph_color = Image.new('RGB', tight_7.size, (59, 82, 53))
im_patch.paste(glyph_color, (77, 10), tight_7)

# Paste inpainted patch back into full image
full_img.paste(im_patch, (x0, y0))

# Save WebP and PNG
os.makedirs('assets/images', exist_ok=True)
full_img.save('assets/images/jennina-official-invitation.webp', 'WEBP', quality=92)
full_img.save('assets/images/jennina-official-invitation.png', 'PNG')
print('Successfully saved jennina-official-invitation.webp and .png!')
