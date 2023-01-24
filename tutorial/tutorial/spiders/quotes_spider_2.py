import scrapy

class QuotesSpider(scrapy.Spider):
    '''
    Tutorial Part 2. Retrieve quotes.
    '''
    name = "quotes2"
    # You don't eed the start_requests method if you have start_urls
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

# scrapy shell 'https://quotes.toscrape.com' to see what code we need
    #  response.css("div.quote") --> List of selectors
    #  quote = response.css("div.quote")[0] --> Assign a particular selector element
    #  text = quote.css("span.text::text").get() --> Get the actual text within this element
    #  author = quote.css("small.author::text").get() --> Get author
    #  tags = quote.css("div.tags a.tag::text").getall() --> Get list of tags
# scrapy crawl quotes2
# scrapy crawl quotes2 -O quotes.json --> Store quotes in json file
# scrapy crawl quotes2 -O quotes.json1 --> Store quotes in json stream file