from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from requests import Session, RequestException

def get_addons_links():
    url = input("Enter the full link to the Steam collection: ").strip()

    if not (url.startswith("https://steamcommunity.com/sharedfiles/") and "id=" in url):
        print("Invalid URL format. Please enter a valid Steam collection URL.")
        return

    try:
        print("Fetching collection page...")

        session = Session()
        ua = UserAgent()

        user_agent = ua.random
        session.headers.update({
            'User-Agent': user_agent
        })

        print(f"Using User-Agent: {user_agent}")

        response = session.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        links = []
        for item in soup.select('div.collectionItem'):
            link_tag = item.select_one('a[href]')
            title_tag = item.select_one('.workshopItemTitle')

            if link_tag and title_tag:
                link = link_tag['href']
                title = title_tag.text.strip()
                links.append((link, title))
                print(f"Processing addon: {title}")

        if links:
            file_name = 'addon_links.txt'
            with open(file_name, 'w') as file:
                for link, _ in links:
                    file.write(link + '\n')

            print(f"Found {len(links)} links and saved to '{file_name}'.")
        else:
            print("No links found.")

    except RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
