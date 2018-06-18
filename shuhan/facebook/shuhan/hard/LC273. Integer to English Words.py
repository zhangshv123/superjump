#每3个是一个pattern，然后，分别要处理<10, 10~20, 20~100之间的特殊case，然后后面的就是调用前面的array，计算重复问题
#http://blog.csdn.net/u013325815/article/details/52582674
class Solution(object):
	belowTen = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
	belowTwenty =["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
	belowHundreds = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
	def numberToWords(self, num):
		res = ""
		if num < 0 :return null
		if num == 0 :
			return "Zero"
		return self.helper(num)
		
	def helper(self,num):
		if num < 10:
			res = self.belowTen[num]
		elif num < 20:
			res = self.belowTwenty[num%10]
		elif num < 100:
			res = self.belowHundreds[num/10] + " " +self.helper(num%10)
		elif num < 1000:
			res = self.belowTen[num/100] + " Hundred " + self.helper(num%100)
		elif num < 1000000:
			res = self.helper(num/1000) + " Thousand " + self.helper(num%1000)
		elif num < 1000000000:
			res = self.helper(num/1000000) + " Million " + self.helper(num%1000000)
		else:
			res = self.helper(num/1000000000) + " Billion " + self.helper(num%1000000000)
		return res.strip()#最后要把多余的空格去掉
		
	

