from urllib import request, response, parse
import urllib
from User_Agent_list import USER_AGENT_LIST
import random

def search_data(keyword):
    # url = "https://www.baidu.com/s?wd=%s" % keyword
    url = "https://www.baidu.com/s?"

    params = {
        'wd': keyword,
    }


    params_str = parse.urlencode(params)
    real_url = url + params_str
    print(real_url)


    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    headers = {'User-Agent': random.choice(USER_AGENT_LIST)}
    print(headers)
    req = request.Request(real_url, headers=headers)

    resp = request.urlopen(req)

    return resp.read()

def write_file(data):
    with open("6baidu.html", "w", encoding="utf-8") as f:
        f.write(data)

if __name__ == "__main__":
    keyword = "虾米"
    data = search_data(keyword)
    write_file(data.decode('utf-8'))
