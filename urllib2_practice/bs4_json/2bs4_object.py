from bs4 import BeautifulSoup


def bs_object():
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
    # 转换类型
    soup = BeautifulSoup(html,"lxml")

    # 1.Tag -->标签 --默认返回的是 复合条件第一个
    head = soup.head
    p = soup.p
    a = soup.a
    # print a
    # print a.name
    # print a.attrs
    # print type(p)

    # 2.Navigablestring
    title = soup.title
    # print title.string
    # print type(title.string)

    # 3.BeautifulSoup
    # print type(soup)

    # 4,.Comment -->注释的内容
    a = soup.a
    print(a)
    print(a.string)
    print(type(a.string))