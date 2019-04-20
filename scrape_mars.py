


#import Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests


def init_browser(): 
# Choose the executable path to driver 
    executable_path = {'executable_path': '/Users/carlosroa/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

#create a mars dictionary to store the info and later use in mongo
mars_info = {}


# # NEWS
def scrape_mars_news():
    try: 

        # Visit the NASA news URL
        url = "https://mars.nasa.gov/news/"
        browser.visit(url)



        # Scrape page into soup
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')



        # save the most recent article, title and date
        article = soup.find("div", class_="list_text")
        news_paragraph = article.find("div", class_="article_teaser_body").text
        news_title = article.find("div", class_="content_title").text
        news_date = article.find("div", class_="list_date").text
        print(news_date)
        print(news_title)
        print(news_paragraph)
        return mars_info

    finally:

        browser.quit()


# # IMAGE
def scrape_mars_image():

    try:

        # Visit Mars Space Images through splinter module
        image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(image_url_featured)



        # HTML Object 
        html_image = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_image, 'html.parser')

        # Retrieve background-image url from style tag 
        featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

        # Website Url 
        main_url = 'https://www.jpl.nasa.gov'

        # Concatenate website url with scrapped route
        featured_image_url = main_url + featured_image_url

        # Display full link to featured image
        featured_image_url


        return mars_info

    finally:

        browser.quit()


# # Weather
def scrape_mars_weather():

    try:


        # visit the mars weather report twitter and scrape the latest tweet
        mars_weather_url = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(mars_weather_url)
        mars_weather_html = browser.html
        mars_weather_soup = BeautifulSoup(mars_weather_html, 'html.parser')

        tweets = mars_weather_soup.find('ol', class_='stream-items')
        mars_weather = tweets.find('p', class_="tweet-text").text
        print(mars_weather)
        return mars_info

    finally:

        browser.quit()


# # Facts
def scrape_mars_facts():

    try:

        # Visit Mars facts url 
        facts_url = 'http://space-facts.com/mars/'

        # Use Panda's `read_html` to parse the url
        mars_facts = pd.read_html(facts_url)

        # Find the mars facts DataFrame in the list of DataFrames as assign it to `mars_df`
        mars_df = mars_facts[0]

        # Assign the columns `['Description', 'Value']`
        mars_df.columns = ['Description','Value']

        # Set the index to the `Description` column without row indexing
        mars_df.set_index('Description', inplace=True)

        # Save html code to folder Assets
        mars_df.to_html()

        data = mars_df.to_dict(orient='records')  # Here's our added param..

        # Display mars_df
        mars_df

        return mars_info

    finally:

        browser.quit()
        


# # Hemisphere
def scrape_mars_hemisphere():

    try:

        # Visit hemispheres website through splinter module 
        hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemispheres_url)


        # HTML Object
        html_hemispheres = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_hemispheres, 'html.parser')

        # Retreive all items that contain mars hemispheres information
        items = soup.find_all('div', class_='item')

        # Create empty list for hemisphere urls 
        hemisphere_image_urls = []

        # Store the main_ul 
        hemispheres_main_url = 'https://astrogeology.usgs.gov'

        # Loop through the items previously stored
        for i in items: 
            # Store title
            title = i.find('h3').text
            
            # Store link that leads to full image website
            partial_img_url = i.find('a', class_='itemLink product-item')['href']
            
            # Visit the link that contains the full image website 
            browser.visit(hemispheres_main_url + partial_img_url)
            
            # HTML Object of individual hemisphere information website 
            partial_img_html = browser.html
            
            # Parse HTML with Beautiful Soup for every individual hemisphere information website 
            soup = BeautifulSoup( partial_img_html, 'html.parser')
            
            # Retrieve full image source 
            img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
            
            # Append the retreived information into a list of dictionaries 
            hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
            

        # Display hemisphere_image_urls
        hemisphere_image_urls

        return mars_info

    finally:

        browser.quit()








