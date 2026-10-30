import fitz

doc = fitz.open(r'reference\DEBUT INVITATION.pdf')
page = doc[0]

# Let's inspect drawings / vectors on page 1
drawings = page.get_drawings()
print("Number of drawing paths on page 1:", len(drawings))
for i, d in enumerate(drawings[:10]):
    print(f"Path {i}: color={d.get('color')}, fill={d.get('fill')}, rect={d.get('rect')}")
