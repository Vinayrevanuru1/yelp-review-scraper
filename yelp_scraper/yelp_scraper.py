import requests
from bs4 import BeautifulSoup
import time
import random

def get_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve content from {url}, status code: {response.status_code}")
        return None

def extract_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', {'class': 'y-css-1iy1dwt', 'id': 'reviews'})
    return content

def extract_total_pages(html):
    soup = BeautifulSoup(html, 'html.parser')
    page_info = soup.find('div', {'class': 'y-css-xdax52'}).find('span', {'class': 'y-css-wfbtsu'}).text
    total_pages = int(page_info.split(' of ')[-1])
    return total_pages

def scrape_reviews(base_url, restaurant_name):
    page_number = 0
    step = 10  # Number of items per page
    all_content_html = []

    # Fetch the first page to get the total number of pages
    initial_url = f"{base_url}{page_number * step}"
    print(f"Fetching URL: {initial_url}")
    initial_html = get_html_content(initial_url)
    total_pages = 0

    if initial_html:
        total_pages = extract_total_pages(initial_html)

    print(f"Total number of pages: {total_pages}")

    while page_number < total_pages:
        url = f"{base_url}{page_number * step}"
        print(f"Fetching URL: {url}")
        html = get_html_content(url)

        if html:
            content = extract_content(html)
            if content:
                all_content_html.append(str(content))
                print(f"Page {page_number + 1}: Content extracted successfully.")
                page_number += 1  # Increment to fetch the next page
                time.sleep(random.randint(5, 7))
            else:
                print("No 'reviews' content found. Ending loop.")
                break
        else:
            break

    # Save all collected content to a file
    with open(f'{restaurant_name}_yelp_reviews.html', 'w') as file:
        for content in all_content_html:
            file.write(content)
            file.write('\n\n')
        print('Content saved successfully.')

    return all_content_html
