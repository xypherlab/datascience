import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = "best_movies"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/?sort=rk,asc&mode=simple&page=1"]

    rules = (Rule(LinkExtractor(restrict_xpaths="//tbody[@class='lister-list']/tr/td[2]/a"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        # item = {}
        # #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        # #item["name"] = response.xpath('//div[@id="name"]').get()
        # #item["description"] = response.xpath('//div[@id="description"]').get()
        # return item
        # print(response.url)
        yield{
            'title':response.xpath("//div[@class='sc-b5e8e7ce-1 kNhUtn']/h1/text()").get,
            'year':response.xpath("//div[@class='sc-b5e8e7ce-2 AIESV']/ul/li[1]/a/text()").get,
            # 'duration':response.xpath("//div[@class='sc-b5e8e7ce-1 kNhUtn']/h1/text()").get,
            'genre':response.xpath("//div[@class='ipc-chip-list__scroller']/a/span/text()").get,
            'rating':response.xpath("//div[@class='sc-7ab21ed2-2 gWdbeG']/span/text()").get,
            'movie_url':response.url
        }
