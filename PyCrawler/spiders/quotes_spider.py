import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "http://quotes.toscrape.com/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = "1"
        filename = "quotes-%s.html" % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log("Saved File %s" % filename)
