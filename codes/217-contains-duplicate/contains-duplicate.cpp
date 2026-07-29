class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
      set <int> nums1(nums.begin(),nums.end());
      return nums1.size() < nums.size();  
    }
};