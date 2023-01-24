import scrapy


class QuotesSpider(scrapy.Spider):
    '''
    Tutorial Part 3. Go to next page and get all quotes from there
    '''
    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

# scrapy shell 'https://quotes.toscrape.com' to see what code we need
    #   response.css('li.next a').get() --> Get the 'next button for next page'
    #   response.css('li.next a::attr(href)').get() --> We only want the href. E.g. '/page/2/'
    #   response.css('li.next a').attrib['href'] --> Alternative to get href. E.g. '/page/2/'
# scrapy crawl quotes3
# scrapy crawl quotes3 -O quotes.json --> Store quotes in json file
# scrapy crawl quotes3 -O quotes.json1 --> Store quotes in json stream file