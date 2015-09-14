import scrapy

from chem_spider.items import ArticleItem


class ArticleSpider(scrapy.Spider):
    name = "article_spider"
    allowed_domains = ["pubs.acs.org"]

    # Get the keyword from the user from the command line
    def __init__(self, keyword=''):
        self.start_urls = ['http://pubs.acs.org/action/doSearch?text1=%s&field1=AllField' % keyword]

    # On search results page
    # search and follow the search result links
    def parse(self, response):
        for url in response.css('div.titleAndAuthor a').xpath('@href').extract() :
            yield scrapy.Request(response.urljoin(url), self.parse_article_page)

    # On article page
    # scrape the title, authors, number of citings
    # and output (yield) the item
    def parse_article_page(self, response):
        item = ArticleItem()
        item['title'] = response.css("h1.articleTitle").xpath("text()").extract()[0]
        item['authors'] = ", ".join(response.css("div#authors a").xpath("text()").extract())
        item['number_of_citings'] = response.css("div.cited-content p a").xpath("text()").extract_first()[9:].split(" ")[0]
        yield item
