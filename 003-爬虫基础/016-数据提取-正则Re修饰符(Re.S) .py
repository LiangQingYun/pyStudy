import re

"""
re.I / re.IGNORECASE：忽略大小写，例如re.match('A', 'a', re.I)可以匹配成功。
re.M / re.MULTILINE：多行模式，例如^和$符号可以匹配每一行的开头和结尾，而不是整个字符串的开头和结尾。
re.X / re.VERBOSE：详细模式，该模式下的正则表达式可以包含注释，而且空格和换行符不会影响正则表达式的匹配。
re.U / re.UNICODE：Unicode模式，可以匹配Unicode字符，例如匹配中文字符。
re.A / re.ASCII：ASCII模式，只能匹配ASCII字符，例如不能匹配中文字符。

"""

pattern = re.compile('hello', re.I | re.M)
