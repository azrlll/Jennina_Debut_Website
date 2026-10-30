from PIL import Image

im = Image.open('scratch/test_removed_xobjs.png')
print("Size of test_removed_xobjs:", im.size)

# Crop the center oval
w, h = im.size
crop = im.crop((int(w * 0.2), int(h * 0.2), int(w * 0.8), int(h * 0.8)))
crop.save('scratch/test_crop_center.png')
print("Saved scratch/test_crop_center.png!")
