
from time import sleep
from subprocess import call
call(['scrapy', 'crawl', 'reuters', '-o', 'output.csv'])
sleep(5)
call(['scrapy', 'crawl', 'article', '-o', 'article_ouput.csv'])


