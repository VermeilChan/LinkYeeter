from bs4 import BeautifulSoup
from requests import Session, RequestException

def get_addons_links():
    url = input("Enter the full link to the Steam collection: ").strip()

    if not (url.startswith("https://steamcommunity.com/sharedfiles/") and "id=" in url):
        print("Invalid URL format. Please enter a valid Steam collection URL.")
        return

    try:
        print("Fetching collection page...")

        session = Session()

        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        session.headers.update({'User-Agent': user_agent})

        print(f"Using User-Agent: {session.headers['User-Agent']}")

        response = session.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        links = [
            (link_tag['href'], title_tag.text.strip())
            for item in soup.select('div.collectionItem')
            if (link_tag := item.select_one('a[href]')) and (title_tag := item.select_one('.workshopItemTitle'))
        ]

        if links:
            file_name = 'addon_links.txt'
            with open(file_name, 'w') as file:
                file.write('\n'.join(link for link, _ in links) + '\n')

            print(f"Found {len(links)} links and saved to '{file_name}'.")
        else:
            print("No links found.")

    except RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
