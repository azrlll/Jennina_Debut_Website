from PIL import Image, ImageDraw, ImageFont
import numpy as np

for sz in range(35, 45):
    font = ImageFont.truetype('assets/fonts/font_4.woff2', sz)
    im = Image.new('L', (100, 100), 255)
    draw = ImageDraw.Draw(im)
    draw.text((10, 10), "7", font=font, fill=0)
    arr = np.array(im)
    y_idx, x_idx = np.where(arr < 128)
    h = y_idx.max() - y_idx.min() + 1
    w = x_idx.max() - x_idx.min() + 1
    print(f"Font size {sz}: '7' width={w}, height={h}")
