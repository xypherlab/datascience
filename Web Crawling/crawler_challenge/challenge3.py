from scrapy import signals
from scrapy.spiders import Spider

class MySpider(Spider):
    name = 'myspider'
    # other spider settings

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.table_items = []

    def parse(self, response):
        # parse the table items and append them to self.table_items

    def close(self, reason):
        if reason == 'finished':
            # sort the items in the same order as they appear in the table
            sorted_items = []
            for item in self.table_items:
                sorted_item = {}
                for field in self.item_fields:
                    sorted_item[field] = item.get(field)
                sorted_items.append(sorted_item)
            # yield the sorted items
            for item in sorted_items:
                yield item

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super().from_crawler(crawler, *args, **kwargs)
        spider.item_fields = [field_name for field_name in spider.item_fields]
        crawler.signals.connect(spider.spider_idle, signal=signals.spider_idle)
        return spider

    def spider_idle(self):
        if not self.crawler.engine.slot.scheduler.total_enqueued:
            self.logger.info('No more URLs to scrape. Sorting and yielding items...')
            self.crawler.engine.close_spider(self, 'finished')
