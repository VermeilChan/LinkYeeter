import requests
from bs4 import BeautifulSoup

def get_addons_links():
    url = input("Enter the full link to the Steam collection: ").strip()
    if not url:
        print("Invalid URL. Please try again.")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        links = []
        for item in soup.find_all('div', class_='collectionItemDetails'):
            link = item.find('a', href=True)
            if link:
                links.append(link['href'])

        if links:
            file_name = 'addon_links.txt'
            with open(file_name, 'w') as file:
                for link in links:
                    file.write(link + '\n')

            print(f"Found {len(links)} links and saved to '{file_name}'.")
        else:
            print("No links found.")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
