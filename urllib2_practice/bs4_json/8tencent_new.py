import requests
from bs4 import BeautifulSoup
import time
import json

class Tencent_job():
    def __init__(self):
        self.base_url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1567329452611&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=5010&language=zh-cn&area="
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.item_list = []

    def send_request(self, url):
        time.sleep(2)
        response = requests.get(url, headers=self.headers).content
        return response

    def write_files(self):
        data_str = json.dumps(self.item_list)
        with open("8tencent.json", "w", encoding="utf-8") as f:
            f.write(data_str)

    def start_work(self):
        data = self.send_request(self.base_url).decode("utf-8")
        data =json.loads(data)
        self.item_list = data["Data"]["Posts"]

        self.write_files()


if __name__ == "__main__":
    tool = Tencent_job()
    tool.start_work()