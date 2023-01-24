import scrapy

class QuotesSpider(scrapy.Spider):
    '''
    Tutorial Part 1. How to parse html.
    '''
    name = "quotes"
    # You don't need the start_requests method if you have start_urls
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        # I.e. 1 or 2
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        # Write response to file.
        with open(filename, 'wb') as f:
            f.write(response.body)
        # Should see in console e.g.: [quotes] DEBUG: Saved file quotes-1.html
        self.log(f'Saved file {filename}')

# Run 'scrapy crawl quotes' to write to html file
# Run 'scrapy shell "https://quotes.toscrape.com/page/1/"' to enter interaction shell
    # CSS: Get seletors and elements as follows
        # response.css('title') --> Get Selector
        # response.css('title::text').get(), --> Get actual text within tags. Will return none if nothing
        # response.css('title::text')[0].get() --> Get element within list, return error if nothing
        # response.css('title').getall() --> Return list of all selectors
        # response.css('title::text').getall() --> Return list of all text
        # response.css('title::text').re(r'Quotes.*') --> Returns everything starting with 'Quotes'
        # response.css('title::text').re(r'Q\w+') --> Return list of all words starting with Q
        # response.css('title::text').re(r'(\w+) to (\w+)') --> Return list of all words as elements
    # Alternative to using CSS, xPath
        # response.xpath('//title') --> Returns selector
        # response.xpath('//title/text()').get() --> Get actual text