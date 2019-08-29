import requests
import re

import time



class Neihan_spider(object):
    def __init__(self):
        self.base_url = "https://www.neihanba.com/dz/list_"
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

        #第一层的解析正则表达式
        #千万注意 这则里面的符号不能改
        self.first_pattern = re.compile(r'<div class="f18 mb20">.*?</div>', re.S|re.I)

        #第二层数据正则表达式
        #1.所有标签无论开关 <.*?>
        #2.字符实体:&(.*?);
        #3.空白  \s
        #4.全角的空格 \u3000\u3000
        self.second_pattern = re.compile(r'<.*?>|&(.*?);|\s|　　')

    # 1.送请求
    def send_request(self,url):
        time.sleep(1)
        try:
             response = requests.get(url, headers=self.headers)
             return response.content
        except Exception as err:
            print(err)

     #2.写入本地
    def write_file(self,data,page):

         with open("4neihan2.txt","a", encoding="utf-8") as f:
             # 区分第几页的数据
             filename = "第" + str(page) + "页的段子\n"
             print(filename)
             f.write(filename)

             for content in data:
                 #第二层解析，替换为空
                 second_data = self.second_pattern.sub("",content)
                 f.write(second_data)
                 #在每个段子结束的时候 加个换行
                 f.write("\n\n")



     #3.解析数据
     #3.1 <div class="f18 mb20">(.*?)</div>
     #3.2二次解析
    def analysis_data(self,data):
         # print(type(data))
         # data = str(data)
         #.解析第一层数据 每一个段子提出来
         data_list = self.first_pattern.findall(data)

         return data_list

     #4.调度方法
    def start_work(self):

         #循环调用
         for page in range(1,5):

             #1.拼接url
             if page == 1:
                 url = "https://www.neihanba.com/dz/index.html"
             else:
                 url = self.base_url + str(page) + ".html"

             #2.发送请求
             data = self.send_request(url)

             #转码: 原因:内涵网址的数据默认编码gbk ;
             #所有码都和unicode 可以互转 , python3默认是utf8的编码，所以只需要将二进制转一次就好了
             data = data.decode("gbk")

             #3.解析第一层的数据
             second_data = self.analysis_data(data)

             #4.将第一次解析完毕的数据 写入
             self.write_file(second_data,page)



if __name__ == '__main__':

    tool = Neihan_spider()
    tool.start_work()