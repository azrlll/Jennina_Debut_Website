from PIL import Image, ImageChops
import numpy as np

orig = Image.open('assets/images/canva_invitation_card_page1_opt.png').convert('RGB')
test = Image.open('scratch/test_removed_xobjs.png').convert('RGB')

diff = ImageChops.difference(orig, test)
diff.save('scratch/diff.png')
print("Diff saved, max diff per channel:", np.array(diff).max(axis=(0,1)))

# Where are the differences located?
diff_arr = np.array(diff)
diff_mask = diff_arr.sum(axis=2) > 20
y_indices, x_indices = np.where(diff_mask)
if len(y_indices) > 0:
    print(f"Diff bounding box: x=[{x_indices.min()}, {x_indices.max()}], y=[{y_indices.min()}, {y_indices.max()}]")
