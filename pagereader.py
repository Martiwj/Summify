import requests
from bs4 import BeautifulSoup

def read_webpage(url: str) -> str:
    tokens = ""
    # Send an HTTP request to the webpage
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text from specific HTML tags (e.g., <p>, <h1-h6>, <a>)
        for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            # Skip header, footer, and links
            if any(parent.name in ['header', 'footer', 'a'] for parent in tag.find_parents(['header', 'footer', 'a'])):
                continue
            tokens += tag.get_text() + " "

    else:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"
    return tokens
