# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from time import sleep
from .article import ArticleSpider
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from crochet import setup

# setup()

class ReutersSpider(scrapy.Spider): 
    name = 'reuters'
    allowed_domains = ['in.reuters.com']

    # here, list down the URLS for dynamic Scrapping
    start_urls = ['https://in.reuters.com/news/archive/rates-rss']


    def parse(self, response):
    

        for article in response.xpath("//div[@class='news-headline-list  ']/article[@class='story ']"):

            print("\n\nNew Article")        
            yield ({
                # mention the xpath for the element to be captured.
                'title' : article.xpath(".//div[@class='story-content']/a/h3/text()").get(),
                'url' : article.xpath(".//div[@class='story-content']/a/@href").get(),
                'press_release' : article.xpath(".//div[@class='story-content']/time[@class='article-time']/span/text()").get(),
            })  
            
            # article_url = response.urljoin(article.xpath(".//div[@class='story-content']/a/@href").get())
            # print("Article Url: ", article_url, "\n\n")
            # yield scrapy.Request(url = article_url, callback = self.parse_article, priority=1)


        # sleep(5)
        # next_page_link = response.xpath("//a[@class='control-nav-next']/@href").get()
        # if next_page_link:
            
        #     # yield response.follow(url = next_page_link, callback = self.NewswireSpider)
        #     absolute_url = response.urljoin(next_page_link)
            
        #     yield scrapy.Request(url = absolute_url, callback = self.parse)
        

            
    def parse_article(self, response):
        
        for article in response.xpath("//div[@class='StandardArticle_inner-container']"):

            content_list = []
            for i in response.xpath("//div[@class='StandardArticleBody_body']/p"):
                content_list.append(i.xpath('string()').extract()[0])
            
            content = ' '.join(content_list)
            
            yield {
                'title' : article.xpath(".//h1/text()").get(),
                'content' : content,
                'author_editor' : article.xpath(".//div[@class='Attribution_attribution']/p/text()").get()
            }
            print("\n<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")



# configure_logging()
# runner = CrawlerRunner()

# @defer.inlineCallbacks
# def crawl():
#     yield runner.crawl(ReutersSpider)
#     yield runner.crawl(ArticleSpider)
#     reactor.stop()

# crawl()
# reactor.run()

# cmd : scrapy crawl reuters -o crawlers/spiders/output.csv

