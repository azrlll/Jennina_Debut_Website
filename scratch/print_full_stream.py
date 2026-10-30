import fitz

doc = fitz.open(r'reference\DEBUT INVITATION.pdf')
stream_23 = doc.xref_stream(23).decode('latin1', errors='ignore')
print(stream_23)
