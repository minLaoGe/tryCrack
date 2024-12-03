from scrapy.cmdline import execute

def excutechinaair():
    execute('scrapy crawl chinaairtest'.split())

def excuteQQmusic():
    execute('scrapy crawl chinaairtest'.split())

## start project
def createQQMusciProject():
    execute('scrapy startproject qqMusic'.split())

## start qqmusciProject
def qqMusicProject():
    execute('scrapy genspider qqMusic www.qqmusic.com'.split())
## meijutt
def meijutttProject():
    execute('scrapy crawl  meijuttt --loglevel DEBUG'.split())

if __name__ == '__main__':
    meijutttProject()