from urllib import request

URLERRORCODE = 666

def can_use_proxy(ask,openner,URLERRORCODE):
    try:
        response = openner.open(ask, timeout=3)
        return response.getcode()
    except request.HTTPError as err:
        return err.code
    except request.URLError as err:
        return URLERRORCODE


if __name__ == '__main__':

    # 1.大量proxy free
    proxy_list = [
        {"https":"123.52.43.64:8118"},
        {"http":"112.85.131.219:9999"},
        {"http": "112.85.165.194:9999"},
        {"https": "120.83.108.113:9999"},
        {"http": "163.204.245.229:9999"}
    ]

    #2.验证有几个能用
    can_use_list = []
    for proxy in proxy_list:

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        request = request.Request("http://www.baidu.com",headers=headers)
        #创建 diali处理器
        proxy_handler = request.ProxyHandler(proxy)
        openner = request.build_opener(proxy_handler)

        #验证
        code = can_use_proxy(request, openner, URLERRORCODE)

        print(code)
