from urllib import request, parse
import urllib

def web_auth_openner():
    # 1.url
    url = "http://60.205.187.28/1.php"

    #密码管理器
    pwd_manager = request.HTTPPasswordMgrWithDefaultRealm()

    pwd_manager.add_password(None, uri=url, user="admin", passwd="admin")

    web_handler = request.HTTPBasicAuthHandler(pwd_manager)

    web_openner = request.build_opener(web_handler)

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 3.request
    ask = request.Request(url, headers=headers)

    # 4.自定义的openner.open()
    response = web_openner.open(ask)

    # 5.返回数据
    print(response.read().decode("utf-8"))


if __name__ == '__main__':
    web_auth_openner()
