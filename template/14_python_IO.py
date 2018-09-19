1 char = 1 byte = 8 bits
1 integer = 4 char = 4 byte  = 32 bits
先写最原始的版本：

b = bytearray("test", encoding="utf-8") # 把string“test”变成一个byteArray
with open("/Users/shuhanzhang/cde", "wb") as fout: #创建一个新的file(名字叫cde，mode是write)然后把b写进去
	fout.write(b)

c = bytearray("est", encoding="utf-8") #我们需要查找的substring,先把string "est"变成byteArray
ss = c.decode()#然后把byteArray变成string

with open("/Users/shuhanzhang/cde", "rb") as fin: #用read模式把cde文件读出来
	content=fin.read()

if ss in content: #判断一个substring在不在一个string中
	print True
else:
	print False
	

