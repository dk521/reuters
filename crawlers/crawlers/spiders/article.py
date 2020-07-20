# -*- coding: utf-8 -*-
import scrapy


class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['in.reuters.com']

    # Replace this for new links to be crawled
    start_urls = ['http://in.reuters.com/article/us-china-economy-lpr/china-keeps-lending-benchmark-lpr-steady-for-third-month-as-expected-idINKCN24L04R']

    def parse(self, response):
        

        


        for article in response.xpath("//div[@class='StandardArticle_inner-container']"):

            content_list = []
            for i in response.xpath("//div[@class='StandardArticleBody_body']/p"):
                print(i.xpath('string()').extract()[0])
                print(type(i.xpath('string()').extract()))
                content_list.append(i.xpath('string()').extract()[0])
            
            content = ' '.join(content_list)

            yield {
                'title' : article.xpath(".//h1/text()").get(),
                'content' : content,

            }

