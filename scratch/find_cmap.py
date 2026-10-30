import fitz

pdf_path = r'C:\Users\KEVIN CHRISTOPHER\.gemini\antigravity\brain\b4e57cab-2651-486a-a820-1d9d96787cfc\.user_uploaded\media_1793351379928_ebcb633b.pdf'
doc = fitz.open(pdf_path)

# Find ToUnicode stream for F29
for xref in range(1, doc.xref_length()):
    try:
        s = doc.xref_stream(xref).decode('latin1', errors='ignore')
        if 'beginbfrange' in s or 'beginbfchar' in s:
            if '2026' in s or '0015' in s or '0019' in s:
                print(f"Xref {xref} is the CMap for F29!")
                print(s)
    except:
        pass
