# import numpy as np
# import cv2
# import matplotlib.pyplot as plt

# #Load an color image in grayscale
# img = cv2.imread('ai-generated-8762055_1920.png', cv2.IMREAD_GRAYSCALE)

# Show the image
# plt.imshow(cv2.cvtColor(img, cv2.COLORMAP_RAINBOW))
# plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# Example string
# Example string
# import re
# import pytesseract
# from PIL import Image
# import cv2
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Prahlad\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


# #Load the image
# image_path = "ewsume2.jpg"
# image = cv2.imread(image_path)

# Convert the image to RGB (Tesseract expects RGB)
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Extract text using pytesseract
# text = pytesseract.image_to_string(image)

# Example of a simple pattern to identify headings (capitalized words or words followed by a colon)
# heading_pattern = r'^[A-Z][A-Z0-9\s]*:?\s*$'

# #Split the text by lines
# lines = text.split("\n")

# Identify headings and divide the text
# sections = {}
# current_heading = None
# current_text = []

# for line in lines:
#     if re.match(heading_pattern, line.strip()):  # Check if line matches the heading pattern
#         if current_heading:  # Save the current section
#             sections[current_heading] = "\n".join(current_text)
#         current_heading = line.strip()  # Update the heading
#         current_text = []  # Reset the text for the next section
#     else:
#         current_text.append(line.strip())  # Append text under the current heading

# Don't forget to save the last section
# if current_heading:
#     sections[current_heading] = "\n".join(current_text)

# Display sections
# for heading, section_text in sections.items():
#     print(f"Heading: {heading}")
#     print(f"Content: {section_text}")
#     print("=" * 20)

import re

# Sample extracted text from resume
text = """John Doe
Email: johndoe@example.com
Phone: +123456789
---
Education:
Bachelors in Computer Science
XYZ University, 2020

Experience:
Software Developer at ABC Corp, 2021 - Present
Worked on building web applications...

Hobbies:
Reading, Traveling, Coding"""

# Define patterns to capture different sections
personal_details_pattern = r"([A-Za-z]+(?: [A-Za-z]+)*)(?:\n|.)*?(?:Email:.*?\n)?(?:Phone:.*?\n)?"
education_pattern = r"Education:\s*(.*?)\n"
experience_pattern = r"Experience:\s*(.*?)\n"
hobbies_pattern = r"Hobbies:\s*(.*?)\n"

# Find sections
personal_details = re.findall(personal_details_pattern, text, re.DOTALL)
education = re.findall(education_pattern, text, re.DOTALL)
experience = re.findall(experience_pattern, text, re.DOTALL)
hobbies = re.findall(hobbies_pattern, text, re.DOTALL)

# Print extracted sections
print("Personal Details:", personal_details)
print("Education:", education)
print("Experience:", experience)
print("Hobbies:", hobbies)
