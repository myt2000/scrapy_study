
import requests
import random
import jsonpath
import json
import time
import urllib


class lagou_spider(object):
    def __init__(self):
        self.base_url = "https://www.lagou.com/jobs/positionAjax.json"
        self.headers = {

            # "Accept": "application/json, text/javascript, */*; q=0.01",
            # "Accept-Encoding": "gzip, deflate, br",
            # "Accept-Language": "zh-CN,zh;q=0.9",
            # "Connection": "keep-alive",
            # "Content-Length": "23",
            # "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            # 反爬字段1
            "Cookie": "_ga=GA1.2.141982794.1513838184; user_trace_token=20171221143624-43c39b96-e619-11e7-a409-525400f775ce; LGUID=20171221143624-43c39e32-e619-11e7-a409-525400f775ce; _gid=GA1.2.1911809108.1513838184; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAACEBACDG18079CDF31E87E380D301BE8438F20C8; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1513838184,1513904123; X_HTTP_TOKEN=d83dd14ec928f4dc04e403c7a7e0d6eb; _gat=1; LGSID=20171222165040-2ff5aea0-e6f5-11e7-9e03-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_navigation; SEARCH_ID=7436bebb4a7d40feb27929f3694161ee; LGRID=20171222165558-ed78c2e0-e6f5-11e7-a52a-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1513932959",
            # "Host": "www.lagou.com",
            # "Origin": "https://www.lagou.com",
            #  反爬字段 2
            "Referer": "https://www.lagou.com/jobs/list_PHP?px=default&city=%E4%B8%8A%E6%B5%B7",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
            # "X-Anit-Forge-Code": "0",
            # "X-Anit-Forge-Token": "None",
            # "X-Requested-With": "XMLHttpRequest",
        }
        self.search_name = input("请输入搜索专业:")
        self.city = input("请输入城市名字:")
        self.page = 1
        self.prox_list = [
            {"http": "mr_mao_hacker:sffqry9r@120.27.218.32:16816"},
            {}
        ]
        self.item_list = []

        # 标志什么时候结束抓取
        self.iswork = True

    # 请求数据
    def send_request(self):
        print("正在抓取第%d" % self.page)
        time.sleep(1)

        # 1.params
        params = {
            "px": "default",
            "city": self.city,
            "needAddtionalResult": "false",
            "isSchoolJob": "0"
        }
        # 2. data
        formdata = {
            "first": "false",
            "pn": self.page,
            "kd": self.search_name
        }

        # 在这里转码 只是为了获取字节长度
        formdata_str = urllib.urlencode(formdata)
        content_length = len(formdata)

        # 3.随机获取代理IP
        random_proxy = random.choice(self.prox_list)
        try:
            response = requests.post(self.base_url, params=params, data=formdata, headers=self.headers, proxies=random_proxy)
            data = response.json()
            return data
        except Exception as err:
            print(err)

    # 解析数据
    def analysis_data(self,data):
        # 1.取出 职位信息
        result_data = jsonpath.jsonpath(data, "$..result")[0]
        print(len(result_data))

        if not len(result_data):
            print("数据爬取结束😆😆...")
            self.iswork = False
            return

        # 2. 循环取出 字典数据 二次解析
        for content in result_data:
            dict = {}
            dict["positionName"] = content["positionName"]
            dict["salary"] = content["salary"]
            dict["education"] = content["education"]
            self.item_list.append(dict)


    # 写入本地
    def write_file(self):
        print("数据保存成功....")
        json.dump(self.item_list, open("2lagou.json", "w"))

    # 调度的方法
    def start_work(self):
       while self.iswork:
           data = self.send_request()
           self.analysis_data(data)
           self.page += 1

       self.write_file()


if __name__ == '__main__':
    tool = lagou_spider()
    tool.start_work()
