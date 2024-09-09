import requests
from bs4 import BeautifulSoup

# Define the base URL and the range of chapters to scrape
base_url = "https://novelbjn.novelmagic.org/book/chaos-heir/chapter-"
start_chapter = 1
end_chapter = 865

# Create or open a text file to store the chapter contents
with open('chaos_heir_novel.txt', 'w', encoding='utf-8') as f:
    # Iterate over the chapters
    for chapter in range(start_chapter, end_chapter + 1):
        # Construct the URL for each chapter
        url = base_url + str(chapter)
        print(f"Scraping {url}...")

        # Send a GET request to the URL
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            try:
                # Extract the chapter title and content (update the selector based on inspection)
                title = soup.find('h1').get_text()
                content_div = soup.find('div', class_='chr-c')

                if content_div:
                    content = content_div.get_text(separator='\n')
                else:
                    print(f"Content not found for {url}")
                    continue

                # Write the title and content to the text file
                f.write(title + '\n\n')
                f.write(content + '\n\n')

            except Exception as e:
                print(f"Error scraping {url}: {e}")
        else:
            print(f"Failed to retrieve {url}, status code: {response.status_code}")
