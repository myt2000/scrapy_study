from urllib import request, parse

if __name__ == "__main__":

    try:
        reponse = request.urlopen("http://www.itcast.cn/adsaf")
    except request.HTTPError as err:
        print(err.code)
    except request.URLError as err:
        print(err)
