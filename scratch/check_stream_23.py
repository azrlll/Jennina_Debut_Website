import fitz

doc = fitz.open(r'reference\DEBUT INVITATION.pdf')
stream_23 = doc.xref_stream(23).decode('latin1', errors='ignore')
print(f"Stream 23 length: {len(stream_23)}")
print("Stream 23 preview:\n", stream_23[:2000])
