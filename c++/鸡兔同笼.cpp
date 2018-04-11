// Description
// 一个笼子里面关了鸡和兔子（鸡有2只脚，兔子有4只脚，没有例外）。已经知道了笼子里面鸡和兔子的总数a和脚的总数b，问笼子里面有多少只鸡，有多少只兔子
// Input
// 输入仅一行，包括两个整数a和b，我们保证输入的合法性
// Output
// 输出也是一行，输出鸡的个数和兔子的个数，中间用空格隔开
// Sample Input
// 5 14
// Sample Output
// 3 2
#include <iostream>
using namespace std;
int main() {
    int a,b,j,t;
    cin >> a >> b;
    for(j = 0; j <= a; j ++){
        t = a - j;
        if(j + t == a && j *2 + t * 4 == b)
            cout << j << " " << t << endl;
    }
    return 0;
}