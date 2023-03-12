import java.lang.Math;
class Solution
{
    public int maxProfit(int[] prices) 
    {
        int n=prices.length;
        int [] maxPro= new int[n];
        maxPro[n-1]=prices[n-1];
        for(int i=n-2; i>=0; i--)
        {
            maxPro[i]=Math.max(maxPro[i+1], prices[i]);
        }
        int res=0;
        for (int i=0;i<n;i++)
        {
            res=Math.max(res, maxPro[i]-prices[i]);
        }
        return res;
    }
    public static void main(String[] args)
    {   
        Solution t  = new Solution();
        int [] prices={7,1,5,3,6,4};
        t.maxProfit(prices);
    }
}