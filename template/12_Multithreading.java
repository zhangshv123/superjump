多线程的特点

1.lightweight
2.threads share memory(process就不行)
3.context switch within threads is easy.


reader writer problem
Read Access: If no threads are writing, and no threads have requested write access.
Write Access: If no threads are reading or writing.

我：你能跟我说下thread还有什么其他方式通信吗？
面试官：HTTP and shared variables..（class static variable）
我：那不就是memory吗？ 只不过是在global segment上。
面试官：对的。



