import pymongo
import json
class json_to_mongo():
    def __init__(self):
        self.host = "192.168.0.120"
        self.port = 27017

    def __open_file(self):
        self.file = open("8tencent.json", "rb")
        self.client = pymongo.MongoClient(self.host, self.port)
        # 创建数据库
        self.db = self.client["tencent"]
        # 创建集合
        self.collection = self.db["job"]

    def __close_file(self):
        self.file.close()

    def write_database(self):
        self.__open_file()
        data = json.load(self.file)

        try:
            self.collection.insert(data)
            print("写入成功")
        except Exception as err:
            print(err)
        finally:
            self.__close_file()

if __name__ == '__main__':
    tool = json_to_mongo()
    tool.write_database()