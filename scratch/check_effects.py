from PIL import Image
import numpy as np

im405 = Image.open('scratch/p1_extracted/img_405.png')
im409 = Image.open('scratch/p1_extracted/img_409.png')

# In Canva, text effects like blur / shadow / glow are exported as raster images!
print("img_405 rect: [97.9, 226.5, 481.2, 469.9]")
print("img_409 rect: [194.2, 238.1, 540.9, 643.2]")
