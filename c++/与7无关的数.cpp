// Description
// 一个正整数,如果它能被7整除,或者它的十进制表示法中某个位数上的数字为7,则称其为与7相关的数.现求所有小于等于n(n<100)的与7无关的正整数的平方和。
// Input
// 输入为一行,正整数n,(n<100)
// Output
// 输出小于等于n的与7无关的正整数的平方和。
// Sample Input
// 21
// Sample Output
// 2336
#include <iostream>
using namespace std;
int main() {
    int n,i,sum = 0;
    cin >> n;
    if(n < 100 && n > 0)
        for(i = 1; i <= n; i++)
            if(i % 7 != 0 && i % 10 != 7 && i/10 != 7)
                sum += i * i;
        cout << sum << endl;
    return 0;
}