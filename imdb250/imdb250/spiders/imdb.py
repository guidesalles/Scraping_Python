import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        for indice,filmes in enumerate(response.css('.titleColumn')):
            yield {
                'nome_do_filme': filmes.css('.titleColumn a::text').get(),
                'Ano_do_filme': filmes.css('.secondaryInfo ::text').get()[1:-1],
                'avaliacao': response.css('strong::text')[indice].get(),
            }



