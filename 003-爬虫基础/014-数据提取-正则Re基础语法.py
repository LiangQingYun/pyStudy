"""
^（脱字符号）：表示匹配字符串的开头，例如表达式 "^hello" 表示以 "hello" 开头的字符串。
$（美元符号）：表示匹配字符串的结尾，例如表达式 "world$" 表示以 "world" 结尾的字符串。
.（点号）：表示匹配任意单个字符，例如表达式 "h.t" 可以匹配 "hat"、"hot"、"hit" 等字符串。
（星号）：表示匹配前面的字符或表达式出现 0 次或多次，例如表达式 "ab" 可以匹配 "a"、"ab"、"abb"、"abbb" 等字符串。
+（加号）：表示匹配前面的字符或表达式出现 1 次或多次，例如表达式 "ab+" 可以匹配 "ab"、"abb"、"abbb" 等字符串，但不能匹配 "a"。
?（问号）：表示匹配前面的字符或表达式出现 0 次或 1 次，例如表达式 "ab?" 可以匹配 "a"、"ab" 等字符串，但不能匹配 "abb"。
[]（方括号）：表示匹配方括号内的任意单个字符，例如表达式 "[abc]" 可以匹配 "a"、"b"、"c" 中的任意一个字符。
[^]（方括号内加脱字符号）：表示匹配方括号内未列出的任意单个字符，例如表达式 "[^abc]" 可以匹配除了 "a"、"b"、"c" 之外的任意字符
"""

import re

text = "hello world"
pattern = "hello"
match = re.search(pattern, text)

if match:
    print(match.group(0))
    print(f"Found match at position {match.start()} to {match.end()}")

# Output: Found match at position 0 to 5
