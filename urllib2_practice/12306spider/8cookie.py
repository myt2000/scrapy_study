from urllib import request, parse


def send_request():
    # 1.url -- 直接访问的 登录之后的数据
    url = "http://www.renren.com/410043129/profile"

    # 2.headers
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",

               "Cookie":"anonymid=jzcsn0he2yjldm; depovince=ZJ; jebecookies=b90d5e49-e057-4868-bffe-c01cdf30f0aa|||||; _r01_=1; ick_login=eae2a79c-bb56-43be-a0e4-9e63bbc33243; _de=74F51DAAE0DAEDEF8B3930DB5A458638; p=02f06af0a9505dcb710d6071025b184f7; first_login_flag=1; ln_uact=myt2000@126.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn321/20121205/2145/h_main_ObVP_1411000017211376.jpg; t=3126b221ae11de78ac98d40d2195231a7; societyguester=3126b221ae11de78ac98d40d2195231a7; id=340478117; xnsid=66587f6e; ver=7.0; loginfrom=null; JSESSIONID=abcrNNkiIs9uvepc4PzYw; wp_fold=0"
               }


    # 3.request
    ask = request.Request(url, headers=headers)

    # 4.发送请求
    response = request.urlopen(ask)

    # 5.返回数据
    return response.read().decode("utf-8")

def write_file(data):
    with open("8renren.html","w", encoding="utf-8") as f:
        f.write(data)



if __name__ == '__main__':
    data = send_request()
    write_file(data)