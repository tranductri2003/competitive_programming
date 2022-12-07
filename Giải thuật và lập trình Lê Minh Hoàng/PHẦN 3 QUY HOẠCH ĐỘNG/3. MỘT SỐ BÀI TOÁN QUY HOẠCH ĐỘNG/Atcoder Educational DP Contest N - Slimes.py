"""
Có N cục thạch xếp thành một hàng ngang. Ban đầu, cục thạch thứ i, đếm từ trái sang, có kích thước ai.

Taro cố gắng ghép những cục thạch này lại với nhau để tạo thành một cục thạch lớn hơn. Anh ấy sẽ liên tục lặp lại thao tác sau cho đến khi chỉ còn lại một cục thạch duy nhất:

Taro chọn hai cục thạch kế bên nhau và ghép chúng lại. Cục thạch mới sẽ có kích thước là x+y, x và y là kích thước của hai cục thạch được chọn trước khi được ghép. Chi phí phát sinh là x+y và vị trí tương đối giữa các cục thạch là không thay đổi trong suốt quá trình kết hợp các cục thạch.
Taro là một người tiết kiệm. Bạn hãy giúp Taro tìm chi phí phát sinh nhỏ nhất có thể.

Input
Dòng đầu tiên chứa số nguyên N(2≤N≤400) là số lượng cục thạch.

Dòng thứ hai chứ N số nguyên a1,a2,a3,...,an(1≤ai≤109).

Output
Dòng duy nhất là chi phí phát sinh nhỏ nhất."""

#dp[i][j]: chi phí thấp nhất để ghép cục thạch i...j