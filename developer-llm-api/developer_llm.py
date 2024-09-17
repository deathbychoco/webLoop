import openai
import os

# Set your OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the prompt for generating HTML and CSS with clear delimiters
messages = [
    {"role": "system", "content": "You are a professional web developer."},
    {"role": "user", "content": """
        Please generate both HTML and CSS for a modern, corporate-style website. 
        Output the HTML and CSS separately, wrapped in clear markers.
        
        1. HTML Structure:
            - A responsive design with a professional color scheme (shades of blue, white, and gray).
            - A header section with a navigation bar. The navigation bar should have links to 'Home', 'About Us', 'Services', and 'Contact'.
            - A hero section with a large background image, bold heading text, and a call-to-action button that says 'Learn More'.
            - A section for About Us with a headline and a few paragraphs describing the company.
            - A section for Our Services, with icons or images representing each service and brief descriptions.
            - A Contact Information section with an email address, phone number, and social media icons.
            - A footer with social media links and a copyright notice.

        2. CSS Stylesheet:
            - Use professional colors like dark blue, light gray, and white.
            - The navigation bar should have a hover effect on links and stay fixed at the top.
            - The hero section should have a full-width background image, large centered text, and a call-to-action button.
            - Padding and spacing between sections for readability.
            - Make the website responsive using media queries.
            - Basic animations for buttons (color change or scale on hover).

        Output the HTML and CSS separately, using the following delimiters to wrap the content:
        - For HTML: use `<!-- HTML_START -->` and `<!-- HTML_END -->`.
        - For CSS: use `/* CSS_START */` and `/* CSS_END */`.

        Make sure to include only valid HTML code within the HTML markers and only CSS code within the CSS markers.
    """}
]

# Use the ChatCompletion API to get a response
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",  # Use GPT-4 for better HTML and CSS generation
    messages=messages,
    max_tokens=2000  # Increase token limit for more detailed responses
)

# Print the response for debugging purposes
print("API Response:", response)

# Access the generated content
generated_content = response.choices[0].message.content

# Split the HTML and CSS content based on the delimiters
html_content = ""
css_content = ""

# Extract HTML and CSS using the delimiters
if "<!-- HTML_START -->" in generated_content and "/* CSS_START */" in generated_content:
    html_content = generated_content.split("<!-- HTML_START -->")[1].split("<!-- HTML_END -->")[0].strip()
    css_content = generated_content.split("/* CSS_START */")[1].split("/* CSS_END */")[0].strip()
else:
    print("Error: Delimiters not found in the response.")
    html_content = generated_content  # Save the raw content as fallback

# Ensure the CSS is linked in the HTML by adding the <link> tag in the <head> section
if "<head>" in html_content:
    html_content = html_content.replace(
        "<head>", "<head>\n    <link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">"
    )
else:
    # If no <head> is found, we append it to the top of the HTML content
    html_content = "<head>\n    <link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">\n</head>\n" + html_content

# Log the contents before saving to files
print("HTML Content:\n", html_content)
print("CSS Content:\n", css_content)

# Save the generated HTML to the mounted volume (host)
html_output_path = '/app/data/generated_website.html'
with open(html_output_path, 'w') as f:
    f.write(html_content)

# Save the generated CSS to a separate file in the mounted volume (host)
css_output_path = '/app/data/style.css'
with open(css_output_path, 'w') as f:
    if css_content:
        f.write(css_content)
    else:
        f.write("/* No CSS generated */")

print(f"Corporate-style website HTML and CSS generated and saved to {html_output_path} and {css_output_path}!")
