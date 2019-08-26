from urllib import request, response, parse

class DoubanSpider(object):
    def __init__(self):
        self.base_url = "https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action="
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    def send_request(self, url):
        try:
            req = request.Request(url, headers=self.headers)
            resp = request.urlopen(req)
            if resp.getcode() == 200:
                return resp.read()
        except Exception as err:
            print(err)


    def write_file(self, data):
        with open("2doubanmovielist.html", "w", encoding="utf-8") as f:
            f.write(data)

    def start_work(self):
        params = {
            "type": "5",
            "interval_id": "100:90",
            "action": "",
            "start": "0",
            "limit": "20",
                  }
        params_str = parse.urlencode(params)
        url = self.base_url + params_str
        data = self.send_request(url)
        self.write_file(data.decode("utf-8"))

if __name__ == "__main__":
    tool = DoubanSpider()
    tool.start_work()
