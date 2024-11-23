from scrapy.cmdline import execute

def executeSpider(spider):
    execute('scrapy crawl chinaairtest'.split())
def executenewspider():
    execute('scrapy genspider qqmusic https://u6.y.qq.com/cgi-bin/musics.fcg'.split())
if __name__ == '__main__':
    executenewspider()