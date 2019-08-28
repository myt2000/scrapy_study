from urllib import request, response, parse
import ssl

def ssl_load_data():

    # 1.url
    url = "https://www.12306.cn/index/"
    # 2.headers
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 3.request
    req = request.Request(url, headers=headers)

    # 4.发送请求
    # 主动告诉系统 忽略证书ssl
    context = ssl._create_unverified_context()
    resp = request.urlopen(req, context=context)

    with open("4ssl.html", "w", encoding="utf-8") as f:
        f.write(resp.read().decode("utf-8"))




if __name__ == '__main__':
    ssl_load_data()