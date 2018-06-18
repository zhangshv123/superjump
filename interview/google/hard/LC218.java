  //"""
//The Skyline Problem
//https://www.youtube.com/watch?v=GSBLe8cKu0s
//https://briangordon.github.io/2014/08/the-skyline-problem.html
//"""
/*
put height into priorityqueue for start
remove height from priorityqueue for end
update the maxHeight in priorityQueue in prev variable if necessary,
if prev change, make a record.

edge case(collapse):
start1, start2:
max height goes first
end1, end2:
smaller height goes first
end1, start2:
start2 goes first
for sorting, start should always smaller than end
the way to do that is:
start -height(negative number for start)
end height
*/
import java.util.*;
class Untitled {
	public static void main(String[] args) {
		
	}
	public List<int[]> getSkyline(int[][] buildings) {
		List<int[]> result = new ArrayList<>();
		List<int[]> height = new ArrayList<>();
		for(int[] b:buildings) {
			height.add(new int[]{b[0], -b[2]});
			height.add(new int[]{b[1], b[2]});
		}
		Collections.sort(height, (a, b) -> {
				if(a[0] != b[0]) 
					return a[0] - b[0];
				return a[1] - b[1];
		});
		Queue<Integer> pq = new PriorityQueue<>((a, b) -> (b - a));
		pq.offer(0);
		int prev = 0;
		for(int[] h:height) {
			if(h[1] < 0) {
				pq.offer(-h[1]);
			} else {
				pq.remove(h[1]);
			}
			int cur = pq.peek();
			if(prev != cur) {
				result.add(new int[]{h[0], cur});
				prev = cur;
			}
		}
		return result;
	}
			
}
