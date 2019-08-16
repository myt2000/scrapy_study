from urllib import request

def proxy_openner():
    '''
    1.url
    2.headers
    3.request
    4.用自己的openner.open()发送请求
    5.返回数据
    :return:
    '''

    proxy = {
        "协议": "IP:port",
        }
    # 免费代理的IP
    proxy = {
        "http": "180.116.216.159:8118",
        }
    # 付费的账号格式
    # proxy = {"http":"mr_mao_hacker:sffqry9r@120.27.218.32:16816"}

    proxy_handler = request.ProxyHandler(proxy)

    openner = request.build_opener(proxy_handler)

    url = "https://www.baidu.com/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    ask = request.Request(url=url, headers=headers)

    apply = openner.open(ask)
    if apply.getcode() == 200:
        print(apply.read().decode("utf-8"))


if __name__ == "__main__":
    proxy_openner()