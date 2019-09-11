from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re

class douyu_spider():
    def __init__(self):
        self.base_url = 'https://www.douyu.com/directory/all'
        self.count = 0
        self.driver = webdriver.Firefox()
        self.page = 1

    def send_request(self):

        self.driver.get(self.base_url)
        # dy-Pagination-disabled 没有下一页了
        while True:
            print("正在下载的页数%d" % self.page)
            time.sleep(1)
            self.page += 1
            data = self.driver.page_source
            self.analysis_data(data)
            # with open("3douyu2.html", "w", encoding='utf-8') as f:
            #     f.write(data)
            print(data.find('dy-Pagination-disabled dy-Pagination-next'))
            if data.find('dy-Pagination-disabled dy-Pagination-next"') != -1:
                break
            # self.analysis_data(data)
            # print(self.driver.find_element_by_class_name('dy-Pagination-next'))
            self.driver.find_element_by_class_name('dy-Pagination-next').click()
        # with open("3douyu.html", "w", encoding='utf-8') as f:
        #     f.write(data)
        #     return data

    def analysis_data(self, data):
        soup = BeautifulSoup(data, 'lxml')

        home_list = soup.select('.layout-Module .DyListCover-intro')

        name_list = soup.select('.layout-Module .DyListCover-user')

        super_list = soup.select('.layout-Module .DyListCover-hot')
        for home, name, supers in zip(home_list, name_list, super_list):
            # pattern = re.compile(r'<.*?>')
            # home = home.decode("utf-8")
            # home = pattern.sub("", home)
            print(home.get_text())
            # name = pattern.sub("", name)
            print(name.get_text())
            # supers = pattern.sub("", supers)
            print(supers.get_text())
            self.count += 1
        print(self.count)

if __name__ == '__main__':
    tool = douyu_spider()
    tool.send_request()
    # tool.analysis_data(data)