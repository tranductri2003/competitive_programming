import java.util.HashMap;
import java.util.Map;
public class Solution
{
    public int singleNumber(int[] nums) 
    {
        HashMap<Integer,Integer> count= new HashMap<Integer,Integer>();
        for (int num: nums)
        {
            int temp=count.getOrDefault(num,0);
            count.put(num,temp+1);
        }
        for (int num: nums)
        {
            if (count.get(num)==1)
            {
                return num;
            }
        }
        return 0;
    }  
}
