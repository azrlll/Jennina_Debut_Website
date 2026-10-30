import fitz

doc = fitz.open(r'reference\DEBUT INVITATION.pdf')
# Find F27
for xref in range(1, doc.xref_length()):
    try:
        obj = doc.xref_object(xref)
        if '/BaseFont' in obj and ('F27' in obj or 'Canva' in obj or 'Cinzel' in obj or 'Great' in obj):
            print(f"Xref {xref}:\n{obj[:300]}")
    except:
        pass
