with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Part 1: Replace section 11 (lines ~873 to .venue-name)
old_sec11_header = '/* --------------------------------------------------------------------------\n   11. THE ROYAL GOLDEN FRAME INVITATION CARD (PDF PAGE 1 RECREATION)\n   -------------------------------------------------------------------------- */'
if old_sec11_header not in css:
    old_sec11_header = '/* --------------------------------------------------------------------------\r\n   11. THE ROYAL GOLDEN FRAME INVITATION CARD (PDF PAGE 1 RECREATION)\r\n   -------------------------------------------------------------------------- */'

venue_name_str = '.venue-name {'
pos_start = css.find(old_sec11_header)
pos_venue = css.find(venue_name_str, pos_start)

if pos_start == -1 or pos_venue == -1:
    print('Error: Could not locate Section 11 in css/style.css')
    exit(1)

new_sec11 = '''/* --------------------------------------------------------------------------
   11. OFFICIAL ROYAL INVITATION CARD (FROM PDF PAGE 1, YEAR CORRECTED TO 2027)
   -------------------------------------------------------------------------- */
.royal-official-invitation-section {
  position: relative;
  width: 100%;
  max-width: 580px;
  margin: 32px auto 36px auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.official-invitation-container {
  position: relative;
  width: 100%;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 
    0 16px 45px rgba(0, 0, 0, 0.75),
    0 0 25px rgba(212, 175, 55, 0.25),
    inset 0 0 0 1px rgba(212, 175, 55, 0.35);
  cursor: pointer;
  background: #031e16;
  transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.35s ease;
  outline: none;
}

.official-invitation-container:hover,
.official-invitation-container:focus-visible {
  transform: translateY(-4px) scale(1.006);
  box-shadow: 
    0 24px 55px rgba(0, 0, 0, 0.85),
    0 0 40px rgba(212, 175, 55, 0.45),
    inset 0 0 0 1.5px rgba(212, 175, 55, 0.6);
}

.official-invitation-image {
  width: 100%;
  height: auto;
  display: block;
  object-fit: contain;
  transition: opacity 0.5s ease;
}

.invitation-tap-hint {
  position: absolute;
  bottom: 14px;
  left: 50%;
  transform: translateX(-50%);
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 6px 16px;
  background: rgba(3, 30, 22, 0.85);
  border: 1px solid rgba(212, 175, 55, 0.5);
  border-radius: 20px;
  color: #f7ecd5;
  font-family: var(--font-serif);
  font-size: clamp(0.72rem, 1.6vw, 0.82rem);
  letter-spacing: 0.05em;
  pointer-events: none;
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  opacity: 0.88;
  transition: opacity 0.3s ease, background 0.3s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
}

.official-invitation-container:hover .invitation-tap-hint,
.official-invitation-container:focus-visible .invitation-tap-hint {
  opacity: 1;
  background: rgba(3, 30, 22, 0.96);
  border-color: rgba(212, 175, 55, 0.85);
}

/* Lightbox Modal for Fullscreen Official Invitation */
.invitation-lightbox-modal {
  position: fixed;
  inset: 0;
  z-index: 99999;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.invitation-lightbox-modal.active {
  opacity: 1;
  pointer-events: auto;
}

.lightbox-backdrop {
  position: absolute;
  inset: 0;
  background: rgba(2, 20, 15, 0.94);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.lightbox-dialog-content {
  position: relative;
  z-index: 2;
  max-width: 92vw;
  max-height: 92vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.lightbox-close-btn {
  position: absolute;
  top: -42px;
  right: 0;
  background: rgba(212, 175, 55, 0.2);
  border: 1px solid rgba(212, 175, 55, 0.6);
  color: #fff;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  font-size: 24px;
  line-height: 1;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.lightbox-close-btn:hover {
  background: rgba(212, 175, 55, 0.4);
  transform: scale(1.1);
}

.lightbox-enlarged-img {
  max-width: 100%;
  max-height: 85vh;
  object-fit: contain;
  border-radius: 12px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.9), 0 0 35px rgba(212, 175, 55, 0.4);
}

'''

css = css[:pos_start] + new_sec11 + css[pos_venue:]

# Remove old media query card rules:
# In media (max-width: 767px)
css = css.replace('.royal-invitation-card {\n    min-height: auto;\n    margin: 24px auto 18px auto;\n  }', '.royal-official-invitation-section {\n    max-width: 100%;\n    margin: 20px auto 24px auto;\n  }')
css = css.replace('.royal-invitation-card {\r\n    min-height: auto;\r\n    margin: 24px auto 18px auto;\r\n  }', '.royal-official-invitation-section {\r\n    max-width: 100%;\r\n    margin: 20px auto 24px auto;\r\n  }')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Successfully updated css/style.css!')
