class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            hashmap[key].append(s)
        return list(hashmap.values())
    
# 这道题的核心是将每个字符串进行排序，得到一个唯一的键，
# 然后将具有相同键的字符串分组在一起。
# 使用哈希表（字典）来存储这些分组，最后返回所有分组的列表。