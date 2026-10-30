import fitz
import os

doc = fitz.open(r'reference\DEBUT INVITATION.pdf')
page = doc[0]

os.makedirs('scratch/p1_extracted', exist_ok=True)
for img_info in page.get_images():
    xref = img_info[0]
    base_img = doc.extract_image(xref)
    ext = base_img["ext"]
    fname = f"scratch/p1_extracted/img_{xref}.{ext}"
    with open(fname, "wb") as f:
        f.write(base_img["image"])
    print(f"Saved {fname}: {base_img['width']}x{base_img['height']}")
