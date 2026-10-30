from PIL import Image

im405 = Image.open('scratch/p1_extracted/img_405.png')
im409 = Image.open('scratch/p1_extracted/img_409.png')

print("im405 size:", im405.size)
print("im409 size:", im409.size)

# Save cropped or full so we can see what they are
im405.save('scratch/im405.png')
im409.save('scratch/im409.png')
