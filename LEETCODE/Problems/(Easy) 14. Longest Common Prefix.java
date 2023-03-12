
class Solution 
{
    public String longestCommonPrefix(String[] strs) 
    {
        if (strs==null || strs.length==0) return "";
        int c=0;
        String res="";
        while (true)
        {   
            boolean stop=false;
            for (String str : strs)
            {
                if (c>=str.length())
                {
                    stop=true;
                    break;
                }
                else
                {
                    if(str.charAt(c)!=strs[0].charAt(c))
                    {
                        stop=true;
                        break;
                    }
                }
            }
            if (stop==true)
            {
                break;
            }
            else
            {
                String temp=""+strs[0].charAt(c);
                res+=temp;
                c+=1;
            }
        }
        return res;
    }
}