from PIL import Image

# Let's crop around Jennina (y=600..900, x=350..900) in test_removed_xobjs
test = Image.open('scratch/test_removed_xobjs.png')
jennina_crop = test.crop((350, 600, 900, 900))
jennina_crop.save('scratch/test_jennina_area.png')

turns18_crop = test.crop((350, 850, 900, 1150))
turns18_crop.save('scratch/test_turns18_area.png')

date_crop = test.crop((350, 1050, 900, 1250))
date_crop.save('scratch/test_date_area.png')

print("Crops saved!")
