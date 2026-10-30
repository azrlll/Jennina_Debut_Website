import fitz
import json

doc = fitz.open(r'reference\DEBUT INVITATION.pdf')
page = doc[0]
text_instances = page.get_text('rawjson')
data = json.loads(text_instances)
for block in data.get('blocks', []):
    for line in block.get('lines', []):
        for span in line.get('spans', []):
            color = span.get('color')
            hex_color = f'#{color:06x}' if isinstance(color, int) else str(color)
            txt = span.get("text")
            font = span.get("font")
            sz = span.get("size")
            bbox = [round(x, 1) for x in span.get("bbox")]
            print(f"Text: {repr(txt):30} | Font: {font:20} | Size: {sz:4.1f} | Color: {hex_color} | Box: {bbox}")
