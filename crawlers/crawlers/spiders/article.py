# -*- coding: utf-8 -*-
import scrapy
import pandas as pd



class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['in.reuters.com']

    # Replace this for new links to be crawled
    # start_urls = ['http://in.reuters.com/article/us-china-economy-lpr/china-keeps-lending-benchmark-lpr-steady-for-third-month-as-expected-idINKCN24L04R'] 
        
    def start_requests(self):

        df = pd.read_csv('output.csv')        
        print(df.url.head())
        urls = []
        for i in df.url:
            urls.append('http://in.reuters.com'+str(i))
        
        # for i in urls:
        #     print(i,"\n\n")

        start_urls = reversed( urls )
        return [ scrapy.Request(url = start_url) for start_url in start_urls ]

    def parse(self, response):
        for article in response.xpath("//div[@class='StandardArticle_inner-container']"):
            print("\n\n\n")
            content_list = []
            for i in response.xpath("//div[@class='StandardArticleBody_body']/p"):
                #print(i.xpath('string()').extract()[0])
                #print(type(i.xpath('string()').extract()))
                content_list.append(i.xpath('string()').extract()[0])
            
            content = ' '.join(content_list)
            yield {
                'title' : article.xpath(".//h1/text()").get(),
                'content' : content,
                'author_editor' : article.xpath(".//div[@class='Attribution_attribution']/p/text()").get(),
                'timestamp' : article.xpath(".//div[@class='ArticleHeader_date']/text()").get(),
                'url' : response.request.url
            }
            
            
            
# date
# url
# publisher
# 

    
        


