🌍 Ubuntu Image Fetcher
"I am because we are." — Ubuntu Philosophy

A mindful Python tool for respectfully collecting and organizing images from the web. Built with the spirit of Ubuntu, this script emphasizes community, sharing, and graceful error handling.

📦 Features
✅ Fetches images from user-provided URLs

✅ Handles multiple URLs in one session

✅ Validates image type and size before saving

✅ Prevents duplicate downloads

✅ Organizes images in a dedicated Fetched_Images directory

✅ Provides clear, human-friendly terminal feedback

🧰 Requirements
Python 3.x

requests library Install via CMD:

bash
python -m pip install requests
🚀 How to Run
Save the script as ubuntu_image_fetcher.py

Open Command Prompt and navigate to the script directory

Run the script:

bash
python ubuntu_image_fetcher.py
Enter image URLs one by one. Type done when finished.

🖼️ Example Output
Code
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Enter image URLs (one per line). Type 'done' when finished:
> https://cdn.pixabay.com/photo/2024/07/27/10/55/ai-generated-8925260_1280.jpg
> done
✓ Successfully fetched: ai-generated-8925260_1280.jpg
✓ Image saved to Fetched_Images/ai-generated-8925260_1280.jpg

Connection strengthened. Community enriched.
🔒 Safety & Respect
Checks Content-Type to ensure only images are downloaded

Limits image size to ~5MB

Skips duplicates to avoid clutter

Handles network errors gracefully

🧠 Philosophy
This tool is more than a downloader—it's a reflection of Ubuntu values:

Community: Connects to the global web to gather shared resources

Respect: Handles failures without blame

Sharing: Organizes images for future appreciation

Practicality: Serves a real-world need with elegance

📁 Folder Structure
Code
ubuntu_image_fetcher.py
Fetched_Images/
├── image1.jpg
├── image2.png
