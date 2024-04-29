#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.


from ast import expr_context
import pyperclip
import re

# Build regular expressions for phone and email
phoneRegex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits 
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # Extension  
)""", re.VERBOSE)

emailRegex = re.compile(r"""(
    [a-zA-Z0-9._%=-]+              # username
    @                              # @ symbol
    [a-zA-Z0-9.-]+                 # domain name
    (\.[a-zA-Z]{2,4})              # dot something
)""", re.VERBOSE)

zipRegEx = re.compile(r"""(
    (\d{5})                         # first 4 digits
    (-)?                            # separator
    (\d{4})?                        # Optional last four                
                      )""", re.VERBOSE)

# Find Matches in clipboard text.
try:
    text = str(pyperclip.paste())
except Exception:
    text = """

This website uses cookies to improve your experience. Learn More
Got It
Skip to main content
Home
Shopping cart
0 Items	Total: $0.00
Search
Enter your keywords 
Catalog
Merchandise
Blog
Early Access
Write for Us
About Us
Contact Us
Topics
Art & Design
General Computing
Hacking & Computer Security
Hardware / DIY
Kids
LEGO®
Linux & BSD
Manga
Programming
Python
Science & Math
Scratch
System Administration
Early Access
FREE ebook edition with every print book purchased from nostarch.com!
+

EARLY ACCESS lets you read full chapters months before a title's release date!
User login
Log in
Create account
Contact Us
Reach Us by Email - email is the best way to reach us
Help with your order: support@nostarch.com
Academic requests: academic@nostarch.com (Further information)
Bulk and special sales questions: sales@nostarch.com
Conference and event inquiries: conferences@nostarch.com
Errata - please send any errata reports to: errata@nostarch.com
General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Proposals or editorial inquiries: editors@nostarch.com
Rights inquiries: rights@nostarch.com (Further information)
Interested in working with us? 
View our current job openings
Reach Us by Mail
Mailing Address

No Starch Press
329 Primrose Road,  #42
Burlingame, CA 94010-4093
USA

Principal Place of Business

No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103
USA

NOTE: Below are our business phone numbers but we are a completely remote company. Please email support@nostarch.com with your questions and we will do our best to promptly resolve any issues that you may have.

Phone: 800.420.7240 or +1 415.863.9900
Fax: +1 415.863.9950

Reach Us on Social Media
Twitter Facebook Instagram Linkedin Pinterest

 
 

Navigation
My account
Want sweet deals?
Sign up for our newsletter.


About Us  |  Jobs!  |  Sales and Distribution  |  Rights  |  Media  |  Academic Requests  |  Conferences  |  FAQ  |  Contact Us  |  Write for Us  |  Privacy
Copyright 2024. No Starch Press, Inc
""" 

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    if phoneNum[0] != "-":
        matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


# Copy results to the clipboard.
if len(matches) > 0:
    try:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard: ')
    except Exception:
        print("Pyperclip error: Could not copy text to clipboard.")
    print("\n".join(matches))
else:
    print("No phone numbers or email addresses werer found.")

