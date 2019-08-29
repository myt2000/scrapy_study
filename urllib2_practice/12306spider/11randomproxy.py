from urllib import request

URLERRORCODE = 666

def can_use_proxy(ask,openner,URLERRORCODE):
    # try:
    response = openner.open(ask)
    return response.getcode()
    # except request.HTTPError as err:
    #     return err.code
    # except request.URLError as err:
    #     return URLERRORCODE


if __name__ == '__main__':

    # 1.大量proxy free,
    # 不稳定，随时要换IP，所以导致很多问题
    proxy_list = [
        {"https":"1.198.73.63:9999"},
        {"http":"123.163.97.7:9999"},
    ]

    #2.验证有几个能用
    can_use_list = []
    for proxy in proxy_list:

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        req = request.Request("http://www.baidu.com", headers=headers)
        #创建 diali处理器
        proxy_handler = request.ProxyHandler(proxy)
        opener = request.build_opener(proxy_handler)

        #验证
        code = can_use_proxy(req, opener, URLERRORCODE)

        print(code)
