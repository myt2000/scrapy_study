from urllib import request

def requests_base_use():

    # 1.get 请求
    request.get(url)

    # 2.get带参数 :自动转码
    params = {
        "kw":2
    }
    requests.get(url,params=params)

    # 3.post请求
    request.post(url)

    # 4.带参数 :自动转码
    formdata={
        "kw":2
    }
    request.post(url,data=formdata)

    # 5.ssl --ca的证书 忽略证书认证
    requests.get(url,verfy = False)

    # 6.proxy
    proxy = {"http":"IP:port"}
    requests.get(url,proxies = proxy)

    # 8.webauth
    auth = ("username","pwd")
    requests.get(url,auth = auth)

    # 7.cookie --session
    #71.创建session 还是为了保存cookie
    session = requests.session()

    #7.2 发送登录 -- cookie
    session.post(url)

    #7.3
    session.post(data_url)




if __name__ == '__main__':
    pass