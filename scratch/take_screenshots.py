import http.server
import socketserver
import threading
import time
from playwright.sync_api import sync_playwright

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

httpd = ReusableTCPServer(('127.0.0.1', 0), http.server.SimpleHTTPRequestHandler)
PORT = httpd.server_address[1]
threading.Thread(target=httpd.serve_forever, daemon=True).start()

time.sleep(0.5)

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe', headless=True)
    
    # Desktop
    page = browser.new_page(viewport={'width': 1280, 'height': 950})
    page.goto(f'http://localhost:{PORT}/index.html')
    page.wait_for_load_state('networkidle')
    page.click('#scrollTrigger')
    page.wait_for_timeout(1400)
    page.screenshot(path='scratch/desktop_official_invitation.png')
    
    # Close-up of invitation card on desktop
    card = page.locator('#invitationCard')
    card.screenshot(path='scratch/desktop_card_crop.png')
    
    # Mobile
    mcontext = browser.new_context(viewport={'width': 390, 'height': 844}, is_mobile=True, has_touch=True)
    mpage = mcontext.new_page()
    mpage.goto(f'http://localhost:{PORT}/index.html')
    mpage.wait_for_load_state('networkidle')
    mpage.click('#scrollTrigger')
    mpage.wait_for_timeout(1400)
    mpage.screenshot(path='scratch/mobile_official_invitation.png')
    
    # Tablet
    tpage = browser.new_page(viewport={'width': 768, 'height': 1024})
    tpage.goto(f'http://localhost:{PORT}/index.html')
    tpage.wait_for_load_state('networkidle')
    tpage.click('#scrollTrigger')
    tpage.wait_for_timeout(1400)
    tpage.screenshot(path='scratch/tablet_official_invitation.png')

print('All verification screenshots captured successfully!')
