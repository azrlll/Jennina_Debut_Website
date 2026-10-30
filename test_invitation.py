import http.server
import socketserver
import threading
import time
import sys
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Bind to free port (port 0 lets OS choose)
class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

httpd = ReusableTCPServer(('127.0.0.1', 0), http.server.SimpleHTTPRequestHandler)
PORT = httpd.server_address[1]
server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
server_thread.start()
print(f'Local test server started on port {PORT}')

time.sleep(0.5)

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe', headless=True)
    
    # =========================================================================
    # 1. DESKTOP VERIFICATION (PHASE 1, 2, 3, AND 4)
    # =========================================================================
    print("\n--- 1. Testing Desktop (1280x850) ---")
    context = browser.new_context(viewport={'width': 1280, 'height': 850})
    page = context.new_page()
    page.goto(f'http://localhost:{PORT}/index.html')
    page.wait_for_load_state('networkidle')

    # Phase 1 Checks: Opening Screen
    assert page.is_visible("text=You Are Invited"), "Phase 1: 'You Are Invited' missing"
    assert page.is_visible("text=Tap the Scroll to Open"), "Phase 1: 'Tap the Scroll to Open' missing"
    page.screenshot(path="reference/desktop_01_closed.png")
    print("  [PASS] Closed scroll opening screen verified")

    # Open Invitation
    page.click("#scrollTrigger")
    page.wait_for_timeout(1400)

    # Phase 1 Checks: Revealed Invitation Card
    assert page.is_visible("text=Celebrate a New Chapter With Us As"), "Phase 1: 'Celebrate' missing"
    assert page.is_visible("text=Jennina"), "Phase 1: 'Jennina' missing"
    assert page.is_visible("text=TURNS"), "Phase 1: 'TURNS' missing"
    assert page.is_visible("text=18"), "Phase 1: '18' missing"
    assert page.is_visible("#revealedScene .subtitle-text"), "Phase 1: 'A Decade and Eight' missing"
    assert "A Decade and Eight" in page.locator("#revealedScene .subtitle-text").inner_text()
    assert page.is_visible("text=2027"), "Phase 1: '2027' missing"
    assert page.is_visible("text=AT 3:00 PM"), "Phase 1: '3:00 PM' missing"
    print("  [PASS] Revealed Phase 1 invitation verified")

    # Phase 2 - Section 1: Save the Date
    print("\n--- Testing Phase 2 Section 1: Save the Date ---")
    s1 = page.locator("#saveTheDateSection")
    s1.scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    assert page.is_visible("text=Save the Date"), "Section 1: 'Save the Date' heading missing"
    assert page.is_visible("text=The Special Occasion Will Be Held On"), "Section 1: 'The Special Occasion Will Be Held On' missing"
    assert page.is_visible("text=FEBRUARY 5, 2027"), "Section 1: 'FEBRUARY 5, 2027' missing"
    assert page.is_visible("text=FRIDAY"), "Section 1: 'FRIDAY' missing"
    assert page.is_visible("text=3:00 PM"), "Section 1: '3:00 PM' missing"
    print("  [PASS] Section 1 (Save the Date) verified")

    # Phase 2 - Section 2: Live Countdown
    print("\n--- Testing Phase 2 Section 2: Live Countdown ---")
    s2 = page.locator("#countdownSection")
    s2.scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    assert page.is_visible("text=Live Countdown"), "Section 2: 'Live Countdown' heading missing"
    assert page.is_visible("text=DAYS"), "Section 2: 'DAYS' missing"
    assert page.is_visible("text=HOURS"), "Section 2: 'HOURS' missing"
    assert page.is_visible("text=MINUTES"), "Section 2: 'MINUTES' missing"
    assert page.is_visible("text=SECONDS"), "Section 2: 'SECONDS' missing"
    print("  [PASS] Section 2 (Live Countdown) verified")

    # Phase 2 - Section 3: February 2027 Calendar
    print("\n--- Testing Phase 2 Section 3: February 2027 Calendar ---")
    s3 = page.locator("#calendarSection")
    s3.scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    assert page.is_visible("#calendarSection .calendar-month-title"), "Calendar month title missing"
    month_title = page.locator("#calendarSection .calendar-month-title").inner_text()
    assert "FEBRUARY" in month_title.upper(), f"Expected February, got {month_title}"
    assert page.is_visible(".day-celebration-highlight"), "Friday Feb 5 highlight badge missing"
    print("  [PASS] Section 3 (February 2027 Calendar & Highlight Badge) verified")

    # Phase 2 - Section 4: The Royal Venue
    print("\n--- Testing Phase 2 Section 4: The Royal Venue ---")
    s4 = page.locator("#venueSection")
    s4.scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    assert page.is_visible("text=The Royal Venue"), "Venue heading missing"
    assert page.is_visible("text=Stalla Suites Events Places"), "Stalla Suites Events Places missing"
    assert page.is_visible("text=Pandora Hall"), "Pandora Hall missing"
    assert page.is_visible("#btnViewLocation"), "View Location button missing"
    print("  [PASS] Section 4 (The Royal Venue & View Location Button) verified")

    # Phase 3 - Section 1: 18 Roses + 18 Candles & Gifts
    print("\n--- Testing Phase 3 Section 1: 18 Roses + 18 Candles & Gifts ---")
    tsec1 = page.locator("#traditionsSection1")
    tsec1.scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    assert page.locator("#listRoses .entourage-item").count() == 18, "Expected 18 Roses"
    assert page.locator("#listCandles .entourage-item").count() == 18, "Expected 18 Candles"
    print("  [PASS] Phase 3 Section 1 verified")

    # Phase 3 - Section 2: 18 Blue Bills + 18 Shots
    print("\n--- Testing Phase 3 Section 2: 18 Blue Bills + 18 Shots ---")
    tsec2 = page.locator("#traditionsSection2")
    tsec2.scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    assert page.locator("#listBlueBills .entourage-item").count() == 18, "Expected 18 Blue Bills"
    assert page.locator("#listShots .entourage-item").count() == 18, "Expected 18 Shots"
    print("  [PASS] Phase 3 Section 2 verified")

    # =========================================================================
    # PHASE 4 - SECTION 1: ROYAL ATTIRE (DESKTOP)
    # =========================================================================
    print("\n--- Testing Phase 4 Section 1: Royal Attire ---")
    attire_sec = page.locator("#attireSection")
    attire_sec.scroll_into_view_if_needed()
    page.wait_for_timeout(600)

    # Heading check
    assert page.is_visible("#attireSection .attire-title"), "Attire heading missing"
    assert page.locator("#attireSection .attire-title").inner_text() == "ATTIRE", "Attire heading mismatch"

    # Description check
    assert page.is_visible(".attire-description"), "Attire description missing"
    desc_text = page.locator(".attire-description").inner_text()
    assert "We highly encourage our guests to dress in their finest modern royal attire" in desc_text, "Attire description mismatch"

    # Part A: For the 18th Roses
    assert page.is_visible("#attirePartRoses .subpart-title"), "Part A: 'For the 18th Roses' missing"
    roses_swatches = page.locator("#swatchesRoses .color-swatch-item")
    assert roses_swatches.count() == 5, f"Expected 5 swatches for Roses, got {roses_swatches.count()}"
    roses_swatch_names = page.locator("#swatchesRoses .swatch-color-name").all_inner_texts()
    expected_roses_colors = ["Navy Blue", "Black", "White (Inner)", "Brown", "Dark Grey"]
    for c in expected_roses_colors:
      assert c in roses_swatch_names, f"Roses color {c} missing from swatches: {roses_swatch_names}"
    print(f"  [PASS] Roses swatches verified: {roses_swatch_names}")

    # Men's Outfits Gallery
    men_outfits = page.locator("#galleryRoses .attire-photo-card")
    assert men_outfits.count() == 5, f"Expected 5 men's outfits, got {men_outfits.count()}"
    # Verify all 5 men's outfit images loaded with natural dimensions
    for i in range(5):
      img_loaded = page.evaluate(f"() => document.querySelectorAll('#galleryRoses img')[{i}].complete && document.querySelectorAll('#galleryRoses img')[{i}].naturalWidth > 0")
      assert img_loaded, f"Men's outfit image {i+1} failed to load"
    print("  [PASS] 5 Men's royal framed outfits verified and loaded")

    # Part B: For the Guests
    assert page.is_visible("#attirePartGuests .subpart-title"), "Part B: 'For the Guests' missing"
    guests_swatches = page.locator("#swatchesGuests .color-swatch-item")
    assert guests_swatches.count() == 6, f"Expected 6 swatches for Guests, got {guests_swatches.count()}"
    guests_swatch_names = page.locator("#swatchesGuests .swatch-color-name").all_inner_texts()
    expected_guests_colors = ["Ivory", "Khaki", "Plum", "Brown", "Rust", "Mustard Yellow"]
    for c in expected_guests_colors:
      assert c in guests_swatch_names, f"Guests color {c} missing from swatches: {guests_swatch_names}"
    print(f"  [PASS] Guests swatches verified (including Mustard Yellow): {guests_swatch_names}")

    # Women's Outfits Gallery
    women_outfits = page.locator("#galleryGuests .attire-photo-card")
    assert women_outfits.count() == 6, f"Expected 6 women's outfits, got {women_outfits.count()}"
    page.locator("#galleryGuests").scroll_into_view_if_needed()
    page.wait_for_timeout(1000)
    page.evaluate("() => Promise.all(Array.from(document.querySelectorAll('#galleryGuests img')).map(img => img.decode ? img.decode().catch(() => {}) : Promise.resolve()))")
    for i in range(6):
      page.locator(f"#galleryGuests .attire-photo-card:nth-child({i+1})").scroll_into_view_if_needed()
      page.wait_for_timeout(300)
      img_loaded = page.evaluate(f"() => document.querySelectorAll('#galleryGuests img')[{i}].complete && document.querySelectorAll('#galleryGuests img')[{i}].naturalWidth > 0")
      assert img_loaded, f"Women's outfit image {i+1} failed to load"
    print("  [PASS] 6 Women's royal framed gowns verified and loaded")

    page.screenshot(path="reference/desktop_09_attire_section.png")

    # =========================================================================
    # PHASE 4 - SECTION 2: GIFT GUIDE (DESKTOP)
    # =========================================================================
    print("\n--- Testing Phase 4 Section 2: Gift Guide ---")
    gift_sec = page.locator("#giftGuideSection")
    gift_sec.scroll_into_view_if_needed()
    page.wait_for_timeout(500)

    assert page.is_visible("#giftGuideSection .gift-title"), "Gift Guide heading missing"
    assert page.locator("#giftGuideSection .gift-title").inner_text() == "GIFT GUIDE", "Gift Guide heading mismatch"
    assert page.is_visible(".gift-guide-text"), "Gift guide text missing"
    gift_text = page.locator(".gift-guide-text").inner_text()
    assert "Your presence is already a precious gift" in gift_text, "Gift Guide text mismatch"
    assert "the celebrant would sincerely appreciate any gifts" in gift_text, "Gift Guide text incomplete"
    page.screenshot(path="reference/desktop_10_gift_guide.png")
    print("  [PASS] Section 2 (Gift Guide) verified")

    # =========================================================================
    # PHASE 4 - SECTION 3: IMPORTANT REMINDERS (DESKTOP)
    # =========================================================================
    print("\n--- Testing Phase 4 Section 3: Important Reminders ---")
    rem_sec = page.locator("#remindersSection")
    rem_sec.scroll_into_view_if_needed()
    page.wait_for_timeout(500)

    assert page.is_visible("#remindersSection .reminders-title"), "Important Reminders heading missing"
    assert page.locator("#remindersSection .reminders-title").inner_text() == "IMPORTANT REMINDERS", "Heading mismatch"
    assert page.is_visible(".reminders-main-text"), "Reminders text missing"
    rem_text = page.locator(".reminders-main-text").inner_text()
    assert "Kindly arrive on time before the program starts" in rem_text, "Reminders text mismatch"
    assert "follow the dress code and bring your warmest smiles" in rem_text, "Reminders text incomplete"
    
    # Verify triad items
    triads = page.locator(".reminder-card-item")
    assert triads.count() == 3, f"Expected 3 reminder triad cards, got {triads.count()}"
    page.screenshot(path="reference/desktop_11_reminders.png")
    print("  [PASS] Section 3 (Important Reminders & Triad Cards) verified")

    # =========================================================================
    # PHASE 5: SECTION 10 — ZITE RSVP INTEGRATION VERIFICATION
    # =========================================================================
    print("\n--- Testing Phase 5: Zite RSVP Integration ---")
    s10 = page.locator("#rsvpSection")
    s10.scroll_into_view_if_needed()
    page.wait_for_timeout(500)

    # 1. Visual Elements Verification
    assert page.is_visible("#rsvpSection"), "RSVP section missing"
    assert page.is_visible("#rsvpSection .rsvp-title"), "RSVP title missing"
    assert page.locator("#rsvpSection .rsvp-title").inner_text() == "RSVP", "RSVP title text mismatch"
    assert page.is_visible(".rsvp-crown-badge"), "RSVP crown crest missing"
    assert page.is_visible(".rsvp-arch-img"), "RSVP royal arched frame missing"

    # 2. Required Text Verification
    assert page.is_visible(".rsvp-main-message"), "RSVP main message missing"
    rsvp_msg = page.locator(".rsvp-main-message").inner_text()
    assert "reserved seats for you" in rsvp_msg, f"Message missing expected text, got: {rsvp_msg}"
    assert "January 15, 2027" in rsvp_msg, "Deadline date missing from message"
    assert "replying through Messenger or our website" in rsvp_msg, "Channels missing from message"

    # 3. Required Important Notice: NO RSVP, NO SEAT
    assert page.is_visible(".rsvp-notice-box"), "NO RSVP, NO SEAT notice box missing"
    notice_text = page.locator(".rsvp-notice-box .notice-text").inner_text()
    assert notice_text == "NO RSVP, NO SEAT", f"Expected 'NO RSVP, NO SEAT', got {notice_text}"

    # 4. Required RSVP Deadline Badge
    assert page.is_visible(".rsvp-deadline-badge"), "RSVP deadline badge missing"
    deadline_text = page.locator(".rsvp-deadline-badge .deadline-text").inner_text()
    assert "January 15, 2027" in deadline_text, f"Deadline badge missing date, got: {deadline_text}"

    # 5. Live Configured State: RSVP_URL = "https://3gtkwbxbwf.zite.so"
    print("  Subtest 5A: Verifying live configured published RSVP URL state...")
    btn_zite = page.locator("#btnZiteRsvp")
    lbl_zite = page.locator("#lblZiteRsvp")
    btn_messenger = page.locator("#btnMessengerRsvp")

    assert btn_zite.is_visible(), "Zite RSVP button missing"
    assert "Confirm Your Attendance" in lbl_zite.text_content(), f"Expected 'Confirm Your Attendance', got {lbl_zite.text_content()}"
    assert "btn-disabled" not in btn_zite.get_attribute("class"), "Button should NOT have .btn-disabled when URL is configured"
    assert btn_zite.get_attribute("aria-disabled") is None, "Button should not have aria-disabled"
    assert btn_zite.get_attribute("href") == "https://3gtkwbxbwf.zite.so", f"href mismatch: {btn_zite.get_attribute('href')}"
    assert btn_zite.get_attribute("target") == "_blank", "Button target must be _blank"
    assert btn_zite.get_attribute("rel") == "noopener noreferrer", "Button rel must be noopener noreferrer"
    page.screenshot(path="reference/desktop_13_rsvp_active.png")
    print("    [PASS] Live configured Zite RSVP URL verified (Confirm Your Attendance, enabled, target=_blank)")

    # 6. Click Handling Test: Verify popup / new tab handling
    with context.expect_page() as new_page_info:
        btn_zite.click()
    new_page = new_page_info.value
    assert "3gtkwbxbwf.zite.so" in new_page.url or "about:blank" in new_page.url, f"Unexpected target URL: {new_page.url}"
    new_page.close()
    print("    [PASS] Clicking button successfully opened published Zite RSVP site in a new tab")

    # 7. Fallback Empty State Test
    print("  Subtest 5B: Testing fallback when RSVP_URL is empty...")
    page.evaluate("window.__setRsvpUrlsForTesting('', '')")
    page.wait_for_timeout(200)
    assert "RSVP Link Coming Soon" in lbl_zite.text_content(), "Expected 'RSVP Link Coming Soon'"
    assert "btn-disabled" in btn_zite.get_attribute("class"), "Should have .btn-disabled"
    assert btn_zite.get_attribute("aria-disabled") == "true", "Should have aria-disabled='true'"
    print("    [PASS] Fallback empty state works properly")

    # 8. Editor URL Blocking Test
    print("  Subtest 5C: Testing that Zite editor URL is rejected and blocked...")
    editor_url = "https://app.zite.com/editor/oinyLbhrWgus/edit/gXFa"
    page.evaluate(f"window.__setRsvpUrlsForTesting('{editor_url}', '')")
    page.wait_for_timeout(200)
    assert "RSVP Link Coming Soon" in lbl_zite.text_content(), "Editor URL should NOT activate the button"
    assert "btn-disabled" in btn_zite.get_attribute("class"), "Editor URL must keep button disabled"
    print("    [PASS] Editor URL successfully blocked and kept disabled")

    # 9. Restore Live State
    page.evaluate("window.__setRsvpUrlsForTesting('https://3gtkwbxbwf.zite.so', '')")
    page.wait_for_timeout(200)
    assert "Confirm Your Attendance" in lbl_zite.text_content(), "Restore failed"
    assert "btn-disabled" not in btn_zite.get_attribute("class"), "Restore failed"
    print("    [PASS] Restored live Zite RSVP state")

    # Check dividers
    dividers_count = page.locator(".royal-floral-divider").count()
    assert dividers_count >= 10, f"Expected at least 10 gold floral dividers, got {dividers_count}"
    print(f"  [PASS] {dividers_count} Gold Floral Dividers verified across entire page")

    # =========================================================================
    # 2. MOBILE TEST (iPhone 14 Viewport 390x844)
    # =========================================================================
    print("\n--- 2. Testing Mobile (390x844) ---")
    mobile_context = browser.new_context(
        viewport={'width': 390, 'height': 844},
        is_mobile=True,
        has_touch=True,
        user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)'
    )
    mpage = mobile_context.new_page()
    mpage.goto(f'http://localhost:{PORT}/index.html')
    mpage.wait_for_load_state('networkidle')
    mpage.tap("#scrollTrigger")
    mpage.wait_for_timeout(1400)

    # Scroll to Attire Section on Mobile
    mattire = mpage.locator("#attireSection")
    mattire.scroll_into_view_if_needed()
    mpage.wait_for_timeout(600)
    assert mpage.is_visible("#attireSection .attire-title"), "Mobile Attire title missing"
    mpage.screenshot(path="reference/mobile_09_attire_roses.png")
    
    mpage.locator("#attirePartGuests").scroll_into_view_if_needed()
    mpage.wait_for_timeout(500)
    mpage.screenshot(path="reference/mobile_10_attire_guests.png")
    print("  [PASS] Mobile Attire section verified")

    # Scroll to Gift Guide on Mobile
    mgift = mpage.locator("#giftGuideSection")
    mgift.scroll_into_view_if_needed()
    mpage.wait_for_timeout(500)
    assert mpage.is_visible("#giftGuideSection .gift-title"), "Mobile Gift Guide title missing"
    mpage.screenshot(path="reference/mobile_11_gift_guide.png")
    print("  [PASS] Mobile Gift Guide verified")

    # Scroll to Important Reminders on Mobile
    mrem = mpage.locator("#remindersSection")
    mrem.scroll_into_view_if_needed()
    mpage.wait_for_timeout(500)
    assert mpage.is_visible("#remindersSection .reminders-title"), "Mobile Reminders title missing"
    mpage.screenshot(path="reference/mobile_12_reminders.png")
    print("  [PASS] Mobile Important Reminders verified")

    # Scroll to RSVP Section on Mobile
    mrsvp = mpage.locator("#rsvpSection")
    mrsvp.scroll_into_view_if_needed()
    mpage.wait_for_timeout(600)
    assert mpage.is_visible("#rsvpSection .rsvp-title"), "Mobile RSVP title missing"
    assert mpage.is_visible("#btnZiteRsvp"), "Mobile Zite RSVP button missing"

    # Verify touch target height >= 48px
    btn_box = mpage.locator("#btnZiteRsvp").bounding_box()
    assert btn_box['height'] >= 48, f"Mobile RSVP button height {btn_box['height']}px is less than 48px touch target!"
    print(f"  [PASS] Mobile button touch height verified: {btn_box['height']}px (>= 48px)")
    mpage.screenshot(path="reference/mobile_13_rsvp.png")

    # Check for horizontal scrollbars / overflow in mobile
    has_horizontal_overflow = mpage.evaluate("() => document.documentElement.scrollWidth > window.innerWidth")
    assert not has_horizontal_overflow, "Mobile page has horizontal overflow!"
    print("  [PASS] Mobile responsiveness verified with 0 horizontal overflow")

    # =========================================================================
    # 3. TABLET TEST (iPad 768x1024)
    # =========================================================================
    print("\n--- 3. Testing Tablet (768x1024) ---")
    tablet_context = browser.new_context(viewport={'width': 768, 'height': 1024})
    tpage = tablet_context.new_page()
    tpage.goto(f'http://localhost:{PORT}/index.html')
    tpage.wait_for_load_state('networkidle')
    tpage.click("#scrollTrigger")
    tpage.wait_for_timeout(1400)
    tpage.locator("#attireSection").scroll_into_view_if_needed()
    tpage.wait_for_timeout(500)
    tpage.screenshot(path="reference/tablet_03_attire.png")
    
    tpage.locator("#remindersSection").scroll_into_view_if_needed()
    tpage.wait_for_timeout(500)
    tpage.screenshot(path="reference/tablet_04_gift_and_reminders.png")
    
    tpage.locator("#rsvpSection").scroll_into_view_if_needed()
    tpage.wait_for_timeout(500)
    assert tpage.is_visible("#rsvpSection"), "Tablet RSVP section missing"
    tpage.screenshot(path="reference/tablet_05_rsvp.png")
    print("  [PASS] Tablet view verified for Phase 4 & Phase 5 RSVP")

    # =========================================================================
    # 4. ACCESSIBILITY & REDUCED MOTION VERIFICATION
    # =========================================================================
    print("\n--- 4. Testing Accessibility & Reduced Motion ---")
    rm_context = browser.new_context(viewport={'width': 1280, 'height': 850}, reduced_motion='reduce')
    rm_page = rm_context.new_page()
    rm_page.goto(f'http://localhost:{PORT}/index.html')
    rm_page.click("#scrollTrigger")
    rm_page.wait_for_timeout(300)
    assert rm_page.is_visible("#attireSection"), "Reduced motion Attire section failed"
    assert rm_page.is_visible("#giftGuideSection"), "Reduced motion Gift Guide failed"
    assert rm_page.is_visible("#remindersSection"), "Reduced motion Reminders failed"
    assert rm_page.is_visible("#rsvpSection"), "Reduced motion RSVP section failed"
    print("  [PASS] Reduced motion mode verified")

    browser.close()
    httpd.shutdown()

print("\n=======================================================")
print("ALL PHASE 1, 2, 3, 4 & 5 TESTS COMPLETED & PASSED SUCCESSFULLY!")
print("=======================================================")
