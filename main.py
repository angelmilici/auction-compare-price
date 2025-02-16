import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Function to scrape auction site
def scrape_auction_site(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    upcoming_auctions = soup.find('div', id='list-page')
    # print(upcoming_auctions.prettify())
    for auction_data in upcoming_auctions.find_all('div', class_='auction-event-summary'):
        # print(auction_data.find('a'))
        link_item = auction_data.find('a')
        if link_item:
            print(link_item.get('href'))
    #     print("HERE: ", auction)
    #     print(auction.)
    
    return 0



# Main function
def main():
    auction_url = "https://www.wilsonsauctions.com/upcoming-auctions/"
    category = "art"  # Example category
    items = scrape_auction_site(auction_url)
    
    # for item in items:
    #     print(f"Item: {item['name']}, Price: {item['price']}, Bids: {item['bids']}")
        # sold_prices = search_ebay_sold_items(item['name'])
        # print(f"eBay Sold Prices: {sold_prices}")

if __name__ == "__main__":
    main()