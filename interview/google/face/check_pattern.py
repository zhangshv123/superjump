"""
server中有一个数组，client传一个数组，判断两个数组是否有一样的pattern。 比如[1, 5, 4]和 [2,9,6]一样， 
和[3,6,1]就不一样，sort数组，判断排序后的index是否一样。follow up：有duplicate， 优化时间复杂度。.


第四轮 [1,5,3,4] 和 [1,5,3,7]算一样pattern吗？

补充内容 (2018-3-2 12:28):

这俩不一样，两个数组任意两两元素之间的关系都要一样。
"""

"""
楼主第四题是不是可以用stack? 如果当前值>top就push, 否则就pop直到当前值>top或者stack为空， pattern一样等价于stack 操作完全一样。
比如，[1,5,4] 和 [2,9,6] 都是 push, push, pop, push，而[3,6,1]是 push, push, pop, pop, push.
"""