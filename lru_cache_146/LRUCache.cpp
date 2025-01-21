#include <iostream>
#include <unordered_map>
#include <vector>

class LRUCache {
public:
  std::unordered_map<int, std::pair<int, int>> lruMap;
  int maxCapacity;
  int timestamp;

  LRUCache(int capacity) {
    maxCapacity = capacity;
    timestamp = 0;
  }

  int get(int key) {
    // Element not found
    if (lruMap.count(key) == 0) {
      return -1;
    }

    // Increase timestamp
    lruMap.at(key).second = ++timestamp;

    // Return value
    return lruMap.at(key).first;
  }

  void put(int key, int value) {
    // if there are duplicate keys
    if (lruMap.count(key) > 0) {
      lruMap[key] = std::pair<int, int>(value, ++timestamp);
      return;
    }

    // if map is full, replace the one with the oldest timestamp
    if (lruMap.size() == maxCapacity) {
      auto it = min_element(lruMap.begin(), lruMap.end(),
                            [](const auto &l, const auto &r) {
                              return l.second.second < r.second.second;
                            });
      lruMap.erase(it);
    }

    lruMap.insert_or_assign(key, std::pair<int, int>(value, ++timestamp));
  }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

int main() {
  LRUCache lRUCache = LRUCache(2);
  lRUCache.put(1, 1);                        // cache is {1=1}
  lRUCache.put(2, 2);                        // cache is {1=1, 2=2}
  std::cout << lRUCache.get(1) << std::endl; // return 1
  lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
  std::cout << lRUCache.get(2) << std::endl; // returns -1 (not found)
  lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
  std::cout << lRUCache.get(1) << std::endl; // return -1 (not found)
  std::cout << lRUCache.get(3) << std::endl; // return 3
  std::cout << lRUCache.get(4) << std::endl; // return 4

  return 0;
}
