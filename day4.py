#打开文件：使用 open() 函数来打开一个文件，可以指定打开文件的模式（读、写、追加等）。
#第二个参数指定权限
file = open("/Users/admin/app-server/pythonTest.text","r")
#读取文件：使用 read() 方法来读取文件的内容。
content = file.read()
print(content)
#写入文件：使用 write() 方法来写入文件的内容。
file = open("/Users/admin/app-server/pythonTest.text","w")
file.write("hello world!")
#关闭文件：使用 close() 方法来关闭文件。
file.close()
#使用 with 语句来打开文件，在文件使用完毕后会自动关闭文件。
with open("/Users/admin/app-server/pythonTest.text","r") as file:
    content = file.read()
    print(content)