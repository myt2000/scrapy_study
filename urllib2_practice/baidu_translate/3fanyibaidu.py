from urllib import request, response, parse
import json

def translate_data(keyword):
    url = "http://fanyi.baidu.com/basetrans"

    formdata = {
        "query": keyword,
        "from": "zh",
        "to": "en",
     }
    formdata_str = bytes(parse.urlencode(formdata).encode(encoding='UTF8'))

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}

    req = request.Request(url=url, data=formdata_str, headers=headers)

    resp = request.urlopen(req)

    data = resp.read().decode("utf-8")

    print(type(data))
    print(data)

    # dict_data = json.loads(data)
    #
    # result = dict_data["trans_result"]["data"][0]["dst"]
    #
    # print(result)

if __name__ == "__main__":
    keyword = input("请输入翻译内容")
    translate_data(keyword)