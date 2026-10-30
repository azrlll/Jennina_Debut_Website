from PIL import Image

up = Image.open(r'C:\Users\KEVIN CHRISTOPHER\.gemini\antigravity\brain\b4e57cab-2651-486a-a820-1d9d96787cfc\.user_uploaded\media_1793349268364_655d165f.png')
print("Uploaded size:", up.size)
up.save('scratch/user_uploaded_inspect.png')
