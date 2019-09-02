from bs4 import BeautifulSoup
import re


def bs_method():
    html = """
         <html><head><title>The Dormouse's story</title></head>
         <body>
         <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
         <p class="story">Once upon a time there were three little sisters; and their names were
         <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
         <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
         <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
         and they lived at the bottom of a well.</p>
         <p class="story">...</p>
         """

    # 1.转换类型
    soup = BeautifulSoup(html, "lxml")
    # 2.find -->只找一个复合条件
    p = soup.find("p")
    p = soup.find(attrs={"class":"title"})
    p = soup.find(text="...")
    p = soup.find(re.compile("^b"))

    # 3.findall-->列表  全局搜索
    p = soup.find_all("p")
    # print len(p)

    # 4.select-->列表 全局搜索  CSS 选择器
    #ID
    #标签
    #类
    #层级选择器
    #并集选择器
    #属性选择器

    a = soup.select("#link2")
    a = soup.select("a")
    a = soup.select(".sister")
    a = soup.select("p #link2")
    a = soup.select("title,a")
    p = soup.select('p[class="story"]')[1]

    # 获取标签包裹的内容
    p_content = p.get_text()
    # 获取属性:默认是列表
    p_class = p.get("class")
    print(p_class[0])


if __name__ == '__main__':
    bs_method()