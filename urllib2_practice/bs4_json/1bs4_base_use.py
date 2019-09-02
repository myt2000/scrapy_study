from bs4 import BeautifulSoup

def bs_base_use():
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

    # 1.转换文档类型为解析类型
    # soup = BeautifulSoup(html)
    soup = BeautifulSoup(html, "lxml")

    # 2.格式化输出
    data = soup.prettify()
    print(data)


if __name__ == '__main__':
    bs_base_use()
