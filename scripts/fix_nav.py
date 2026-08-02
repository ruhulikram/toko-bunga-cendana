import os
import glob
import re

files = glob.glob('*.html') + glob.glob('*.php')

new_desktop_nav = """<nav class="main-nav d-none d-lg-flex">
                            <ul class="nav">
                                <li><a href="index.html"><span class="menu-text">Home</span></a></li>
                                <li><a href="shop.html"><span class="menu-text">Shop</span></a></li>
                                <li><a href="about-us.html"><span class="menu-text">About Us</span></a></li>
                                <li><a href="contact-us.html"><span class="menu-text">Contact Us</span></a></li>
                            </ul>
                        </nav>"""

new_mobile_nav = """<nav>
                            <ul class="mobile-menu">
                                <li><a href="index.html">Home</a></li>
                                <li><a href="shop.html">Shop</a></li>
                                <li><a href="about-us.html">About Us</a></li>
                                <li><a href="contact-us.html">Contact Us</a></li>
                            </ul>
                        </nav>"""

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace Title
    title_regex = re.compile(r'<title>.*?</title>', re.IGNORECASE)
    content = title_regex.sub('<title>Toko Bunga Cendana</title>', content)
    
    
    # Replace language options in top switchers (if exist)
    
    # We will use regex to handle the desktop nav replacement precisely.
    # Look for <nav class="main-nav d-none d-lg-flex"> ... </nav>
    desktop_regex = re.compile(r'<nav class="main-nav d-none d-lg-flex">.*?</nav>', re.DOTALL)
    content = desktop_regex.sub(new_desktop_nav, content)
    
    # Look for <nav> <ul class="mobile-menu"> ... </ul> </nav> inside mobile-navigation
    mobile_regex = re.compile(r'<nav>\s*<ul class="mobile-menu">.*?</nav>', re.DOTALL)
    content = mobile_regex.sub(new_mobile_nav, content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Processed {len(files)} files.")
