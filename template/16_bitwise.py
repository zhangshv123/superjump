1 char = 1 byte = 8 bits
1 integer = 4 byte
整数是
32 bit = 4 bytes = 1 integer

所以array长度<= 32都可以用一个整数来代替
01010000......
这里0可以代表false, 1 代表true
把第n位为从0变成1和从1变成0都可以用XOR
mask = mask^(1<<n)





按位与&(bitwise AND)
两个都是1时结果才为1
e.g. 1&0=0, 0&1=0, 0&0=0, 1&1=1

按位或|(bitwise inclusive OR)
两个有一个是1结果就为1
e.g. 1|1=1, 1|0=1, 0|0=0, 0|1=1
经常用来将某些二进制位设为1

按位异或^(bitwise exclusive OR)
当两位相异时，结果为1，相加不进位
e.g. 1^1=0, 1^0=1, 0^1=1, 0^0=0
任意一位，和0异或操作不变，和自身异或操作为0
对于任何数,都有A^0=A A^A=0
自反性：A^B^A=B^0=B

