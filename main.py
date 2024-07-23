import os
from yelp_scraper import scrape_reviews
from yelp_reviews_parser import parse_reviews, save_reviews_to_csv

base_url = ''  # get the base URL from the Yelp page make sure to include the start= at the end just like this
restaurant_name = ''  # enter the name of the restaurant here

if __name__ == "__main__":
    all_content_html = scrape_reviews(base_url, restaurant_name)
    reviews_df = parse_reviews(all_content_html)
    save_reviews_to_csv(reviews_df, restaurant_name)
