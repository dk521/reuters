# -*- coding: utf-8 -*-
import scrapy


class ReutersSpider(scrapy.Spider):
    name = 'reuters'
    allowed_domains = ['in.reuters.com']
    start_urls = ['https://in.reuters.com/news/archive/rates-rss']

    def parse(self, response):
    
        for article in response.xpath("//div[@class='news-headline-list  ']/article[@class='story ']"):
            yield {
                'title' : article.xpath(".//div[@class='story-content']/a/h3/text()").get(),
                'url' : article.xpath(".//div[@class='story-content']/a/@href").get(),
                'press_release' : article.xpath(".//div[@class='story-content']/time[@class='article-time']/span/text()").get(),

            }

        next_page_link = response.xpath("//a[@class='control-nav-next']/@href").get()

        if next_page_link:
            
            # yield response.follow(url = next_page_link, callback = self.NewswireSpider)
            absolute_url = response.urljoin(next_page_link)



            print('\n\n\n\nTRUE3333\n\n\n')
            print(absolute_url)
            print(type(absolute_url))


            yield scrapy.Request(url = absolute_url, callback = self.parse)
            
