import os
import pandas as pd

# 打开文件并读取内容  
with open(r'D:\Desktop\Resume\Personal_page\_talks\Resaerch_of_FAD.md', 'r', encoding='utf-8') as file:  
    content = file.read()  
  
# 打印文件内容  
# print(content)

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    if type(text) is str:
        return "".join(html_escape_table.get(c,c) for c in text)
    else:
        return "False"

content=html_escape(content)

print(content)