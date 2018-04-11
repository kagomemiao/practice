// Description
// 将一个数组中的值按逆序重新存放。例如，原来的顺序为8,6,5,4,1。要求改为1,4,5,6,8。
// Input
// 输入为两行：第一行数组中元素的个数n（1 < n < 100)，第二行是n个整数，每两个整数之间用空格分隔。
// Output
// 输出为一行：输出逆序后数组的整数，每两个整数之间用空格分隔。
// Sample Input
// 5
// 8 6 5 4 1
// Sample Output
// 1 4 5 6 8
#include <iostream>
using namespace std;
int main() {
    int n,a[100],i,j;
    cin >> n;
    if(n > 1 && n < 100)
        for(i = 0; i < n; i++)
            cin >> a[i];
        for(j = n - 1; j >= 0; j--)
            cout << a[j] << " ";
    return 0;
}