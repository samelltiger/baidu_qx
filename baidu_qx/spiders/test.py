import urllib.parse as parse

url = "http://huiyan.baidu.com/migration/cityrank.jsonp?dt=city&id=510300&type=move_in&date=20200101"
res = parse.parse_qs(url)
# res.
print(res)