import fitz

doc = fitz.open(r'reference\DEBUT INVITATION.pdf')
page = doc[0]

# Inspect resources
res = page.get_xobjects()
print("XObjects on Page 1:")
for x in res:
    print(x)
