"""
 自己定义一个数据结构，来表示HTML的element（面试对html做了些简化，假设只有p、div、h1、h2、br、span）。然后，检查两个html页面的文字，是否一样。比如：html1="<p>H<h1>el<h2>l</h2>o</h1> wo</p><span>rld</span>". html2 = "Hel<div>lo w</div>orl<br>d</br>" => 返回true，因为两个页面的结构尽管不同，但是如果抛开结构的不同，按顺序把文字拼在一起，两个的文字都是“Hello world”。
"""
def checkWeb(s1, s2):
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        while i < len(s1) and s1[i] == "<":
            while s1[i] != ">":
                i += 1
            i += 1
        while j < len(s2) and s2[j] == "<":
            while s2[j] != ">":
                j += 1
            j += 1    
        if i < len(s1) and j < len(s2) and s1[i] != s2[j]:
            return False
        i += 1
        j += 1
    return i > len(s1) and j > len(s2)
html1="<p>H<h1>el<h2>l</h2>o</h1> wo</p><span>rld</span>"
html2 = "Hel<div>lo w</div>orl<br>d</br>"
print(checkWeb(html1, html2))