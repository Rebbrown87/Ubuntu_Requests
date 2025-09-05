#importing os and requests
import os
import requests
from urllib.parse import urlparse
from uuid import uuid4

#fetched image directory
FETCH_DIR = "Fetched_Images"
MAX_SIZE = 5_000_000  # ~5MB

def welcome():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

#urls from online with images
def get_urls():
    print("Enter image URLs (one per line). Type 'done' when finished:")
    urls = []
    while True: #urls parsing
        url = input("> ").strip()
        if url.lower() == 'done':
            break
        if url.startswith("http"):
            urls.append(url)
    return urls

#fetch directory
def create_directory(path=FETCH_DIR):
    os.makedirs(path, exist_ok=True)

def extract_filename(url):
    parsed = urlparse(url)
    name = os.path.basename(parsed.path)
    return name if name else f"image_{uuid4().hex}.jpg"

def is_safe_image(response):
    content_type = response.headers.get("Content-Type", "")
    if not content_type.startswith("image/"):
        print("✗ Not an image. Skipping.")
        return False
    content_length = response.headers.get("Content-Length")
    if content_length and int(content_length) > MAX_SIZE:
        print("✗ Image too large. Skipping.")
        return False
    return True

#dealing with duplicates
def is_duplicate(filepath):
    return os.path.exists(filepath)

def fetch_and_save_image(url):
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()

        if not is_safe_image(response):
            return

        filename = extract_filename(url)
        filepath = os.path.join(FETCH_DIR, filename)

        if is_duplicate(filepath):
            print(f"✗ Duplicate detected: {filename}. Skipping.")
            return

        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}\n")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    welcome()
    create_directory()
    urls = get_urls()
    for url in urls:
        fetch_and_save_image(url)
    print("Connection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
