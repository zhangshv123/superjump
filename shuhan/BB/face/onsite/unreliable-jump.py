#!/usr/bin/python
unreliable jump vs reliable jump
這題蠻有趣的
unreliable jump就是call這function可能會往上跳一個或往下跳一個 要你用unreliable jump implement reliable jump, reliable jump保證要往上跳一格
要求用了三種寫法 用loop, 用recursive傳parameter, 用recursive但不能傳parameter


答案：
int unreliableJump() 會回傳+1(往上跳) or -1(往下跳) 
void reliableJump() 基本上就是要保證往上跳1

最後小哥要的是這樣:
void reliableJump() {
	if (unreliableJump() == 1) return;
	else {
		reliableJump();
		reliableJump();
#		因為unreliableJump() != 1. Waral 鍗氬鏈夋洿澶氭枃绔�,
#		就代表你往下跳了一格
#		所以要往上跳兩次 才能達到往上跳一格
#		這也是小哥提醒我的..
	}
}

count = 0
while count != 1:
	count += unreliableJump()

