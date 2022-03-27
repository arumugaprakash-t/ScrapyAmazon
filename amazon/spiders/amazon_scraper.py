import scrapy

from ..items import AmazonItem

class AmazonScraperSpider(scrapy.Spider):
    name = 'amazon_scraper'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.in/gp/bestsellers/books/1318158031?ref_=Oct_d_obs_S&pd_rd_w=h42I9&pf_rd_p=63783fbe-7156-4f6f-9542-5efc5e74da13&pf_rd_r=ATVRZ8AK9DNX7V6SVHNJ&pd_rd_r=fe003763-7dd0-4072-a42b-7850b9fb7ce3&pd_rd_wg=jaosq']

    def parse(self, response):
        item = AmazonItem()

        #div = response.css('div.p13n-gridRow _p13n-zg-list-grid-desktop_style_grid-row__3Cywl')
        #for div_response in div:

        book_name = response.css(
            '.a-link-normal ._p13n-zg-list-grid-desktop_truncationStyles_p13n-sc-css-line-clamp-1__1Fn1y').css(
            '::text').extract()
        book_author = response.css(
            '.a-link-child ._p13n-zg-list-grid-desktop_truncationStyles_p13n-sc-css-line-clamp-1__1Fn1y').css(
            '::text').extract()
        book_price = response.css('span.p13n-sc-price::text').extract()
        # print(book_price)
        item['book_name'] = book_name
        item['book_author'] = book_author
        item['book_price'] = book_price

        yield item


