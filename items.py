import scrapy

#nombre del proyecto
class tipologiaItem(scrapy.Item):
    # se definen todos los campos que se esperan raspar de la pagina,
    #estos fueron separados en tres grupos, producto, vendedor e imagenes

    #info de producto
    titulo = scrapy.Field()
    modelo = scrapy.Field()
    marca = scrapy.Field()
    tipoPantalla = scrapy.Field()
    precio = scrapy.Field()
    condicion = scrapy.Field()
    envio = scrapy.Field()
    opiniones = scrapy.Field()

    #imagenes
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_name = scrapy.Field()

    #info de la tienda o vendedor
    vendedor_url = scrapy.Field()
    tipo_vendedor = scrapy.Field()
    