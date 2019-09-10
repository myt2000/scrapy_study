import jsonpath
import json
import requests

def jsonpath_base_use():

    url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    # 注意点: 只有返回是json文件才可以使用json()方法
    data = requests.get(url, headers=headers).json()

    # 解析 -->返回是列表
    analysis_name = jsonpath.jsonpath(data, "$..name")
    # print analysis_name
    for name in analysis_name:
        print(name)

if __name__ == '__main__':
    jsonpath_base_use()
