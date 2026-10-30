import fitz

doc = fitz.open(r'reference\DEBUT INVITATION.pdf')
page = doc[0]

for img_info in page.get_images():
    xref = img_info[0]
    rects = page.get_image_rects(xref)
    print(f"Image xref {xref}: dims={img_info[2]}x{img_info[3]}, rects={rects}")
