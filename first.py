from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # This points the Python script to the browser you installed via pacman
    browser = p.chromium.launch(
        executable_path='/usr/bin/chromium', 
        headless=False
    )
    
    page = browser.new_page()
    page.goto("https://www.google.com")
    print(f"Success! Page title is: {page.title()}")
    
    browser.close()