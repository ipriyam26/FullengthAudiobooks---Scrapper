import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

links=[]

class AudiobooksSpider(CrawlSpider):
    name = 'audiobooks'
    allowed_domains = ['fulllengthaudiobooks.com']
    start_urls = ['https://fulllengthaudiobooks.com']

    rules = (
        Rule(LinkExtractor(allow=r'/series',follow=True)),
        Rule(LinkExtractor(allow=r'/author',follow=True)),
        Rule(LinkExtractor(allow=r'/books',follow=True)),
        Rule(LinkExtractor(allow=r'/page',follow=True)),
        Rule(LinkExtractor(deny=links), callback='parse_item',follow=True),
        
    )

    def parse_item(self, response):
        link = response.url
        title = response.css(".post-title::text").extract_first()
        try:
            author = response.css(".meta-tags a::text").extract_first()
        except:
            author = "Unknown"
        try:    
            image_url = response.css("img::attr(src)").extract()[1]    
        except:
            image_url = "Null"        
        links.append(link)
        yield {
            'title' : title,
            'link' : link,
            'author' : author,
            'image_url' : image_url
        }
