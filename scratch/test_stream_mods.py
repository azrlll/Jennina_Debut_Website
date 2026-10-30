import fitz

doc = fitz.open(r'reference\DEBUT INVITATION.pdf')
# Read stream 23
stream_23 = doc.xref_stream(23).decode('latin1')

# Let's see what calls /X16 Do and /X19 Do
lines = stream_23.split('\n')
print(f"Total lines in stream 23: {len(lines)}")
for i, l in enumerate(lines):
    if any(k in l for k in ['X16', 'X19', 'X22', 'X26', 'X28', 'X30', 'Do']):
        print(f"Line {i}: {l}")
