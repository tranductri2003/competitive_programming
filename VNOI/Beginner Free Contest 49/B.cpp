#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

void getValidNumbers(std::string s)
{
    std::vector<std::string> sArr;
    std::string temp = "";
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == ',')
        {
            sArr.push_back(temp);
            i += 1;
            temp = "";
        }
        else
        {
            temp += s[i];
        }
    }
    sArr.push_back(temp);

    std::vector<int> data;
    std::vector<int> number;
    for (int i = 0; i < 10; i++)
    {
        number.push_back(i);
    }

    for (std::string chuoi : sArr)
    {
        std::vector<int> tempData;
        int i = 0;
        temp = "";
        while (i < chuoi.length())
        {
            while (i < chuoi.length() && std::find(number.begin(), number.end(), chuoi[i] - '0') != number.end())
            {
                temp += chuoi[i];
                i++;
            }
            if (!temp.empty())
            {
                tempData.push_back(std::stoi(temp));
                temp = "";
            }
            i++;
        }
        if (!tempData.empty())
        {
            int maxTempData = *std::max_element(tempData.begin(), tempData.end());
            data.push_back(maxTempData);
        }
    }

    std::sort(data.begin(), data.end());
    if (data.empty())
    {
        std::cout << 0 << std::endl;
    }
    else
    {
        for (int i = 0; i < data.size(); i++)
        {
            std::cout << data[i];
            if (i != data.size() - 1)
            {
                std::cout << ", ";
            }
        }
        std::cout << std::endl;
    }
}

int main()
{
    string s;
    cin >> s;
    getValidNumbers(s);
}
