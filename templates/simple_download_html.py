import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from urllib.parse import urljoin, urlparse
import os
import time
import shutil

# User input URL
URL = input("Enter the URL to download: ")

# Automatically create a folder based on the URL
def sanitize_folder_name(url):
    parsed_url = urlparse(url)
    folder_name = parsed_url.netloc.replace('.', '_')
    return folder_name

SAVE_DIR = os.path.join("downloaded_pages", sanitize_folder_name(URL))
os.makedirs(SAVE_DIR, exist_ok=True)

# Set Chrome Driver options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Launch Chrome Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

print(f"[+] Downloading: {URL}")
driver.get(URL)

# Scroll to trigger lazy loading
for _ in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Get the complete HTML
html_content = driver.page_source

# Save the HTML
html_path = os.path.join(SAVE_DIR, "index.html")
with open(html_path, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"[+] HTML saved to {html_path}")

# Download all images, CSS, and JS resources
resource_types = [
    ("//link[@rel='stylesheet']", "href"),  # CSS
    ("//script[@src]", "src"),              # JS
    ("//img", "src")                        # Images
]

for xpath, attr in resource_types:
    resources = driver.find_elements("xpath", xpath)
    for resource in resources:
        src = resource.get_attribute(attr)
        if src:
            full_url = urljoin(URL, src)  # Convert to full URL
            file_name = full_url.split("/")[-1].split("?")[0]
            save_path = os.path.join(SAVE_DIR, file_name)
            try:
                response = requests.get(full_url, stream=True, timeout=10)
                if response.status_code == 200:
                    with open(save_path, "wb") as f:
                        shutil.copyfileobj(response.raw, f)
                    print(f"[+] Resource downloaded: {file_name}")
                else:
                    print(f"[-] Failed to download: {full_url}")
            except Exception as e:
                print(f"[-] Error downloading: {full_url} | Error: {e}")

driver.quit()
print(f"✅ Complete webpage and resources from {URL} have been downloaded to {SAVE_DIR}!")
