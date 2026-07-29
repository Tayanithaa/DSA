class Solution {
public:
    bool isPalindrome(string s) {
        string clean="";
        for(char c: s){
            if(isalnum(c)){
                clean.push_back(tolower(c));
            }
        }
        string rev=clean;
        reverse(rev.begin(),rev.end());

        return clean==rev;
        
    }
};