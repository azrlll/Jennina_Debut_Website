from PIL import Image

clean = Image.open('scratch/clean_canva_p1.png')

# Save WebP with high quality
clean.save('assets/images/canva_invitation_card_page1.webp', 'WEBP', quality=92, method=6)
print("Saved assets/images/canva_invitation_card_page1.webp")

# Save PNG with optimization
clean.save('assets/images/canva_invitation_card_page1_opt.png', 'PNG', optimize=True)
print("Saved assets/images/canva_invitation_card_page1_opt.png")
