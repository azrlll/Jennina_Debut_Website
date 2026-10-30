from PIL import Image
import numpy as np

for name in ['img_405.png', 'img_409.png', 'img_416.png']:
    im = Image.open('scratch/p1_extracted/' + name)
    arr = np.array(im)
    print(f"{name}: shape={arr.shape}, min={arr.min()}, max={arr.max()}, mean={arr.mean():.1f}")
