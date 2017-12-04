class Solution{
public:
    bool isHappy(int n)
    {
        vector<int> result;
        int val = getSquareSum(n);
        while(val != 1)
        {
            if(std::find(result.begin(), result.end(), val) != result.end())
                return false;
            result.push_back(val);
            val = getSquareSum(val);
        }
        reurn true;
    }

    int getSquareSum(int n)
    {
        int sum = 0, temp;
        while(n)
        {
            temp = n%10;
            sum += temp*temp;
            n = n / 10;
        }
        return sum;
    }
}
