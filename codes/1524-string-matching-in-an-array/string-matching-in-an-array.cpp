using namespace std;
class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        vector <string> output={};
        for (string i: words){
            for (string j:words){
                if(i!=j and j.contains(i)){
                    output.push_back(i);
                    break;
                }
            
            }
        
        }
        return output;
    }
};