#include <vector>
using namespace std;
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int sum=0;
        vector <int> num;
        for (int i: nums){
            sum+=i;
            num.push_back(sum);
       
        }
        return num;
    }
};