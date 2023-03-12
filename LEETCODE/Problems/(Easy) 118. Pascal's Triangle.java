import java.util.ArrayList;
import java.util.List;
class Solution
{
    public List<List<Integer>> generate(int numRows) 
    {
        int [][] pascal = new int[numRows][numRows];
        for (int i = 0; i < numRows; i++)
        {
            for (int j = 0; j <= i;j++)
            {
                if (j==0||j==i)
                {
                    pascal[i][j]=1;
                }
                else
                {
                    pascal[i][j]=pascal[i-1][j-1]+pascal[i-1][j];
                }
            }
        }
        List<List<Integer>> res= new ArrayList();
        for (int i = 0; i < numRows; i++)
        {
            List<Integer> temp= new ArrayList();
            for (int j = 0; j <= i; j++)
            {
                temp.add(pascal[i][j]);
            }
            res.add(temp);
        }
        return res;
    }
}