import fitz

pdf_path = r'C:\Users\KEVIN CHRISTOPHER\.gemini\antigravity\brain\b4e57cab-2651-486a-a820-1d9d96787cfc\.user_uploaded\media_1793351379928_ebcb633b.pdf'
doc = fitz.open(pdf_path)
s = doc.xref_stream(18)
lines = s.split(b'\n')
print(f"Total lines: {len(lines)}")
for i in range(240, min(len(lines), 265)):
    print(f"Line {i}: {lines[i]}")
