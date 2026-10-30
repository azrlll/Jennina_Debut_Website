import fitz

doc = fitz.open(r'reference\DEBUT INVITATION.pdf')
# Find which xref contains Block 4 and Block 6
for xref in [23, 226, 228, 229, 230, 231, 232, 233]:
    try:
        s = doc.xref_stream(xref).decode('latin1', errors='ignore')
        if 'F13' in s:
            print(f"Xref {xref} uses font F13!")
    except:
        pass
