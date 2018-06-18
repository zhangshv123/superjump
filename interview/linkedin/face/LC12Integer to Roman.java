#!/usr/bin/python
public class Solution {
	public String intToRoman(int num) {
		/**
		I: 1
		V: 5
		X: 10
		L: 50
		C: 100
		D: 500
		M: 1000
		**/
		String roman="";
		String one[]={"I","II","III","IV","V","VI","VII","VIII","IX"};
		String two[]={"X","XX","XXX","XL","L","LX","LXX","LXXX","XC"};
		String three[]={"C","CC","CCC","CD","D","DC","DCC","DCCC","CM"};
		String four[]={"M","MM","MMM"};
		
		if(num/1000!=0){
			roman=roman+four[num/1000-1];
			num=num-1000*(num/1000);
		}
		if(num/100!=0){
			roman=roman+three[num/100-1];
			num=num-100*(num/100);
		}
		if(num/10!=0){
			roman=roman+two[num/10-1];
			num=num-10*(num/10);
		}
		if(num>0){
			roman=roman+one[num-1];
		}
	   return roman; 
	}
}