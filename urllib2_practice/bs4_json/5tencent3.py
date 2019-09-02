import requests
from bs4 import BeautifulSoup
import json
import time


class tencent_job(object):
    def __init__(self):
        self.base_url = "http://hr.tencent.com/position.php?"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.item_list = []
        self.page = 0

    def send_request(self, url, params={}):
        time.sleep(2)
        try:
            response = requests.get(url, params=params, headers=self.headers).content
            return response
        except Exception as err:
            print(err)

    # 解析数据
    def analysis_data(self, data):
        # 1.转换类型
        soup = BeautifulSoup(data, "lxml")

        # 2.获取标签--列表
        data_list = soup.select(".even,.odd")

        # 3.将里面的每一行的数据 提取出来
        for tr in data_list:
            dict = {}
            dict["work_name"] = tr.select("td a")[0].get_text()
            dict["work_type"] = tr.select("td")[1].get_text()
            dict["work_count"] = tr.select("td")[2].get_text()
            dict["work_place"] = tr.select("td")[3].get_text()
            dict["work_time"] = tr.select("td")[4].get_text()

            self.item_list.append(dict)

        # 4.获取到 最大的页数
        a_list = soup.select(".pagenav a")
        all_num = a_list[-2].get_text()
        print(all_num)
        return all_num

    # 写入本地文件
    def write_file(self):
        # 将列表转换成 字符串str
        data_str = json.dumps(self.item_list)
        with open("5tencent.json", "w") as f:
            f.write(data_str)

    # 调度方法
    def start_work(self):

       # 1.获取第一页的数据 --> 最大的页数
       params = {
           "keywords": "python",
           "tid": "0",
           "lid": "2156",
           "start": "0",
       }
       # 2.发送请求
       data = self.send_request(self.base_url, params=params)

       # 3.解析数据 -->返回 判断是都是最后一页的条件
       all_num = self.analysis_data(data)

       # 4.根据 最大页数 循环请求数据
       all = (int(all_num) + 1) *10
       for page in range(10,all,10):
           params = {
               "keywords": "python",
               "tid": "0",
               "lid": "2156",
               "start": page,
           }
           print(page)
           # 2.发送请求
           data = self.send_request(self.base_url, params=params)

           # 3.解析数据 -->返回 判断是都是最后一页的条件
           self.analysis_data(data)

       self.write_file()



if __name__ == '__main__':
    tool = tencent_job()
    tool.start_work()
    # 1.发送请求

    # 2.解析数据

    # 3.写入本地文件

    # 4.调度方法
