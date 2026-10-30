import fitz

doc = fitz.open(r'reference\DEBUT INVITATION.pdf')
page = doc[0]

# Inspect the command sequence
commands = []
for op in page.get_cdrawings():
    commands.append(op)
print(f"Total cdrawings: {len(commands)}")

# Let's inspect the xref stream of the page
contents_xref = page.get_contents()
print("Contents xref:", contents_xref)
for xref in contents_xref:
    stream = doc.xref_stream(xref).decode('latin1', errors='ignore')
    print(f"Stream {xref} length: {len(stream)}")
    # Find text operators (Tj, TJ) in stream
    import re
    text_ops = re.findall(r'(\([^\)]*\)|\[[^\]]*\])\s*(Tj|TJ)', stream)
    print(f"Found {len(text_ops)} text operations:")
    for op in text_ops[:20]:
        print(" ", op)
