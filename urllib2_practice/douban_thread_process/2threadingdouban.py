import requests
from lxml import etree
import time
import threading


class douban_movie_data(object):
    def __init__(self):
        self.base_url = "https://movie.douban.com/top250"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.count = 0

    def send_request(self, url):
        time.sleep(2)
        try:
            response = requests.get(url, headers=self.headers)
            data = response.content
            self.analysis_data(data)

        except Exception as err:
            print(err)

    def analysis_data(self, data):

        # 1.转换类型
        html_data = etree.HTML(data)

        # 2.xpath
        name_list = html_data.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')

        # 3. 打印查看下
        for name in name_list:
            print(name)
            self.count += 1

    def start_work(self):
        start_time = time.time()

        url_list = []
        thread_list = []
        for page in range(0, 225+1, 25):
            #拼接网址
            url = self.base_url + "?"+"start="+str(page)
            print(url)

            # 1.创建线程
            thread = threading.Thread(target=self.send_request, args=[url])
            # 2.开启
            thread.start()
            thread_list.append(thread)



        # 让主线程等待; 所有的子线程执行完毕
        for thread in thread_list:
            thread.join()

        end_time = time.time()
        all_time = end_time - start_time
        print("总共电影%d" % self.count)
        print("总共的时间是%s" % all_time)



if __name__ == '__main__':
    tool = douban_movie_data()
    tool.start_work()
