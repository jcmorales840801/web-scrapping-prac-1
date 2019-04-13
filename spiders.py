import scrapy #se cargan todas las librerias a usar en el metodo
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from tipologia.items import tipologiaItem

class tipologiaSpider(CrawlSpider):
	name = 'tipologia' #este es el nombre del metodo que sera usado cuando se invoque la clase al momento de ejecutar el crawl scrapy 
	item_count = 0 #controla la cantidad de veces que ingresara a buscar productos, en este esta variable la usamos para inicializar
	allowed_domain = ['www.mercadolibre.com.mx'] #dominio el cual sera usado, es decir solamente va permitir informacion obtenida de este dominio #en la parte inferior sera controlada y en este ejercicio se uso un numero de 10
	start_urls = ['https://laptops.mercadolibre.com.mx/laptops/hp/notebook']

	rules = {
		# aca se aplican dos reglas que va tener este proceso la primer regla indica y controla la paginacion, es decir buscara el boton siguiente una vez terminar con los productos de la primera pagina y con esta regla buscara el boton siguiente para seguir con la proxima pagna que contendran
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li[@class="andes-pagination__button andes-pagination__button--next"]/a'))),
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//h2[contains(@class,"item__title")]/a')),
							callback = 'parse_item', follow = False)
	}

	def parse_item(self, response):
		ml_item = tipologiaItem()
		#los productos que se encuentran indicados en la clase items.py, deben indicarse aca con su respectivo xpath el cual
        #funcionara indicando exactamente donde esta la informacion que necesitamos para cada una de las variables.
        #se usa la opcion llamada normalize-space ya que en esta pagina los textos contienen demasiados espacios.
		ml_item['titulo'] = response.xpath('normalize-space(//h1[@class="item-title__primary "]/text())').extract_first()
		ml_item['modelo'] = response.xpath('normalize-space(//div/div[1]/div[1]/section[3]/div/section/ul/li[3]/span)').extract()
		ml_item['marca'] = response.xpath('normalize-space(//div/div[1]/div[1]/section[3]/div/section/ul/li[1]/span)').extract()
		ml_item['tipoPantalla'] = response.xpath('normalize-space(/html/body/main/div/div/div[1]/div[1]/section[1]/div/section[2]/ul/li[1]/span)').extract()
		ml_item['precio'] = response.xpath('normalize-space(//span[@class="price-tag-fraction"]/text())').extract()
		ml_item['condicion'] = response.xpath('normalize-space(//div[@class="item-conditions"]/text())').extract()
		ml_item['envio'] = response.xpath('normalize-space(//p[contains(@class, "shipping-method-title")]/text())').extract()
		ml_item['opiniones'] = response.xpath('normalize-space(//span[@class="review-summary-average"]/text())').extract()
		#imagenes del producto
		ml_item['image_urls'] = response.xpath('//figure[contains(@class, "gallery-image-container")]/a/img/@src').extract()
		ml_item['image_name'] = response.xpath('normalize-space(//h1[@class="item-title__primary "]/text())').extract_first()
		#info de la tienda o vendedor
		ml_item['vendedor_url'] = response.xpath('//*[contains(@class, "reputation-view-more")]/@href').extract()
		ml_item['tipo_vendedor'] = response.xpath('normalize-space(//p[contains(@class, "power-seller")]/text())').extract()
		self.item_count += 1
		if self.item_count > 10:
			raise CloseSpider('item_exceeded')
		yield ml_item
        #la condicion indicada anteriormente que hace las veces de contador para seguir con la siguiente pagina y terminar el raspado
        #en este caso sera cuando obtenga mas de 10 productos
