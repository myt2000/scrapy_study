from urllib import request
import execjs
import json
import ssl


class BaiDuTranslateWeb:
    def __init__(self):
        self.url = "https://fanyi.baidu.com/v2transapi"
        self.headers = {
            # "Cookie": "xxx",
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"
        }
        self.data = {
            "from": "zh",
            "to": "en",
            "query": None,
            "transtype": "translang",
            "simple_means_flag": 3,
            "sign": None,
            "token": "300f465c88543c5218f056447a33a348"
        }

    def get_baidu_sign(self):
        with open("baidusign.js") as f:
            jsData = f.read()
            sign = execjs.compile(jsData).call("e", self.input)
            return sign

    def run(self):
        self.input = input("请输入要翻译的内容：")
        self.get_baidu_sign()
        self.data["query"] = self.input
        self.data["sign"] = self.get_baidu_sign()
        req = request.Request(url=self.url, data=self.data, headers=self.headers)
        context = ssl._create_unverified_context()
        resp = request.urlopen(req, context=context)
        self.result_strs = resp.read().decode("utf-8")

    def get_translate_result(self):
        result_dict = json.loads(self.result_strs)
        if 'trans_result' in result_dict:
            result_dict = result_dict['trans_result']['data'][0] if len(
                result_dict['trans_result']['data']) > 0 else None
            result_dict = result_dict['result'][0] if len(result_dict['result']) > 0 else None
            result = result_dict[1] if len(result_dict) > 1 else None
            print("翻译结果为：")
            print(result)
        else:
            print("请输入内容再进行翻译")


if __name__ == '__main__':
    while True:
        baidutranlate = BaiDuTranslateWeb()
        baidutranlate.run()
        baidutranlate.get_translate_result()
