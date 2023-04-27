

"""
浏览器可以复制路径   但是可能跟源代码不一样  , 浏览器可以安装xpath helper插件

    选取元素：nodename
    选取属性：@attribute
    选取子元素：/
    选取子孙元素：//   (跨节点)
    选取当前节点：.
    选取父节点：..
    选取文本节点：text()

选取所有元素：*
选取所有 book 元素：//book
选取所有具有 category 属性的 book 元素：//book[@category]
选取所有 book 元素的 title 子元素：//book/title
选取 book 元素的第一个 title 子元素：//book[1]/title
选取 book 元素的第二个 title 子元素：//book[2]/title
选取具有 price 属性的 book 元素的 title 子元素：//book[@price]/title
"""