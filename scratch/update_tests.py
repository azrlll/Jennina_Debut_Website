with open('test_invitation.py', 'r', encoding='utf-8') as f:
    code = f.read()

old_desktop_phase1 = '''    # Phase 1 Checks: Revealed Invitation Card
    assert page.is_visible("text=Celebrate a New Chapter With Us As"), "Phase 1: 'Celebrate' missing"
    assert page.is_visible("text=Jennina"), "Phase 1: 'Jennina' missing"
    assert page.is_visible("text=TURNS"), "Phase 1: 'TURNS' missing"
    assert page.is_visible("text=18"), "Phase 1: '18' missing"
    assert page.is_visible("#revealedScene .subtitle-text"), "Phase 1: 'A Decade and Eight' missing"
    assert "A Decade and Eight" in page.locator("#revealedScene .subtitle-text").inner_text()
    assert page.is_visible("text=2027"), "Phase 1: '2027' missing"
    assert page.is_visible("text=AT 3:00 PM"), "Phase 1: '3:00 PM' missing"
    print("  [PASS] Revealed Phase 1 invitation verified")'''

new_desktop_phase1 = '''    # Phase 1 Checks: Revealed Official Invitation Image (PDF Page 1, Year Corrected to 2027)
    assert page.is_visible("#officialInvitationImg"), "Phase 1: Official invitation image missing"
    official_img = page.locator("#officialInvitationImg")
    assert official_img.is_visible(), "Phase 1: Official invitation image is not visible"
    img_natural_w = page.evaluate("document.getElementById('officialInvitationImg').naturalWidth")
    img_natural_h = page.evaluate("document.getElementById('officialInvitationImg').naturalHeight")
    assert img_natural_w > 0 and img_natural_h > 0, f"Phase 1: Failed to load official invitation image ({img_natural_w}x{img_natural_h})"
    
    # Task 1 Check: Verify old rectangular cream card design elements are removed
    assert page.locator(".card-parchment-body").count() == 0, "Phase 1: Old rectangular cream card body was not removed"
    assert page.locator(".baroque-frame-img").count() == 0, "Phase 1: Old baroque frame was not removed"
    assert page.locator(".card-floral-swag").count() == 0, "Phase 1: Old floral swag was not removed"
    assert page.locator(".card-butterfly").count() == 0, "Phase 1: Old butterfly was not removed"
    
    # Task 4 Check: Lightbox modal tap-to-enlarge
    page.click(".official-invitation-container")
    page.wait_for_timeout(350)
    assert page.is_visible("#invitationLightbox"), "Lightbox failed to open on click"
    page.click("#lightboxCloseBtn")
    page.wait_for_timeout(350)
    print("  [PASS] Revealed Official PDF invitation and tap-to-enlarge lightbox verified")'''

if old_desktop_phase1 in code:
    code = code.replace(old_desktop_phase1, new_desktop_phase1)
elif old_desktop_phase1.replace('\n', '\r\n') in code:
    code = code.replace(old_desktop_phase1.replace('\n', '\r\n'), new_desktop_phase1.replace('\n', '\r\n'))
else:
    print('Error: old_desktop_phase1 not found')
    exit(1)

# Add mobile Phase 1 check
mobile_trigger = '''    mpage.tap("#scrollTrigger")
    mpage.wait_for_timeout(1400)'''

mobile_check = '''    mpage.tap("#scrollTrigger")
    mpage.wait_for_timeout(1400)

    # Phase 1 Mobile Check: Official Invitation Image
    assert mpage.is_visible("#officialInvitationImg"), "Mobile: Official invitation image missing"
    box = mpage.locator("#officialInvitationImg").bounding_box()
    assert box['width'] <= 390, f"Mobile invitation width {box['width']} exceeds 390px"
    print(f"  [PASS] Mobile official invitation image responsive: width={box['width']:.1f}px")'''

if mobile_trigger in code:
    code = code.replace(mobile_trigger, mobile_check)
elif mobile_trigger.replace('\n', '\r\n') in code:
    code = code.replace(mobile_trigger.replace('\n', '\r\n'), mobile_check.replace('\n', '\r\n'))

with open('test_invitation.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('Successfully updated test_invitation.py!')
