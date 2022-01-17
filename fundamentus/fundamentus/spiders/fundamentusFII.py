import scrapy



class FundamentusfiiSpider(scrapy.Spider):
    name = 'fundamentusFII'
    start_urls = ['http://www.fundamentus.com.br/fii_resultado.php?segmento=6']



    def parse(self, response):
        for indice, pagina in enumerate(response.css('td')):
            yield {
            'FII' : response.css('.tips a::text')[indice].get(),
            'cotacoes' : response.css('td:nth-child(3)::text')[indice].get(),
            'dy' : response.css('td:nth-child(5)::text')[indice].get(),
            'vacancia' : response.css('td:nth-child(13)::text')[indice].get()
            }