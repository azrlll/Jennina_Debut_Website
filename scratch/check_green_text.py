from PIL import Image
import numpy as np

im = Image.open('scratch/test_crop_center.png')
arr = np.array(im)

# Check green pixels (where G is noticeably higher than R and B, or dark green)
# The green script text has color around (59, 82, 53) in hex #3B5235
# Let's count pixels close to #3B5235
r = arr[:, :, 0]
g = arr[:, :, 1]
b = arr[:, :, 2]

# Condition for green text: g > r and g > b, and g < 120 (dark green)
green_mask = (g > r + 5) & (g > b + 10) & (g < 140) & (g > 30)
print("Green text pixels count in test_crop_center:", np.sum(green_mask))

orig = Image.open('assets/images/canva_invitation_card_page1_opt.png')
w, h = orig.size
orig_crop = orig.crop((int(w * 0.2), int(h * 0.2), int(w * 0.8), int(h * 0.8)))
orig_arr = np.array(orig_crop)
or_r = orig_arr[:, :, 0]
or_g = orig_arr[:, :, 1]
or_b = orig_arr[:, :, 2]
orig_green_mask = (or_g > or_r + 5) & (or_g > or_b + 10) & (or_g < 140) & (or_g > 30)
print("Green text pixels count in original:", np.sum(orig_green_mask))
