from selenium import webdriver
# 火狐需要的包
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

# 谷歌需要的包

def selenium_base_use():
    # options = Options()
    # options.add_argument('-headless')
    # 1.创建浏览器对象
    driver = webdriver.Firefox()

    # 2. 请求数据
    driver.get("https://www.baidu.com")
    # 3.获取数据
    data = driver.page_source

    with open("1baidu.html", "w", encoding="utf-8") as f:
        f.write(data)
    # print(driver)
    # 点击新闻
    driver.find_element_by_name("tj_trnews").click()
    # 给输入框输入文字
    driver.find_element_by_id("ww").send_keys(u"平安夜")

    driver.find_element_by_class_name('btn').click()

    driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
    # 8. 找到新开的页面 list
    print(driver.window_handles)
    # 9. 根据角标可以切换页面
    # driver.switch_to_window(driver.window_handles[1])
    # 10.再次回到上一个界面
    # driver._switch_to.window(driver.window_handles[0])

    # 11 当前的网址
    current_url = driver.current_url
    print(current_url)
    #
    # 12 获取所有的cookie
    driver.get_cookies()
    #
    # 13. 关闭当前的页面
    driver.close()
    #     # 关闭浏览器
    driver.quit()
    # 4. 快照
    # driver.save_screenshot("1baidu.png")

if __name__ == '__main__':
    selenium_base_use()