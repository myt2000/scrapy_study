import urllib.request
import sys
import io

def load_daidu_data():
    url = "http://www.baidu.com"
    # url = "https://www.python.org"
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
    response = urllib.request.urlopen(url)

    data = response.read()
    # python3
    # str:unicode字符串
    # bytes:非unicode
    print(data.decode("utf-8"))
    return data

def write_file(data):
    with open("3baidu.html", "w", encoding="utf-8") as f:
        f.write(data)

if __name__ == "__main__":
    data = load_daidu_data()
    # 因为获取的是bytes 需要转码 str(unicode)字符
    decode_data = data.decode("utf-8")
    write_file(decode_data)
#
# def load_data():
#     #
#     # 1.URL
#     url = "http://www.baidu.com"
#
#     # 2.发送请求
#     response = urllib.request.urlopen(url)
#
#     # 3.返回数据
#     data = response.read()
#
#     print(data)
#     return data
#     # python3
#     #     str:unicode字符串
#     #     bytes:非unicode
#
# def  write_file(data):
#     with open("3baidu.html","w", encoding='utf-8') as f:
#          f.write(data)
#
# if __name__ == '__main__':
#     data = load_data()
#
#     #因为 获取出来的是bytes类型 我们需要转码 str(unicode字符)
#     decode_data = data.decode("utf-8")
#     write_file(decode_data)