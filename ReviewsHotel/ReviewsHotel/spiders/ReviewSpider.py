import scrapy
from ..items import ReviewshotelItem
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings
import time

class ReviewspiderSpider(scrapy.Spider):
    name = 'ReviewSpider'
    allowed_domains = ['tripadvisor.com']
    start_urls = [
'https://www.tripadvisor.com/Hotel_Review-g293926-d4357913-Reviews-Hue_Serene_Palace_Hotel-Hue_Thua_Thien_Hue_Province.html',


    ]

    def parse(self, response):
        settings = get_project_settings()
        driver_path =settings['CHROME_DRIVER_PATH']
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('disable-popup-blocking')
        options.add_argument('--log-level=1')
        driver = webdriver.Chrome(driver_path, options=options) #bat chrome len
        driver.get(response.url) #duyet trang web
        time.sleep(3)
        #driver.find_element_by_xpath('//button[@id="onetrust-accept-btn-handler"]').click()
        #time.sleep(3)
        #duyet toan bo trang web
        while True:
            h_url= driver.current_url
            #duyet toan bo noi dung cai reveview 10 cai
            h_reviewer_name = "NA"
            h_reviewer_id = "NA"
            h_comment_date = "NA"
            h_reviewer_address = "NA"
            h_reviewer_contribution = "NA"
            h_reviever_helpfulvote = "NA"
            h_rating = "NA"
            h_title_comment = "NA"
            h_content_comment = "NA"
            h_reviewer_staydate = "NA"
            h_triptype = "NA"
            #click vo nut expand
            try:
                driver.find_element_by_xpath('//div[@data-test-target="expand-review"]').click()
                time.sleep(3)
            except:
                item= ReviewshotelItem()
                item['h_url']= h_url
                item['h_reviewer_name'] = h_reviewer_name
                item['h_reviewer_id'] = h_reviewer_id
                item['h_comment_date'] = h_comment_date
                item['h_reviewer_address'] = h_reviewer_address
                item['h_reviewer_contribution'] = h_reviewer_contribution
                item['h_reviever_helpfulvote'] = h_reviever_helpfulvote
                item['h_rating'] = h_rating
                item['h_title_comment'] = h_title_comment
                item['h_content_comment'] = h_content_comment
                item['h_reviewer_staydate'] = h_reviewer_staydate
                item['h_triptype'] = h_triptype
                yield item

            #Lay lan luot tung thong tin
            try:
                comments= driver.find_elements_by_xpath('//div[@data-test-target="HR_CC_CARD"]')
                num_comment_items= min(len(comments), 10)
            except:
                item= ReviewshotelItem()
                item['h_url']= h_url
                item['h_reviewer_name'] = h_reviewer_name
                item['h_reviewer_id'] = h_reviewer_id
                item['h_comment_date'] = h_comment_date
                item['h_reviewer_address'] = h_reviewer_address
                item['h_reviewer_contribution'] = h_reviewer_contribution
                item['h_reviever_helpfulvote'] = h_reviever_helpfulvote
                item['h_rating'] = h_rating
                item['h_title_comment'] = h_title_comment
                item['h_content_comment'] = h_content_comment
                item['h_reviewer_staydate'] = h_reviewer_staydate
                item['h_triptype'] = h_triptype
                yield item  

            for j in range(num_comment_items):
                try:
                    h_reviewer_name= comments[j].find_element_by_xpath('.//a[@class="ui_header_link bPvDb"]').text
                except:   
                    h_reviewer_name="NA" 
                try:
                    h_reviewer_id = comments[j].find_element_by_xpath('.//a[@class="ui_header_link bPvDb"]').get_attribute('href')
                except:
                    h_reviewer_id = "NA"
                try:
                    h_comment_date = comments[j].find_element_by_xpath('.//div[@class="bcaHz"]/span').text
                    h_comment_date = h_comment_date.replace(h_reviewer_name,"")
                    h_comment_date = h_comment_date.replace(" wrote a review ","")
                except:
                    h_comment_date = "NA"
                try:
                    h_reviewer_address = comments[j].find_element_by_xpath('.//span[@class="default ShLyt small"]').text
                except:
                    h_reviewer_address = "NA"
                try:
                    h_reviewer_contribution = comments[j].find_element_by_xpath('.//span[@class="ckXjS"]').text
                except:
                    h_reviewer_contribution = "NA"
                try:
                    h_reviever_helpfulvote = comments[j].find_elements_by_xpath('.//span[@class="ckXjS"]')[1].text
                except:
                    h_reviever_helpfulvote = "NA"
                try:
                    h_rating = comments[j].find_element_by_xpath('.//div[@class="emWez F1"]/span').get_attribute('class')
                    h_rating = h_rating.replace("ui_bubble_rating bubble_","")
                except:
                    h_rating = "NA"
                try:
                    h_title_comment = comments[j].find_element_by_xpath('.//a[@class="fCitC"]').text
                except:
                    h_title_comment = "NA"
                try:
                    h_content_comment = comments[j].find_element_by_xpath('.//q[@class="XllAv H4 _a"]').text
                except:
                    h_content_comment = "NA"
                try:
                    h_reviewer_staydate = comments[j].find_element_by_xpath('.//span[@class="euPKI _R Me S4 H3"]').text
                    h_reviewer_staydate= h_reviewer_staydate.replace("Date of stay: ","")
                except:
                    h_reviewer_staydate = "NA"
                try:
                    h_triptype = comments[j].find_element_by_xpath('.//span[@class="eHSjO _R Me"]').text
                    h_triptype = h_triptype.replace("Loại chuyến đi: ","")
                except:
                    h_triptype = "NA"   

                item= ReviewshotelItem()
                item['h_url']= h_url
                item['h_reviewer_name'] = h_reviewer_name
                item['h_reviewer_id'] = h_reviewer_id
                item['h_comment_date'] = h_comment_date
                item['h_reviewer_address'] = h_reviewer_address
                item['h_reviewer_contribution'] = h_reviewer_contribution
                item['h_reviever_helpfulvote'] = h_reviever_helpfulvote
                item['h_rating'] = h_rating
                item['h_title_comment'] = h_title_comment
                item['h_content_comment'] = h_content_comment
                item['h_reviewer_staydate'] = h_reviewer_staydate
                item['h_triptype'] = h_triptype
                yield item    
            #press next button
            try:
                driver.find_element_by_xpath('//a[@class="ui_button nav next primary "]').click()
                time.sleep(3)
            except:
                break
        #khi ket thuc crawl hoan tat
        driver.quit()
        pass
