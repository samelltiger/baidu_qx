import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://segmentfault.com/blog/sown',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('section.stream-list__item'):
            print(quote.css('h2.title a::text').extract_first())
            print(quote.css('h2.title a::attr(href)').extract_first())