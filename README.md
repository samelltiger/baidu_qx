# baidu_qx
 # 百度迁徙数据爬虫

### 一、基本功能介绍

本爬虫用于爬取全国**各个城市的迁入迁出**数据，以及某**各个省份的人数占该城市迁入或迁出人数百分比**。也就是百度迁徙页面中的这个部分：

![](https://github.com/samelltiger/baidu_qx/blob/master/img/baidu_qianxi.png?raw=true)

### 二、项目介绍

**使用的库**：

* datetime
* json
* scrapy
* urllib

__注意__：为了该项目能够在你的计算机中运行，请先安装以上库。

在当前项目中已经爬取了2020.1.1至1.2日的每个城市的迁入迁出数据；但是**省份所占百分比**只爬取了一个城市1.1日的数据。

### 三、使用方式

1. 首先**克隆**或**下载**该项目至你的本地
2. 安装python3.6或以上版本的python，并安装上述的库，使用 `pip install datetime json scrapy urlib`安装
3. 安装完成后进入到该项目的目录中 `cd baidu_qx` (注意是该项目根目录，不是里面有spiders目录的baidu_qx）
4. 执行 `scrapy crawl city_rank -o city_rank.csv` 爬取所有城市的迁徙数据
5. 执行 `scrapy crawl provincerank -o province_rank.csv` 爬取每个城市的迁徙人数的省份百分比数。

**注意**：可以在`baidu_qx/baidu_qx/spiders/city_rank`以及`baidu_qx/baidu_qx/spiders/provincerank`下修改你想要爬取的日期端。默认为 2020.1.1–2020.2.10.

### 四、字段说明

**city_rank**表的字段说明：

| city_name                  | 当前爬取的城市                    |
| -------------------------- | --------------------------------- |
| date                       | 哪一天的迁徙数据                  |
| inOrOUt_city               | 表示人来自或进入那个城市          |
| inOrout                    | 迁入（move_in）或迁出（move_out） |
| inOrout_city_province_name | inOrOUt_city所在的省份            |
| value                      | 值                                |

**provincerank**表的字段说明：

| city_name     | 爬取的城市                        |
| ------------- | --------------------------------- |
| date          | 日期                              |
| inOrout       | 迁入（move_in）或迁出（move_out） |
| province_name | 省份                              |
| value         | 值                                |

