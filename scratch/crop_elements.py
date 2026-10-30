from PIL import Image

im = Image.open('assets/images/canva_invitation_card_page1_opt.png')
w, h = im.size
print(f"Hero image size: {w}x{h}")

# In DEBUT INVITATION.pdf, the page rect is 595.5 x 842.25.
# The image is 1241 x 1755 (scale factor = 1241 / 595.5 = 2.08396)
scale_x = w / 595.5
scale_y = h / 842.25

# 1. White text Jennina: around y = 200..450, x = 150..450 in PDF points
# In pixels:
crop1 = im.crop((int(150 * scale_x), int(180 * scale_y), int(450 * scale_x), int(420 * scale_y)))
crop1.save('scratch/crop_white_jennina.png')

# 2. Gold 18: around y = 350..550, x = 250..450 in PDF points
crop2 = im.crop((int(250 * scale_x), int(350 * scale_y), int(450 * scale_x), int(550 * scale_y)))
crop2.save('scratch/crop_gold_18.png')

# 3. Gold 5: around y = 480..580, x = 280..420 in PDF points
crop3 = im.crop((int(280 * scale_x), int(480 * scale_y), int(420 * scale_x), int(580 * scale_y)))
crop3.save('scratch/crop_gold_5.png')

print("Crops saved successfully!")
