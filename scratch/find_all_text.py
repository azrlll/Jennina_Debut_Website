import fitz

doc = fitz.open(r'reference\DEBUT INVITATION.pdf')

for xref in range(1, doc.xref_length()):
    try:
        stream = doc.xref_stream(xref)
        if stream:
            text = stream.decode('latin1', errors='ignore')
            if 'Jennina' in text or 'GreatVibes' in text or 'CanvaSans' in text:
                print(f"Xref {xref} has Canva text!")
    except:
        pass
