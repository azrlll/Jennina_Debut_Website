with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_start = '      <!-- Golden Framed Royal Invitation Card -->'
old_end = '      </article>\n'
if old_end not in text:
    old_end = '      </article>\r\n'

start_pos = text.find(old_start)
end_pos = text.find(old_end, start_pos) + len(old_end)

if start_pos != -1 and end_pos != -1:
    print('Found old invitation card block at', start_pos, 'to', end_pos)
    
    new_card = '''      <!-- =====================================================================
           OFFICIAL ROYAL INVITATION (From PDF Page 1, Year Corrected to 2027)
           ===================================================================== -->
      <section class="royal-official-invitation-section" id="invitationCard" aria-label="Official Debut Invitation Presentation">
        <div class="official-invitation-container" tabindex="0" role="button" aria-label="Official Debut Invitation for Jennina - Tap to enlarge">
          <picture>
            <source srcset="assets/images/jennina-official-invitation.webp" type="image/webp">
            <img src="assets/images/jennina-official-invitation.png" 
                 id="officialInvitationImg"
                 alt="Jennina Turns 18 - Official Debut Invitation - Friday, February 5, 2027 at 3:00 PM at Stalla Suites Events Place (Pandora Hall)" 
                 class="official-invitation-image"
                 width="1241"
                 height="1756"
                 loading="eager"
                 decoding="async">
          </picture>
          <div class="invitation-tap-hint" aria-hidden="true">
            <span class="tap-hint-icon">🔍</span>
            <span class="tap-hint-text">Tap to enlarge invitation</span>
          </div>
        </div>
      </section>
'''
    text = text[:start_pos] + new_card + text[end_pos:]
    
    # Also add the lightbox modal before </main>
    lightbox_markup = '''      <!-- Lightbox Modal for Fullscreen Official Invitation Inspection -->
      <div class="invitation-lightbox-modal" id="invitationLightbox" role="dialog" aria-modal="true" aria-label="Enlarged Official Invitation" hidden>
        <div class="lightbox-backdrop" id="lightboxBackdrop"></div>
        <div class="lightbox-dialog-content">
          <button type="button" class="lightbox-close-btn" id="lightboxCloseBtn" aria-label="Close enlarged view">&times;</button>
          <img src="assets/images/jennina-official-invitation.png" alt="Enlarged Official Debut Invitation" class="lightbox-enlarged-img">
        </div>
      </div>
'''
    main_end = '</main>'
    pos_main = text.rfind(main_end)
    text = text[:pos_main] + lightbox_markup + '    ' + text[pos_main:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Successfully updated index.html!')
else:
    print('Failed to locate block')
