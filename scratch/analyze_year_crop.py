from PIL import Image
import numpy as np

im = Image.open('scratch/year_2026_crop_0.png')
arr = np.array(im)

# Parchment background pixels (bright, light cream)
# Text pixels (dark forest green)
dark_pixels = arr[(arr[:, :, 0] < 120) & (arr[:, :, 1] < 120) & (arr[:, :, 2] < 120)]
print("Dark pixels count in year crop:", len(dark_pixels))
print("Mean dark color:", dark_pixels.mean(axis=0))
print("Min dark color (darkest core):", dark_pixels.min(axis=0))

parchment_pixels = arr[(arr[:, :, 0] > 220) & (arr[:, :, 1] > 215) & (arr[:, :, 2] > 200)]
print("Mean parchment color:", parchment_pixels.mean(axis=0))
