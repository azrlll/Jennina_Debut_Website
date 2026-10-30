import fitz

pdf_path = r'C:\Users\KEVIN CHRISTOPHER\.gemini\antigravity\brain\b4e57cab-2651-486a-a820-1d9d96787cfc\.user_uploaded\media_1793351379928_ebcb633b.pdf'
doc = fitz.open(pdf_path)

for xref in range(1, doc.xref_length()):
    try:
        s = doc.xref_stream(xref).decode('latin1', errors='ignore')
        if '0037' in s:
            print(f"Xref {xref} has Unicode 0037 (digit 7)!")
            lines = s.split('\n')
            for l in lines:
                if '0037' in l:
                    print("  ", l)
    except:
        pass
