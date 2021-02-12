# Sentimental-Analysis

Designed for someone who is looking for an influencer for a marketing campain.

It combine sentimental analysis for instagram and twitter.
Brands will not work with someone with a negative result because that would represent the brand.

I've tried multiple Instagram-scrapers. The most complete solution for python is Instagram-Scraper by arc298
https://github.com/arc298/instagram-scraper

The code for extract instagram comments looks like this (for users):
instagram-scraper <user to scrape> -u <your username> -p <your password> --comments --media-types none --maximum 80
  
The code for extract instagram comments looks like this (for tags):
instagram-scraper <user to scrape> -u <your username> -p <your password> --tags --comments --media-types none --maximum 80

In order to access twitter Api, you'd need to request access. It took 2 days for me. Once you have the keys, change line 13.

One you have the JSON file from instagram, just change line 5 from extract_comment_tags or extract_comment_tags.

Run "Influencers sentimental Analysis"


Enjoy results!



