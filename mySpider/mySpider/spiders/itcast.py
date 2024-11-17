import scrapy
from mySpider.items import ItcastItem
import logging


class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = ("https://www.itheima.com/teacher.html",)

    def parse(self, response):
        # 存放老师信息的集合
        items = []
        for each in response.xpath("//div[@class='li_txt']"):
                item = ItcastItem()
                # 提取字段
                name = each.xpath("h3/text()").get()
                title = each.xpath("h4/text()").get()
                info = each.xpath("p/text()").get()

                item['name'] = name
                item['title'] = title
                item['info'] = info

                items.append(item)

        # 使用 Scrapy 的日志记录
        logging.debug(f'Response: {items}')
        return items
