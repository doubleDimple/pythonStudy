#模块与包：Python 的模块是一个包含函数、类和变量的文件，而包是一个包含模块的目录。通过使用模块和包，可以组织和管理大型的 Python 项目。
#导入模块
#import module_name

import re
import os

pattern = r"abc"
text = "abcdefg"

result = re.search(pattern,text)

if result:
    print("匹配成功")
else:
    print("匹配失败")

#文件操作进阶：除了基本的文件读写操作外，Python 还提供了更多的文件处理功能，如文件的复制、重命名、删除等。

## 复制文件
os.copy_file_range()
#重命名文件
os.rename()
#删除文件
os.remove()

