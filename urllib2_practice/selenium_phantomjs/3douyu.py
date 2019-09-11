from selenium import webdriver
import time
from bs4 import BeautifulSoup

class douyu_spider():
    def __init__(self):
        self.base_url = 'https://www.douyu.com/directory/all'
        self.count = 0
        self.driver = webdriver.Firefox()

    def send_request(self):
        time.sleep(1)
        self.driver.get(self.base_url)
        data = self.driver.page_source
        self.analysis_data(data)
        # dy-Pagination-disabled 没有下一页了

            # self.driver.find_element_by_class_name('dy-Pagination-next').click()
        # with open("3douyu.html", "w", encoding='utf-8') as f:
        #     f.write(data)
        return data

    def analysis_data(self, data):
        soup = BeautifulSoup(data, 'lxml')

        home_list = soup.select('.layout-Module .DyListCover-intro')

        name_list = soup.select('.layout-Module .DyListCover-user')

        super_list = soup.select('.layout-Module .DyListCover-hot')

        for home, name, supers in zip(home_list, name_list, super_list):
            print(home.get_text().strip())
            print(name.get_text())
            print(supers.get_text())
            self.count += 1
        print(self.count)

if __name__ == '__main__':
    tool = douyu_spider()
    data = tool.send_request()
    tool.analysis_data(data)