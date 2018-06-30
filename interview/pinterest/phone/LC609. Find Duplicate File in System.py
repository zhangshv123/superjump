from collections import defaultdict
class Solution(object):
	def findDuplicate(self, paths):
		"""
		:type paths: List[str]
		:rtype: List[List[str]]
		"""
		store = defaultdict(list)
		for path in paths:
			splitted_path = path.split(" ")
			for rest in splitted_path[1:]:
				filename, content = rest.split("(")
				store[content].append(splitted_path[0] + "/" + filename)
		return [value for value in store.values() if len(value) > 1]
		
s = Solution()
print s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])

follow up question:
1.Imagine you are given a real file system, how will you search files? DFS or BFS?

如果是一个真实的文件系统，那么其实DFS和BFS搜索都是可以的。不同点在于用DFS搜索时，如果文件深度太深，
那么可能会需要占用较大的内存栈空间；用BFS时，如果每个文件夹下面的文件夹数量太多，则队列可能会比较长，因此也会占用较大的内存空间
2.If the file content is very large (GB level), how will you modify your solution?

如果文件内容过大，那么显然就不能将文件内容直接作为哈希表的key了。我觉得有几种可能的改进方法：
a）用MD5算法（或者其它类似的算法）生成文件内容对应的key，然后用这个key作为哈希表的key；
2）采用多次哈希的方法，例如第一次用fn_content的长度来作为key，第二次处理的时候，在长度相同的文件列表中，
再用MD5算法判断文件内容是不是相同。这样做的好处在于第一次哈希的时候，就排除了大量内容大小不同的文件，
从而使得需要用MD5算法的文件数目大大减少，从而提高效率。
实际的例子：
In real-world file system, we usually store large file in multiple "chunks" (in GFS, one chunk is 64 MB),so we have meta data recording the file size,file name and index of different chunks along with each chunk's checkSum (the xor for the content).
So when we upload a file, we record the meta data as mentioned above.
When we need to check for duplicates, we could simply check the meta data:
1.Check if files are of the same size;
2.if step 1 passes, compare the first chunk's checkSum
3.if step 2 passes, check the second checkSum
...
and so on.
There might be false positive duplicates, because two different files might share the same checkSum.
3.If you can only read the file by 1kb each time, how will you modify your solution?

那就每读进来1kb的数据，做一次MD5吧，最后把所有的MD5结果生成一个向量，或者再次MD5，用最终结果来作为哈希表的key。
we could read the meta data instead of the entire file, and compare the information KB by KB.

4.What is the time complexity of your modified solution? What is the most time-consuming part and memory consuming part of it? How to optimize?

如果认为平均每个文件夹下面有常数个文件（夹），那么修改后的算法的时间复杂度就是O(file_counts * avg_file_length)，
其中file_counts表示文件系统中所有的文件个数；avg_file_length表示平均文件长度。
最耗时的有可能是两部分：a）遍历文件的部分（如果文件数量特别大）；b）读取每个文件内容的部分（如果每个文件特别大）。
要优化，那么除了采用3）中的方法之外，还可以采用并行化方法来处理。例如遍历文件的时候，采用多线程或者map reduce的思路进行并行，
最后再合成所有的结果。读取每个文件内容的时候，也可以采用多线程（需要硬盘支持了，有这样的硬盘吗？）。
5.How to make sure the duplicated files you find are not false positive?

再牛逼的哈希算法也不能保证完全消除冲突，那么为了make sure，就只好最后对结果采用最笨的方法进行double check了。。。
Using checkSum, we could quickly and accurately find out the non-duplicated files. 
But to totally avoid getting the false positive, we need to compare the content chunk by chunk 
when we find two "duplicates" using checkSum.


