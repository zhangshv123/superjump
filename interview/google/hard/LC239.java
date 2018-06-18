/*
We scan the array from 0 to n-1, keep "promising" elements in the deque. The algorithm is amortized O(n) as each element is put and polled once.

At each i, we keep "promising" elements, which are potentially max number in window [i-(k-1),i] or any subsequent window. This means

If an element in the deque and it is out of i-(k-1), we discard them. We just need to poll from the head, as we are using a deque and elements are ordered as the sequence in the array

Now only those elements within [i-(k-1),i] are in the deque. We then discard elements smaller than a[i] from the tail. This is because if a[x] <a[i] and x<i, then a[x] has no chance to be the "max" in [i-(k-1),i], or any other subsequent window: a[i] would always be a better candidate.

As a result elements in the deque are ordered in both sequence in array and their value. At each step the head of the deque is the max element in [i-(k-1),i]
*/

//http://www.jianshu.com/p/7662caf4f39c
class Untitled {
    public int[] maxSlidingWindow(int[] a, int k) {		
        if (a == null || k <= 0) {
            return new int[0];
        }
        int n = a.length;
        int[] r = new int[n-k+1];
        int ri = 0;
        // store index
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < a.length; i++) {
            // remove numbers out of range k
            while (!q.isEmpty() && q.peek() < i - k + 1) {
                q.poll();
            }
            // remove smaller numbers in k range as they are useless
            while (!q.isEmpty() && a[q.peekLast()] < a[i]) {
                q.pollLast();
            }
            // q contains index... r contains content
            q.offer(i);
            if (i >= k - 1) {
                r[ri++] = a[q.peek()];
            }
        }
        return r;
    }
}
/**
*A Set contains no duplicate elements. That is one of the major reasons to use a set. There are 3 commonly used implementations of Set: HashSet, 
*TreeSet and LinkedHashSet. When and which to use is an important question. In brief, if you need a fast set, you should use HashSet; 
*if you need a sorted set, then TreeSet should be used; if you need a set that can be store the insertion order, LinkedHashSet should be used.
**/

public class Solution {
    //http://www.programcreek.com/2013/03/hashset-vs-treeset-vs-linkedhashset/
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (k == 0) return new int[]{};
        
        TreeSet<Integer> bst = new TreeSet<Integer>(new Comparator<Integer>(){
            @Override
            public int compare(Integer a, Integer b) {
                if (nums[a] != nums[b]) {
                    return nums[a] - nums[b];
                } else {
                    return a-b;//a[a]-a[b]can not be 0 so we just return anyting except 0
                }
            }
        });
        
        int[] ans = new int[nums.length - k + 1];
        for (int i = 0; i < nums.length; i++) {
            bst.add(i);
            if (i >= k) {
                bst.remove(i - k);
            }
            if (i >= k - 1) {
                ans[i - (k - 1)] = nums[bst.last()];
            }
        }
        
        return ans;
    }
}
//treemap
public class Solution {
    //http://www.programcreek.com/2013/03/hashset-vs-treeset-vs-linkedhashset/
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (k == 0) return new int[]{};
        
        TreeMap<Integer, Integer> bst = new TreeMap<>((o1, o2) -> o1 - o2); 
        
        int[] ans = new int[nums.length - k + 1];
        for (int i = 0; i < nums.length; i++) {
            if (!bst.containsKey(nums[i])) {
                bst.put(nums[i], 1);
            } else {
                bst.put(nums[i], bst.get(nums[i]) + 1);
            }
            if (i >= k) {
                bst.put(nums[i-k], bst.get(nums[i-k]) - 1);
                if (bst.get(nums[i-k]) == 0) {
                    bst.remove(nums[i-k]);
                }
            }
            if (i >= k - 1) {
                ans[i - (k - 1)] = bst.lastKey();
            }
        }
        return ans;
    }
}