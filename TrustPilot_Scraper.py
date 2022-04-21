from bs4 import BeautifulSoup
import time
import pandas as pd
import os
import requests

start_time = time.time()

review_name_list = []
review_location_list = []
review_number_list = []
review_header_list = []
review_content_list = []
review_stars_list = []
review_time_list = []

# Start of web scraping
for i in range(1, 101, 1):

    # ADD YOUR COMPANY NAME HERE 
    if i == 1:
        url = 'https://www.trustpilot.com/review/www.------ADD COMPANY NAME HERE------.com?stars=1&stars=2'
    else:
        url = 'https://www.trustpilot.com/review/www.------ADD COMPANY NAME HERE------.com?page=' + str(i) + '&stars=1&stars=2'

    html_source = requests.get(url)
    soup = BeautifulSoup(html_source.text, 'html.parser')        

    src = soup.find_all('div', {'class', 'paper_paper__1PY90 paper_square__lJX8a card_card__lQWDv card_noPadding__D8PcU styles_cardWrapper__LcCPA styles_show__HUXRb styles_reviewCard__9HxJJ'})
    for element in src:
        # Only accepts reveiws with content 
        if 'h2 class="typography_typography__QgicV typography_h4__E971J typography_color-black__5LYEn typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3 styles_reviewTitle__04VGJ"' and 'p class="typography_typography__QgicV typography_body__9UBeQ typography_color-black__5LYEn typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3"' not in str(element):
            pass
        else:
            # Scrape name
            review_name_list_src = element.find('div', {'class','typography_typography__QgicV typography_bodysmall__irytL typography_weight-medium__UNMDK typography_fontstyle-normal__kHyN3 styles_consumerName__dP8Um'})
            review_name_list.append(review_name_list_src.get_text())

            # Scrape location 
            review_location_list_src = element.find('span', {'class': 'typography_typography__QgicV typography_weight-inherit__iX6Fc typography_fontstyle-inherit__ly_HV', 'data-consumer-country-typography': 'true'})
            review_location_list.append(review_location_list_src.get_text())

            # Scrape number of reviews
            review_number_list_src = element.find('span', {'class': 'typography_typography__QgicV typography_weight-inherit__iX6Fc typography_fontstyle-inherit__ly_HV', 'data-consumer-reviews-count-typography': 'true'})
            review_number_list.append(review_number_list_src.get_text())

            # Scrape title of review
            review_header_list_src = element.find('a', {'class','link_internal__7XN06 link_wrapper__5ZJEx styles_linkwrapper__73Tdy'})
            review_header_list.append(review_header_list_src.get_text())

            # Scrape review content 
            review_content_list_src = element.find('p', {'class', "typography_typography__QgicV typography_body__9UBeQ typography_color-black__5LYEn typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3"})
            review_content_list.append(review_content_list_src.get_text())

            # Scrape number of stars
            review_stars_list_src = element.find('div', {'class', 'star-rating_starRating__4rrcf star-rating_medium__iN6Ty'})
            if 'Rated 1 out of 5 stars' in str(review_stars_list_src):
                review_stars_list.append(1)
            elif 'Rated 2 out of 5 stars' in str(review_stars_list_src):
                review_stars_list.append(2)
            else:
                print('ERROR HAS OCCURED')

            # Scrape date
            review_time_list_src = element.find('time')
            review_time_list.append(review_time_list_src['title'])

# Attatch to Pandas data frame and zip to csv file
df = pd.DataFrame(list(zip(review_name_list, review_location_list, review_number_list, review_time_list, review_stars_list, review_header_list, review_content_list,)),columns=['Name', 'Place', 'Number of Review(s)', 'Date', 'Stars', 'Title','Review'])
os.makedirs('/Users/jordanchen/Python', exist_ok=True)
df.to_csv('/Users/jordanchen/Python/------ADD COMPANY TITLE------_out.csv')

print("--- %s seconds ---" % (time.time() - start_time))

