from PIL import Image
import os

for f in sorted(os.listdir('scratch/p1_extracted')):
    p = os.path.join('scratch/p1_extracted', f)
    im = Image.open(p)
    print(f"{f}: size={im.size}, mode={im.mode}")
