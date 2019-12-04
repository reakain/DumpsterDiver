# -*- coding: utf-8 -*-
import scrapy


class TrashSpider(scrapy.Spider):
    name = 'trash_spider'
    start_urls = [
            'http://quotes.toscrape.com/'
        ]
    visited_urls = ['http://quotes.toscrape.com/']
    
    def parse(self, response):
        f=open("urls.txt", "a+")
        f.write(response.url + "\n")
        f.close()
        for new_url in response.css('a::attr(href)'):
            if new_url is not None:
                self.log('Found new url %s' % new_url)
                if new_url not in self.visited_urls:
                    self.visited_urls.append(new_url)
                    yield response.follow(new_url, callback=self.parse)

