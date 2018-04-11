// Description
// 计算非负整数 m 到 n（包括m 和 n ）之间的所有奇数的和，其中，m 不大于 n，且n 不大于300。例如 m=3, n=12, 其和则为：3+5+7+9+11=35
// Input
// 两个数 m 和 n，两个数以空格间隔，其中 0 <= m <= n <= 300 。
// Output
// 奇数之和
// Sample Input
// 7 15
// Sample Output
// 55
#include <iostream>
using namespace std;
int main() {
    int m,n,i,sum;
    cin >> m >> n;
    if(m >= 0 && m <= n && n <= 300)
        if(m % 2 == 0){
            for(i = m + 1; i <= n; i = i + 2)
                sum += i;
            cout << sum << endl;
        }
        else{
            for(i = m; i <= n; i = i + 2)
                sum += i;
            cout << sum << endl;
        }
    return 0;
}