import scrapy
from mySpider.items import MyspiderItem

# Use 'scrapy crawl itcast' to run

class Opp2Spider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]

    def parse(self, response):
        # context = response.xpath('/html/head/title/text()')
        # title = context.extract_first()
        # pass
        items = []
        for each in  response.xpath("//div[@class='li_txt']"):
            item = MyspiderItem()
            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            items.append(item)

        return items
    

    # 4 ways to store datas
    # scrapy crawl itcast -o teachers.json
    # scrapy crawl itcast -o teachers.jsonl
    # scrapy crawl itcast -o teachers.csv
    # scrapy crawl itcast -o teachers.xml