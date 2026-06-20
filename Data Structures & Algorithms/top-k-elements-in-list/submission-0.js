class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freqMap = new Map();
        for (let num of nums) {
            freqMap.set(num, (freqMap.get(num) || 0) + 1);
        }
        const sortedItems = [...freqMap.entries()].sort((a,b) => b[1]- a[1]);

        return sortedItems.slice(0,k).map(item => item[0]);
    }
}
