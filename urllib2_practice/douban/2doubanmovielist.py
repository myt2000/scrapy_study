from urllib import request, response, parse

class DoubanSpider(object):
    def __init__(self):
        self.base_url = "https://movie.douban.com/j/chart/top_list?"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    def send_request(self):
        try:
            req = request.Request(self.base_url, headers=self.headers)
            resp = request.urlopen(req)
            if resp.getcode() == 200:
                return resp.read()
        except Exception as err:
            print(err)


    def write_file(self, data):
        with open("1doubanhome.html", "w", encoding="utf-8") as f:
            f.write(data)

    def start_work(self):
        data = self.send_request()
        self.write_file(data.decode("utf-8"))

if __name__ == "__main__":
    tool = DoubanSpider()
    tool.start_work()
