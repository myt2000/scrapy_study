from urllib import request, parse

def custom_openner():
    '''
    1. 创建处理器
    2. 根据处理器 自定义opener
    3. 使用自己的openner,openner.open()发送请求
    '''

    handler = request.HTTPHandler()

    openner = request.build_opener(handler)

    url = "https://www.baidu.com/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    ask = request.Request(url, headers=headers)

    reply = openner.open(ask)

    print(reply)


if __name__ == "__main__":
    custom_openner()


'''
1.为什么创建处理和自定义opener

2.web认证cookie
代理IP

3.系统的url

'''