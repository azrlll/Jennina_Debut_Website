from PIL import Image

up = Image.open(r'C:\Users\KEVIN CHRISTOPHER\.gemini\antigravity\brain\b4e57cab-2651-486a-a820-1d9d96787cfc\.user_uploaded\media_1793349268364_655d165f.png')

# Let's crop:
# 1. The top part with "CELEBRATE A NEW CHAPTER WITH US AS" and the white "Jennina" behind it
up_top = up.crop((int(up.width * 0.1), int(up.height * 0.1), int(up.width * 0.9), int(up.height * 0.4)))
up_top.save('scratch/up_white_jennina.png')

# 2. The middle part with "Jennina", "TURNS 18" and the gold 18 behind it
up_mid = up.crop((int(up.width * 0.1), int(up.height * 0.3), int(up.width * 0.9), int(up.height * 0.7)))
up_mid.save('scratch/up_gold_18.png')

# 3. The bottom part with "FEB 5 2026" and the gold 5 behind it
up_bot = up.crop((int(up.width * 0.1), int(up.height * 0.6), int(up.width * 0.9), int(up.height * 0.95)))
up_bot.save('scratch/up_gold_5.png')

print("Uploaded sub-crops saved!")
