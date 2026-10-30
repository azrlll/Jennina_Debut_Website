with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

lightbox_code = '''  /**
   * Official Invitation Lightbox Modal
   * Allows guests (especially on mobile) to tap to view an enlarged version
   */
  function initInvitationLightbox() {
    const container = document.querySelector('.official-invitation-container');
    const modal = document.getElementById('invitationLightbox');
    const closeBtn = document.getElementById('lightboxCloseBtn');
    const backdrop = document.getElementById('lightboxBackdrop');

    if (!container || !modal) return;

    function openModal() {
      modal.removeAttribute('hidden');
      requestAnimationFrame(() => modal.classList.add('active'));
      document.body.style.overflow = 'hidden';
      if (closeBtn) closeBtn.focus();
    }

    function closeModal() {
      modal.classList.remove('active');
      setTimeout(() => {
        modal.setAttribute('hidden', '');
        document.body.style.overflow = '';
        container.focus();
      }, 300);
    }

    container.addEventListener('click', openModal);
    container.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        openModal();
      }
    });

    if (closeBtn) closeBtn.addEventListener('click', closeModal);
    if (backdrop) backdrop.addEventListener('click', closeModal);
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('active')) {
        closeModal();
      }
    });
  }

  // Initialize Dynamic Elements
  populateTraditionLists();
  initMobileTraditionTabs();
  populateAttireSection();
  initSectionObserver();
  initRsvpIntegration();
  initInvitationLightbox();
'''

old_target = '''  // Initialize Dynamic Elements
  populateTraditionLists();
  initMobileTraditionTabs();
  populateAttireSection();
  initSectionObserver();
  initRsvpIntegration();'''

if old_target in js:
    js = js.replace(old_target, lightbox_code)
elif old_target.replace('\n', '\r\n') in js:
    js = js.replace(old_target.replace('\n', '\r\n'), lightbox_code.replace('\n', '\r\n'))
else:
    print('Error: Target not found in js/main.js')
    exit(1)

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully added initInvitationLightbox to js/main.js!')
