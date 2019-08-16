from urllib import request, parse

from http import cookiejar

def send_request():

    #具有cookie 的openner

    #cookjar 用来保存这个 cookie
    cookjar = cookiejar.CookieJar()

    #1.创建处理器
    cook_handler = request.HTTPCookieProcessor(cookjar)

    #2.openner
    cook_openner = request.build_opener(cook_handler)


    # headers
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
               }

    #1.登录成功 -- 有哦cookie
    login_url = "http://renren.com/PLogin.do"

    #2.参数
    formdata = {
        "email": "123@126.com",
        "password": "123"
    }
    formdata_str = bytes(parse.urlencode(formdata).encode("utf-8"))
    ask = request.Request(login_url, data=formdata_str, headers=headers)

    #先发送登录请求 获取保存的cookie
    cook_openner.open(ask)




    #2.拿着有登录成功 cookie的opnner 发送数据请求
    # 1.url -- 直接访问的 登录之后的数据
    data_url = "http://www.renren.com/410043129/profile"
    data_request = request.Request(data_url,headers=headers)

    response = cook_openner.open(data_request)

    return response.read().decode("utf-8")




def write_file(data):
    with open("8renren.html", "w", encoding="utf-8") as f:
        f.write(data)


if __name__ == '__main__':
    data = send_request()
    write_file(data)
