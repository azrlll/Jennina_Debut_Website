import fitz

doc = fitz.open(r'reference\DEBUT INVITATION.pdf')

# 1. In xref 228 (X16): replace BT...ET with whitespace
s_228 = doc.xref_stream(228).decode('latin1')
bt_idx1 = s_228.find('BT')
et_idx1 = s_228.find('ET', bt_idx1) + 2
if bt_idx1 != -1 and et_idx1 != -1:
    mod_228 = s_228[:bt_idx1] + ' ' * (et_idx1 - bt_idx1) + s_228[et_idx1:]
    doc.update_stream(228, mod_228.encode('latin1'))
    print("Xref 228 (white Jennina text) removed!")

# 2. In xref 229 (X19): replace BT...ET with whitespace
s_229 = doc.xref_stream(229).decode('latin1')
bt_idx2 = s_229.find('BT')
et_idx2 = s_229.find('ET', bt_idx2) + 2
if bt_idx2 != -1 and et_idx2 != -1:
    mod_229 = s_229[:bt_idx2] + ' ' * (et_idx2 - bt_idx2) + s_229[et_idx2:]
    doc.update_stream(229, mod_229.encode('latin1'))
    print("Xref 229 (gold 18 text) removed!")

# 3. In stream 23: remove /X28 Do (gold 5)
s_23 = doc.xref_stream(23).decode('latin1')
mod_23 = s_23.replace('/X28 Do', '% /X28 Do')
doc.update_stream(23, mod_23.encode('latin1'))
print("Stream 23 (/X28 Do gold 5) removed!")

# Render page 0 at high res (1241x1755, scale = 1241/595.5 = 2.083963)
page = doc[0]
zoom = 1241 / 595.5
mat = fitz.Matrix(zoom, zoom)
pix = page.get_pixmap(matrix=mat, alpha=False)
pix.save('scratch/clean_canva_p1.png')
print(f"Rendered scratch/clean_canva_p1.png: size={pix.width}x{pix.height}")
