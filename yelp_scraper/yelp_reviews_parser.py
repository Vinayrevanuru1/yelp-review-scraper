import pandas as pd
from bs4 import BeautifulSoup

def parse_reviews(all_content_html):
    all_reviews = []

    # Iterate through each HTML content in the list
    for html_content in all_content_html:
        soup = BeautifulSoup(html_content, 'html.parser')
        review_blocks = soup.find_all('li', {'class': 'y-css-1jp2syp'})  # Adjust the class if needed

        # Iterate over each review block in the current HTML content
        for block in review_blocks:
            # Safely extracting each element with checks
            reviewer_name = block.find('a', {'class': 'y-css-12ly5yx'}).text.strip() if block.find('a', {'class': 'y-css-12ly5yx'}) else None
            user_profile_url = block.find('a', {'class': 'y-css-12ly5yx'})['href'] if block.find('a', {'class': 'y-css-12ly5yx'}) else None
            user_profile_image_url = block.find('img', {'class': 'y-css-1k4vfmo'})['src'] if block.find('img', {'class': 'y-css-1k4vfmo'}) else None
            elite_status = 'Elite' in block.find('div', {'class': 'elite-badge__09f24__dykWK'}).text if block.find('div', {'class': 'elite-badge__09f24__dykWK'}) else 'No'
            reviewer_location = block.find('span', {'class': 'y-css-h9c2fl'}).text if block.find('span', {'class': 'y-css-h9c2fl'}) else None
            friends_count = int(block.find_all('div', {'aria-label': 'Friends'})[0].text.split()[-1]) if block.find_all('div', {'aria-label': 'Friends'}) else None
            reviews_count = int(block.find_all('div', {'aria-label': 'Reviews'})[0].text.split()[-1]) if block.find_all('div', {'aria-label': 'Reviews'}) else None
            photos_count = int(block.find_all('div', {'aria-label': 'Photos'})[0].text.split()[-1]) if block.find_all('div', {'aria-label': 'Photos'}) else None
            rating = float(block.find('div', {'role': 'img'})['aria-label'].split()[0]) if block.find('div', {'role': 'img'}) else None
            date_of_review = block.find('span', {'class': 'y-css-wfbtsu'}).text if block.find('span', {'class': 'y-css-wfbtsu'}) else None
            review_text = block.find('p', {'class': 'comment__09f24__D0cxf'}).text.strip() if block.find('p', {'class': 'comment__09f24__D0cxf'}) else None
            helpful_count = int(block.find_all('span', {'class': 'y-css-ihry0w'})[0].text) if block.find_all('span', {'class': 'y-css-ihry0w'}) else None
            thanks_count = int(block.find_all('span', {'class': 'y-css-ihry0w'})[1].text) if block.find_all('span', {'class': 'y-css-ihry0w'}) else None
            love_count = int(block.find_all('span', {'class': 'y-css-ihry0w'})[2].text) if block.find_all('span', {'class': 'y-css-ihry0w'}) else None
            oh_no_count = int(block.find_all('span', {'class': 'y-css-ihry0w'})[3].text) if block.find_all('span', {'class': 'y-css-ihry0w'}) else None

            # Append all information to the list
            all_reviews.append({
                'Reviewer Name': reviewer_name,
                'User Profile URL': user_profile_url,
                'User Profile Image URL': user_profile_image_url,
                'Elite Status': elite_status,
                'Reviewer Location': reviewer_location,
                'Friends Count': friends_count,
                'Reviews Count': reviews_count,
                'Photos Count': photos_count,
                'Rating': rating,
                'Date of Review': date_of_review,
                'Review Text': review_text,
                'Helpful Count': helpful_count,
                'Thanks Count': thanks_count,
                'Love Count': love_count,
                'Oh No Count': oh_no_count
            })

    # Convert the list of dictionaries into a pandas DataFrame
    reviews_df = pd.DataFrame(all_reviews)
    return reviews_df

def save_reviews_to_csv(reviews_df, restaurant_name):
    reviews_df.to_csv(f'{restaurant_name}_yelp_reviews.csv', index=False)
    print(f'Reviews saved to {restaurant_name}_yelp_reviews.csv')
