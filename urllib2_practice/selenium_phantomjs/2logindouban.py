from selenium import webdriver

def login_douban():
    # 1.创建 浏览器对象
    driver = webdriver.Firefox()
    # 2.发送请求
    driver.get("https://accounts.douban.com/passport/login")
    driver.save_screenshot("2doubancode.png")
    driver.find_element_by_class_name("account-tab-account").click()
    # 3.填充 用户名 密码 验证码
    driver.find_element_by_name("username").send_keys(u"#########")
    driver.find_element_by_name("password").send_keys(u"*********")
    data = driver.page_source

    with open("2douban.html", "w", encoding="utf-8") as f:
        f.write(data)
    # 4.点击登录按钮
    driver.find_element_by_class_name("btn-active").click()
    # driver.find_element_by_xpath('//*/div[@class="account-form-field-submit"]/a').click()

    # 5.是否登录成功
    driver.save_screenshot("2logined.png")

if __name__ == '__main__':
    login_douban()