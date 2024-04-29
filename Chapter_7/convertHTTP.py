#! python3
# convertHTTP.py - Converts http:// URL adresses to https://
import re
import pyperclip

# Build regex for identifying http vs. https

httpRegex = re.compile(r'http[s]*\S+')
   
# Get URL from clipboard or user input
try: 
    urls = pyperclip.paste()
except Exception:
    urls = "http://wikipedia.org I am soo cool and secure https://cool.com"

# Match http type and convert if needed
newUrls = []
for url in httpRegex.findall(urls):
    if not url.startswith('https'):
        newUrl = url.replace("http", "https")
        newUrls.append(newUrl)
    else:
        newUrls.append(url)

# Copy new address to clipboard and/or display to screen
if len(newUrls) > 0:
    try:
        pyperclip.copy("\n".join(newUrls))
        print("Copied to clipboard.")
    except Exception:
        print("\nPyperclip error: could not copy text to clipboard.")
    print("\n".join(newUrls))

