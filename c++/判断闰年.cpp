// Description
// 正常情况下一年有365天，但是闰年的时候，一年有366天。现在给定一个年份，请你判断它是不是闰年
// Input
// 一行一个整数，表示年份
// Output
// 闰年输出"YES"
// 否则输出"NO"
// Sample Input
// 2000
// Sample Output
// YES
// Hint
// 1900年不是闰年
#include <iostream>
using namespace std;
int main() {
    int year;
    cin >> year;
    if(year % 4 == 0 && year % 100 != 0 || year % 400 == 0)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}