关于linkedhashmap的介绍可以参考：https://www.tutorialspoint.com/java/java_linkedhashmap_class.htm
public class LRUCache {
		
		private Map<Integer,Integer> zhenXi;
		private final int capacity;
		
		public LRUCache(int _capacity) {
			zhenXi = new LinkedHashMap<>();
			capacity = _capacity;
		}
		
		public int get(int key) {
			if (!zhenXi.containsKey(key)){
				return -1;
			}
			int value = zhenXi.get(key);
			zhenXi.remove(key);
			zhenXi.put(key,value);
			return value;
		}
		
		public void put(int key, int value) {
			if(zhenXi.containsKey(key)){
				zhenXi.remove(key);
			}else if(zhenXi.size() == capacity){
				Iterator<Map.Entry<Integer,Integer>> iter = zhenXi.entrySet().iterator();
				iter.next();
				iter.remove();
			}
			zhenXi.put(key,value);			
		}
	}