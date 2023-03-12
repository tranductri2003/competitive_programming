// I             1
// V             5
// X             10
// L             50
// C             100
// D             500
// M             1000
class Solution {
    public int romanToInt(String s) 
    {
        int res = 0;
        int i = 0;
        while (i < s.length()) 
        {
            if (s.charAt(i) == 'I') 
            {
                if (i == s.length() - 1) 
                {
                    res += 1;
                    i += 1;
                } 
                else 
                {
                    if (s.charAt(i + 1) == 'V') 
                    {
                        res += 4;
                        i += 2;
                    } 
                    else if (s.charAt(i + 1) == 'X') 
                    {
                        res += 9;
                        i += 2;
                    } 
                    else 
                    {
                        res += 1;
                        i += 1;
                    }
                }
            } 
            else if (s.charAt(i) == 'V') 
            {
                res += 5;
                i += 1;
            } 
            else if (s.charAt(i) == 'X') 
            {
                if (i == s.length() - 1) 
                {
                    res += 10;
                    i += 1;
                } 
                else 
                {
                    if (s.charAt(i + 1) == 'L') 
                    {
                        res += 40;
                        i += 2;
                    }
                    else if (s.charAt(i + 1) == 'C') 
                    {
                        res += 90;
                        i += 2;
                    } 
                    else 
                    {
                        res += 10;
                        i += 1;
                    }
                }
            } 
            else if (s.charAt(i) == 'L') 
            {
                res += 50;
                i += 1;
            } 
            else if (s.charAt(i) == 'C') 
            {
                if (i == s.length() - 1) 
                {
                    res += 100;
                    i += 1;
                } else 
                {
                    if (s.charAt(i + 1) == 'D') 
                    {
                        res += 400;
                        i += 2;
                    }
                    else if (s.charAt(i + 1) == 'M') 
                    {
                        res += 900;
                        i += 2;
                    } else 
                    {
                        res += 100;
                        i += 1;
                    }
                }
            } 
            else if (s.charAt(i) == 'D') 
            {
                res += 500;
                i += 1;
            } 
            else if (s.charAt(i) == 'M') 
            {
                res += 1000;
                i += 1;
            }
        }
        return res;
    }
}