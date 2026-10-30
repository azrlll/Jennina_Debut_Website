import fitz

pdf_path = r'C:\Users\KEVIN CHRISTOPHER\.gemini\antigravity\brain\b4e57cab-2651-486a-a820-1d9d96787cfc\.user_uploaded\media_1793351379928_ebcb633b.pdf'
doc = fitz.open(pdf_path)

for xref in range(1, doc.xref_length()):
    try:
        s = doc.xref_stream(xref)
        if s:
            text = s.decode('latin1', errors='ignore')
            # Look for 2283.3508 cm or F29 25.33
            if '2283.35' in text or '2411.1' in text:
                print(f"Xref {xref} contains date stream!")
                lines = text.split('\n')
                for i, l in enumerate(lines):
                    if any(k in l for k in ['2283', '2411', 'Tj', 'TJ']):
                        print(f"  {i}: {l}")
    except:
        pass
