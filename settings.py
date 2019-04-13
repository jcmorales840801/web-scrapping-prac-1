
BOT_NAME = 'tipologia'

SPIDER_MODULES = ['tipologia.spiders']
NEWSPIDER_MODULE = 'tipologia.spiders'


#CSV IMPORTACION
ITEM_PIPELINES = {'tipologia.pipelines.tipologiaPipeline': 500,
					'tipologia.pipelines.tipologiaImagenesPipeline': 600, }

# valida las reglas del robot y obedece las reglas que este tiene si se encuentra en true
ROBOTSTXT_OBEY = True

#Imagenes
IMAGES_STORE = (r"C:\Users\Esalazar\tutorial\tipologia")
DOWNLOAD_DELAY = 2
