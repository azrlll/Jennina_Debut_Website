from PIL import Image
import numpy as np

im = Image.open('scratch/exact_2026.png')
arr = np.array(im)

# Find dark pixels
dark_mask = (arr[:, :, 0] < 120) & (arr[:, :, 1] < 120) & (arr[:, :, 2] < 120)
y_idx, x_idx = np.where(dark_mask)
print(f"Dark pixels in exact_2026: x=[{x_idx.min()}, {x_idx.max()}], y=[{y_idx.min()}, {y_idx.max()}]")
print(f"Total width={x_idx.max() - x_idx.min() + 1}, height={y_idx.max() - y_idx.min() + 1}")

# Character breakdown:
# 2: x ~ 0..25
# 0: x ~ 25..50
# 2: x ~ 50..75
# 6: x ~ 75..100
m_6 = dark_mask.copy()
m_6[:, :72] = False
y6, x6 = np.where(m_6)
print(f"Digit '6' only: x=[{x6.min()}, {x6.max()}], y=[{y6.min()}, {y6.max()}]")
print(f"Digit '6' width={x6.max() - x6.min() + 1}, height={y6.max() - y6.min() + 1}")
