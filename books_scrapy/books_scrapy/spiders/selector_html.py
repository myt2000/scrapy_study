#-*-coding:utf-8-*-
from scrapy.selector import Selector

text = '''
       <html>
            <body>
                <h1>Hello World</h1> 
                <h1>Hello Scrapy</h1> 
                <h1>Hello python</h1> 
                <ul> 
                    <li>C++</li> 
                    <li>Java</li> 
                    <li>Python</li> 
                </ul> 
            </body> 
       </html> 
       '''
selector = Selector(text=text)