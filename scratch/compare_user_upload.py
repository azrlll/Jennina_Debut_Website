from PIL import Image

uploaded_img = Image.open(r'C:\Users\KEVIN CHRISTOPHER\.gemini\antigravity\brain\b4e57cab-2651-486a-a820-1d9d96787cfc\.user_uploaded\media_1793349268364_655d165f.png')
print("Uploaded image size:", uploaded_img.size, uploaded_img.mode)

current_hero = Image.open('assets/images/canva_invitation_card_page1.webp')
print("Current hero size:", current_hero.size, current_hero.mode)
