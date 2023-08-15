#include <iostream>
#include <vector>
#include <array>

using namespace std;

int main()
{
    // Khởi tạo vector fib chứa các số Fibonacci nhỏ hơn 901
    vector<array<long long, 2>> fib(901);
    array<long long, 2> preCheck = {1, 0};
    fib[1] = preCheck;
    array<long long, 2> check = {0, 1};
    fib[2] = check;

    // Tính các số Fibonacci từ 3 đến 900 và lưu vào vector fib
    for (long long i = 3; i < 901; ++i)
    {
        array<long long, 2> new_one;
        new_one[0] = preCheck[0] + check[0];
        new_one[1] = preCheck[1] + check[1];
        fib[i] = new_one;

        preCheck = check;
        check = new_one;
    }

    // Đọc số lượng truy vấn t
    long long t;
    cin >> t;

    while (t--)
    {
        long long n, k;
        cin >> n >> k;

        // Xử lý trường hợp k >= 901
        if (k >= 901)
        {
            cout << 0 << endl;
            continue;
        }

        // Lấy giá trị Fibonacci thứ k từ vector fib
        array<long long, 2> val = fib[k];
        long long result = 0;

        // Tính số cách phân tích n thành tổng của k số nguyên không âm
        for (long long i = 0; i <= n; ++i)
        {
            long long temp = (n - val[0] * i);
            if (temp % val[1] == 0 && temp / val[1] >= i)
            {
                ++result;
            }
        }

        // In kết quả số cách phân tích
        cout << result << endl;
    }

    return 0;
}
