# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ReviewshotelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    h_url = scrapy.Field() #url hotel
    h_reviewer_name = scrapy.Field() #reviewer name
    h_reviewer_id= scrapy.Field()
    h_comment_date = scrapy.Field()
    h_reviewer_address= scrapy.Field()
    h_reviewer_contribution = scrapy.Field()
    h_reviever_helpfulvote= scrapy.Field()
    h_rating = scrapy.Field()
    h_title_comment= scrapy.Field()
    h_content_comment= scrapy.Field()
    h_reviewer_staydate= scrapy.Field()
    h_triptype= scrapy.Field()
    pass
