from PIL import Image, ImageChops
import numpy as np

orig = Image.open('assets/images/canva_invitation_card_page1_opt.png')
clean = Image.open('scratch/clean_canva_p1.png')

# Resize clean if needed to match orig (1241, 1755)
if clean.size != orig.size:
    clean = clean.resize(orig.size, Image.Resampling.LANCZOS)
    clean.save('scratch/clean_canva_p1.png')

diff = ImageChops.difference(orig, clean)
diff_arr = np.array(diff)
print("Max diff per channel:", diff_arr.max(axis=(0,1)))

# Let's check region 1: Celebrate area (x=300..900, y=350..650)
r1 = diff_arr[350:650, 300:900]
print("Region 1 (white Jennina watermark) diff max:", r1.max(), "mean:", r1.mean())

# Region 2: Turns 18 area (x=600..950, y=650..950)
r2 = diff_arr[650:950, 600:950]
print("Region 2 (gold 18 watermark) diff max:", r2.max(), "mean:", r2.mean())

# Region 3: Date 5 area (x=650..900, y=1000..1250)
r3 = diff_arr[1000:1250, 650:900]
print("Region 3 (gold 5 watermark) diff max:", r3.max(), "mean:", r3.mean())

# Region 4: Jennina main text area (x=350..700, y=600..750) - should NOT be wiped out!
orig_jennina = np.array(orig)[600:750, 350:700]
clean_jennina = np.array(clean)[600:750, 350:700]
print("Original Jennina main text min pixel (darkest):", orig_jennina.min(axis=(0,1)))
print("Clean Jennina main text min pixel (darkest):", clean_jennina.min(axis=(0,1)))
