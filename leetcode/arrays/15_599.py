class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_map = {val: idx for idx, val in enumerate(list1)}
        min_sum = float('inf')
        result = []

        for idx2, val in enumerate(list2):
            if val in index_map:
                idx1 = index_map[val]
                total = idx1 + idx2
                if total < min_sum:
                    result = [val]
                    min_sum = total
                elif total == min_sum:
                    result.append(val)

        return result