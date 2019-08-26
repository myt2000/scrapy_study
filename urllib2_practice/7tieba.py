from urllib import request, response, parse
from User_Agent_list import USER_AGENT_LIST
import random
import time

class Tiebaspider(object):
    def __init__(self, tiebaname, start_page, end_page):
        self.base_url = "https://tieba.baidu.com/f?"
        self.name = tiebaname
        self.start = start_page
        self.end = end_page
        # self.headers = {"User-Agent": random.choice(USER_AGENT_LIST)}
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    # 发送请求
    def send_request(self, url):
        time.sleep(2)
        try:
            req = request.Request(url, headers=self.headers)
            resp = request.urlopen(req)
            if resp.getcode() == 200:
                return resp.read().decode('utf-8')
        except Exception as err:
            print(err)

    def write_file(self, data, page):
        filename = "Tieba/" + str(page) + "页数.html"
        print("正在下载中%s" % filename)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(data)


    def start_work(self):
        for page in range(self.start, self.end+1):
            pn = (page -1)*50
            params = {
                "kw" : self.name,
                # "ie": "utf-8",
                "pn": pn,
            }
            params_str = parse.urlencode(params)
            url = self.base_url + params_str
            print(url)
            data = self.send_request(url)
            self.write_file(data, page)

if __name__ == "__main__":

    tieba = input("请输入贴吧名字：")

    start_page = int(input("开始页："))

    end_page = int(input("结束页："))


    tool = Tiebaspider(tieba, start_page, end_page)
    tool.start_work()