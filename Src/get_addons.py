from os import path
from re import match, search
from bs4 import BeautifulSoup
from requests import Session, exceptions

def get_addons_links():
    url = input("Enter the full link to the Steam collection: ").strip()
    
    pattern = r'^https://steamcommunity\.com/(workshop|sharedfiles)/filedetails/\?id=\d+(&.*)?$'
    if not match(pattern, url):
        print("Invalid URL format. Please enter a valid Steam collection URL.")
        return

    collection_id = search(r'id=(\d+)', url).group(1)
    print("Fetching collection page...")

    session = Session()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    session.headers.update({'User-Agent': user_agent})
    print(f"Using User-Agent: {session.headers['User-Agent']}")

    try:
        response = session.get(url, timeout=30)
        response.raise_for_status()
    except exceptions.HTTPError as e:
        print(f"HTTP error: {e}. Collection doesn't exist or unable to access.")
        return
    except exceptions.ConnectionError:
        print("Unable connect to Steam. Check your internet connection.")
        return
    except exceptions.Timeout:
        print("The request timed out. connection might be slow or unstable.")
        return
    except exceptions.RequestException as e:
        print(f"An error occurred while fetching the page: {e}.")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    links = [
        (link_tag['href'], title_tag.text.strip())
        for item in soup.select('div.collectionItem')
        if (link_tag := item.select_one('a[href]')) and (title_tag := item.select_one('.workshopItemTitle'))
    ]

    if links:
        file_name = f'addon_links-{collection_id}.txt'
        if path.exists(file_name):
            while True:
                overwrite = input(f"'{file_name}' already exists. Overwrite? (y/n): ").strip().lower()
                if overwrite == 'y':
                    print("Overwriting file...")
                    break
                elif overwrite == 'n':
                    print("File was not overwritten.")
                    return
                else:
                    print("Please enter 'y' or 'n'.")
        try:
            with open(file_name, 'w') as file:
                file.write('\n'.join(link for link, _ in links) + '\n')
            print(f"Found {len(links)} links and saved to '{file_name}'.\n")
        except IOError as e:
            print(f"Couldn't save the file: {e}. Do you have permission to write here?")
    else:
        print("Unable to find any addons in this collection. Could be a hidden collection or no addons in it.")
