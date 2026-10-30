from PIL import Image

im = Image.open('scratch/clean_canva_p1.png')

# 1. Top area with Celebrate + Jennina
c1 = im.crop((200, 350, 1040, 850))
c1.save('scratch/clean_crop_jennina.png')

# 2. Mid area with Turns 18
c2 = im.crop((200, 750, 1040, 1150))
c2.save('scratch/clean_crop_18.png')

# 3. Date area with Feb 5
c3 = im.crop((200, 1050, 1040, 1400))
c3.save('scratch/clean_crop_5.png')

print("All 3 clean crops saved successfully!")
