import fitz

doc = fitz.open(r'reference\DEBUT INVITATION.pdf')
page = doc[0]
print("Images on Page 1:")
for img in page.get_images():
    print(" ", img)

print("\nWords on Page 1:")
for w in page.get_text("words"):
    print(" ", w)
