from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-minimized")
chrome_options.add_argument("--window-position=99000,99000")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-browser-side-navigation")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-default-apps")
chrome_options.add_argument("--disable-hang-monitor")
chrome_options.add_argument("--disable-prompt-on-repost")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-sync")
chrome_options.add_argument("--disable-translate")
chrome_options.add_argument("--disable-web-resources")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--no-first-run")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--blink-settings=imagesEnabled=false")
