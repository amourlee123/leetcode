class Solution{
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        vector<int> result(2, -1);
        unordered_map<int, int> m;
        for(int i = 0; i < nums.size(); i++ )
        {
            diff = target - nums[i];
            if( m.find(diff) == m.end() )
            {
                m[nums[i]] = i;
            }
            else
            {
                result[0] = m[diff];
                result[1] = i;
                return result;
            }
        }
    }
}
