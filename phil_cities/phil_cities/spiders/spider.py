import scrapy

class PhilCitiesSpider(scrapy.Spider):
    name = 'phil_cities'
    start_urls = ['https://www.philatlas.com/cities.html']

    def parse(self, response):
        cities_selector = response.xpath('//section[@id="listCities"]//li/a')
        
        for city_selector in cities_selector:
            url = city_selector.xpath('./@href').get()
            city = city_selector.xpath('./text()').get()
            yield {'city': city, 'url': response.urljoin(url)}