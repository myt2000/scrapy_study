import urllib


def load_daidu_data():
    url = "http://www.baidu.com"
    # url = "https://www.python.org"
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
    # 伪装用户头
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    # request = urllib.request.Request(url, headers=headers)
    # 构建请求对象
    request = urllib.request.Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36')
    request.add_header('Connection', 'keep-alive')
    response = urllib.request.urlopen(request)
    # 获取用户头
    user = request.get_header("User-agent")
    print(user)
    # 获取真实路径
    real_url = response.geturl()
    print(real_url)
    # 获取返回状态码
    code = response.getcode()

    if code == 200:
        print(code)


    data = response.read()
    # python3
    # str:unicode字符串
    # bytes:非unicode
    # print(data.decode("utf-8"))
    return data



if __name__ == "__main__":
    data = load_daidu_data()
    # 因为获取的是bytes 需要转码 str(unicode)字符
    # decode_data = data.decode("utf-8")
    # print(data.decode('utf-8'))


