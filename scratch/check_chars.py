import fitz

doc = fitz.open(r'reference\DEBUT INVITATION.pdf')
page = doc[0]

for block in page.get_text("rawjson")["blocks"] if isinstance(page.get_text("rawjson"), dict) else []:
    pass

import json
data = json.loads(page.get_text("rawjson"))
for b_idx, block in enumerate(data.get("blocks", [])):
    for l_idx, line in enumerate(block.get("lines", [])):
        for s_idx, span in enumerate(line.get("spans", [])):
            chars = "".join([c.get("c", "") for c in span.get("chars", [])])
            print(f"Block {b_idx} Line {l_idx} Span {s_idx}: chars={repr(chars)}, font={span.get('font')}, size={span.get('size'):.1f}, color=#{span.get('color'):06x}, bbox={span.get('bbox')}")
