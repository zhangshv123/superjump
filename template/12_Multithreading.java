多线程的特点

1.lightweight
2.threads share memory(process就不行)
3.context switch within threads is easy.


reader writer problem
Read Access: If no threads are writing, and no threads have requested write access.
Write Access: If no threads are reading or writing.



