class Untitled {
	public static void main(String[] args) {
		
	}
	public int g(T[] a){
		int start = 0;
		int end = a.length-1;
		while (start <= end){
			int mid = start+(end-start)/2;
			G midVal = g(a[mid])
			if(midVal == target){
				return mid;
			}
			if(midVal < target){
				start = mid+1;
			}else{
				back = mid-1;
			}
		}
		return -1;//not found
	}
	
	public int g(T[] a){ //相等的情况
		int start = 0;
		int end = a.length-1;
		int pos = -1;
		while (start <= end){
			int mid = start+(end-start)/2;
			G midVal = g(a[mid])
			if(midVal <= target){
				pos = mid;
				start = mid+1;
			}else{
			   end = mid-1;	
			}			
		}
		return -1;//not found
	}
}