from PIL import Image
import numpy as np

im = Image.open('assets/images/canva_invitation_card_page1_opt.png')
w, h = im.size

# Let's inspect:
# 1. White text Jennina:
# In the area around x=300..900, y=300..600
# The parchment background has color ~ (240, 238, 230)
# White text has color ~ (255, 255, 255)
# 2. Gold 18:
# In the area around x=650..850, y=700..950
# Gold color has color with higher red/yellow: (220, 195, 140) or similar
# 3. Gold 5:
# In the area around x=700..850, y=1050..1200
# Gold color ~ (220, 195, 140)

print("Let's analyze pixels in those 3 areas:")
