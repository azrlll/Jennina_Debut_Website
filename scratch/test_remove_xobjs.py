import fitz

doc = fitz.open(r'reference\DEBUT INVITATION.pdf')
stream_23 = doc.xref_stream(23).decode('latin1')

# Replace /X16 Do with % /X16 Do (or spaces)
# Replace /X19 Do with % /X19 Do
# Replace /X28 Do with % /X28 Do
mod_stream = stream_23
mod_stream = mod_stream.replace('/X16 Do', '% /X16 Do')
mod_stream = mod_stream.replace('/X19 Do', '% /X19 Do')
mod_stream = mod_stream.replace('/X28 Do', '% /X28 Do')

# Update stream 23 in doc
doc.update_stream(23, mod_stream.encode('latin1'))

# Render page 0
page = doc[0]
pix = page.get_pixmap(dpi=150)
pix.save('scratch/test_removed_xobjs.png')
print("Rendered scratch/test_removed_xobjs.png!")
