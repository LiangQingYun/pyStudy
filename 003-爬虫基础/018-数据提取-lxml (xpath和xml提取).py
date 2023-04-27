from lxml import etree

html = """
<!DOCTYPE html>
<html>
<head>
	<title>Example HTML Page</title>
</head>
<body>
	<header>
		<h1>Welcome to my website!</h1>
		<nav>
			<ul>
				<li><a href="#">Home</a></li>
				<li><a href="#">About</a></li>
				<li><a href="#">Contact</a></li>
			</ul>
		</nav>
	</header>
	<main>
		<article>
			<h2>Article Title</h2>
			<p>This is the first paragraph of the article.</p>
			<p>This is the second paragraph of the article.</p>
			<ul>
				<li>List item 1</li>
				<li>List item 2</li>
				<li>List item 3</li>
			</ul>
		</article>
	</main>
	<footer>
		<p>&copy; 2022 Example Company. All rights reserved.</p>
	</footer>
</body>
</html>
"""

# 将 HTML 文本转换成 Element 对象
tree = etree.HTML(html)

print(etree.tostring(tree, encoding='utf-8').decode('utf-8'))

# 使用 XPath 表达式获取文章标题
title = tree.xpath('//h2/text()')[0]
print('\n标题的名称为 : '+title)
# 输出结果：Article Title
