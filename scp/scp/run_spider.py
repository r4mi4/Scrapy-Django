import scrapy.crawler as crawler 
from twisted.internet import reactor
from multiprocessing import Process, Queue
from scrapy.settings import Settings
from scrapy.utils.log import configure_logging
from .import settings as my_settings
from .pipelines import ScpPipeline

def run_spider(spider,url=None):
    def f(q):
        try:
            crawler_settings = Settings()
            crawler_settings.setmodule(my_settings)
            # configure_logging()
            runner = crawler.CrawlerRunner(settings=crawler_settings)
            deferred = runner.crawl(spider,url)
            deferred.addBoth(lambda _: reactor.stop())
            reactor.run()
            q.put(ScpPipeline.result)
        except Exception as e:
            q.put(e)
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    result = q.get()
    p.join()
    if result is not None:
        return result
    else:
        return 'NONE'
