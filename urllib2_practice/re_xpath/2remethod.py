import re

if __name__ == "__main__":

    # re.match("\d+",str)
    # re.search("",str)
    # re.findall()

    # 1.match 默认从开头 匹配一次
    # 纯数字的正则
    match_str = "123abc"
    pattern = re.compile("\d+")

    result = pattern.match(match_str)
    # 123
    result = pattern.match(match_str, 1, 4)
    # 23

    # 2.search 默认任意位置开始 匹配一次
    result = pattern.search(match_str)
    print(result.group())
    # 3.findall 全局 返回的是列表
    all_str = "abdsffsdbfsdsbfdsfb"
    all_pattern = re.compile(r"b")
    result = all_pattern.findall(all_str)
    print(result)
    # ['b', 'b', 'b', 'b']
    # 4.finditer 全局 返回 迭代对象
    result = all_pattern.finditer(all_str)

    for page in result:
        print(page.group())
    '''
    b
    b
    b
    b
    '''