
import requests

class lagou_spider(object):
    def __init__(self):
        self.base_url = "https://www.lagou.com/jobs/positionAjax.json"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        # self.search_name = raw_input("请输入搜索专业:")

    # 请求数据
    def send_request(self):
        # 1.params
        params = {
            "px": "default",
            "city": "上海",
            "needAddtionalResult": "false",
            "isSchoolJob": "1"
        }
        # 2. data
        formdata = {
            "first": "false",
            "pn": "1",
            "kd": "PHP"
        }
        try:
            response = requests.post(self.base_url, params=params, data=formdata, headers=self.headers)
            data = response.content
            return data
        except Exception as err:
            print(err)

    # 解析数据

    # 写入本地
    def write_file(self, data):
        with open("2lagou.html", "w", encoding="utf-8") as f:
            f.write(data)

    # 调度的方法
    def start_work(self):
        data = self.send_request().decode("utf-8")
        self.write_file(data)


if __name__ == '__main__':
    tool = lagou_spider()
    tool.start_work()