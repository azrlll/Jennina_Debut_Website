import fitz
import json

pdf_path = r'C:\Users\KEVIN CHRISTOPHER\.gemini\antigravity\brain\b4e57cab-2651-486a-a820-1d9d96787cfc\.user_uploaded\media_1793351379928_ebcb633b.pdf'
doc = fitz.open(pdf_path)
page = doc[0]

data = json.loads(page.get_text('rawjson'))
for b_idx, block in enumerate(data.get('blocks', [])):
    for l_idx, line in enumerate(block.get('lines', [])):
        for s_idx, span in enumerate(line.get('spans', [])):
            chars = ''.join([c.get('c', '') for c in span.get('chars', [])])
            if any(k in chars for k in ['2026', '2027', 'FEB', '5', 'FRIDAY', 'AT 3 PM']):
                print(f"chars={repr(chars):15} | font={span.get('font'):20} | size={span.get('size'):.1f} | color=#{span.get('color'):06x} | bbox={[round(x,1) for x in span.get('bbox')]}")
