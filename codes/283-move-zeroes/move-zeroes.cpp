#include<vector>
using namespace std;
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
    vector <int> list={};

    for (int num:nums){
        if(num!=0){
            list.push_back(num);
        }
    }

    for (int i=0;i<list.size();i++){
        nums[i]=list[i];
    }
    for(int i= list.size();i<nums.size();i++){
        nums[i]=0;
    }
    }
};