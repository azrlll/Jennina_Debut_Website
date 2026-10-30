from PIL import Image

# Check if img_405, 409, 416 have transparency or what they contain
for name in ['img_405.png', 'img_409.png', 'img_416.png', 'img_401.png', 'img_227.png']:
    im = Image.open('scratch/p1_extracted/' + name)
    print(name, 'size:', im.size, 'mode:', im.mode)
    # Check alpha or sample some pixels
    # Save a thumbnail or smaller version
    im.thumbnail((300, 300))
    im.save(f'scratch/thumb_{name}')
print("Thumbnails saved!")
