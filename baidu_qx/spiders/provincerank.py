import scrapy
import json
import urllib.parse as parse
from config import city_dict
from baidu_qx.items import ProvinceRankItem
from common import datelist


# print(city_dict)
class mingyan(scrapy.Spider):  # 需要继承scrapy.Spider类

    name = "provincerank"  # 定义蜘蛛名

    def start_requests(self):  # 由此方法通过下面链接爬取页面
        url = "http://huiyan.baidu.com/migration/provincerank.jsonp?dt=city&id={0}&type=move_in&date={1}"

        # 修改起始日期
        date = datelist((2020, 1, 1), (2020, 2, 11))

        # 定义爬取的链接
        urls = [url.format(city, d) for d in date for city in city_dict.keys()]

        for url in urls[:2]:
            yield scrapy.Request(url=url, callback=self.parse)  # 爬取到的页面如何处理？提交给parse方法处理
            yield scrapy.Request(url=url.replace("move_in", "move_out"), callback=self.parse)  # 爬取到的页面如何处理？提交给parse方法处理

    def parse(self, response):
        # print(response.text)
        json_dict = json.loads(response.text[3:-1], encoding='utf-8')['data']['list']
        # print(json_dict)
        url = response.url
        res = parse.parse_qs(url)
        date = res['date'][0]
        eara = city_dict[res['id'][0]]
        type_str = res['type'][0]

        item = ProvinceRankItem()
        for data in json_dict:
            item["city_name"] = eara
            item["province_name"] = data['province_name']
            item["value"] = data['value']
            item["inOrout"] = type_str
            item["date"] = date
            yield item
