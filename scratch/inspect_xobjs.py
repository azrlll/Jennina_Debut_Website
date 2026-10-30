import fitz

doc = fitz.open(r'reference\DEBUT INVITATION.pdf')

for name, xref in [('X16', 228), ('X19', 229), ('X22', 230), ('X26', 231), ('X28', 232), ('X30', 233)]:
    stream = doc.xref_stream(xref).decode('latin1', errors='ignore')
    print(f"=== {name} (xref {xref}) ===")
    print(stream)
