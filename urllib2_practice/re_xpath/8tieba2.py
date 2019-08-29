import requests
from lxml import etree


import time

class Tieba_spider(object):
    def __init__(self,tiebaname,start_page,end_page):
        self.base_url = "https://tieba.baidu.com"
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.start = start_page
        self.end = end_page
        self.name = tiebaname

        #1.第一层数据解析 xpath
        self.first_xpth = '//div[@class="t_con cleafix"]/div/div/div/a/@href'

        #2.第二层数据解析 xpath
        self.secxpath = '//img[@class="BDE_Image"]/@src'

    #发送请求
    def send_request(self,url,params={}):
        time.sleep(1)
        # try:
        reponse = requests.get(url, params=params, headers=self.headers)
        print(url, params)
        return reponse.content
        # except Exception as err:
        #     print(err)

    #写入文件
    def write_file(self, data, page):
        print(page)
        # page是图片名称
        filename = "Tieba/" + page
        with open(filename, "wb") as f:
            f.write(data)

    #解析数据
    def analysis_data(self,data,xpathstr):
        #1.转换html 类型
        html_data = etree.HTML(data)
        #2.解析
        data_list = html_data.xpath(xpathstr)

        return data_list

    #调度方法
    def start_work(self):

        for page in range(self.start,self.end+1):
            pn = (page - 1) * 50
            #1.拼接url
            params = {
                "kw": self.name,
                "ie": "utf-8",
                "pn": pn
            }

            #2.发送 第一次 页面的额请求
            first_data = self.send_request(self.base_url + '/f?',params)

            #3.提取 子链接 每一条单独的 帖子
            first_data_list = self.analysis_data(first_data, self.first_xpth)

            #4. 将每一条子的 数据请求
            for link in first_data_list:
                #拼接 每个帖子 url
                link_url = self.base_url + link
                #发送二次请求
                second_data = self.send_request(link_url)

                #二次解析 取出 每个帖子里面的图片 地址 请求数据
                second_list = self.analysis_data(second_data, self.secxpath)

                #发送图片的请求  将图片保存到本地
                for imgurl in second_list:
                    image_data = self.send_request(imgurl)

                    #写入本地
                    page = imgurl[-15:]
                    if image_data:
                        self.write_file(image_data, page)



if __name__ == '__main__':

    tiebaname = input("请输入贴吧名字:")
    start_page = 1
    end_page = 1

    tool = Tieba_spider(tiebaname, start_page, end_page)
    tool.start_work()


    #1.贴吧第一页的数据

    #2.提取每个字链接

    #3.提取图片的 src