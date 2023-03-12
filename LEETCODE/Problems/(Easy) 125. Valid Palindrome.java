
class Solution
{
    private boolean check(char c)
    {
        String alphabet="abcdefghijklmnopqrstuvwxyz0123456789";
        for (int i = 0; i <36;i++)
        {
            if (c==alphabet.charAt(i))
            {
                return true;
            }
        }
        return false;

    }
    public boolean isPalindrome(String s) 
    {
        s=s.toLowerCase();
        StringBuilder newString = new StringBuilder();
        for (int i = 0; i < s.length(); i++)
        {
            if (check(s.charAt(i))==true)
            {
                newString.append(s.charAt(i));
            }
        }
        StringBuilder newNewString=new StringBuilder(newString);
        newNewString.reverse();
        if (newString.toString().equals(newNewString.toString()))
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}