import requests

class Tieba_spider(object):
    def __init__(self,tiebaname,start_page,end_page):
        self.base_url = "https://tieba.baidu.com"
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.start = start_page
        self.end = end_page
        self.name = tiebaname

        #1.第一层数据解析 xpath

        #2.第二层数据解析 xpath

    #发送请求
    def send_request(self, url, params={}):
        try:
            reponse = requests.get(url, params=params, headers=self.headers)
            print(url)
            return reponse.content
        except Exception as err:
            print(err)

    #写入文件
    def write_file(self,data):
        with open("7teiba.html","w", encoding="utf-8") as f:
            f.write(data)

    #解析数据
    def analysis_data(self, data):
        pass

    #调度方法
    def start_work(self):

        for page in range(self.start, self.end+1):
            pn = (page - 1) * 50
            #1.拼接url
            params = {
                "kw": self.name,
                "ie": "utf-8",
                "pn": pn,
            }

            #2.发送 第一次 页面的额请求
            first_data = self.send_request(self.base_url + '/f?', params)

            #3.存入 本地
            if first_data:
                self.write_file(first_data.decode("utf-8"))



if __name__ == '__main__':

    tiebaname = input("请输入贴吧名字:")
    start_page = 1
    end_page = 1

    tool = Tieba_spider(tiebaname, start_page, end_page)
    tool.start_work()


    #1.贴吧第一页的数据

    #2.提取每个字链接

    #3.提取图片的 src