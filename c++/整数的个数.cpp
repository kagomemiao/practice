// Description
// 给定k（1
// Input
// 输入有两行：第一行包含一个正整数k，第二行包含k个正整数，每两个正整数用一个空格分开。
// Output
// 输出有三行，第一行为1出现的次数，，第二行为5出现的次数，第三行为10出现的次数。
// Sample Input
// 5
// 1 5 8 10 5
// Sample Output
// 1
// 2
// 1
#include <iostream>
using namespace std;
int main() {
    int k;
    int c1 = 0, c5 = 0, c10 = 0;
    cin >> k;
    for(int i = 0; i < k; i++){
        int n;
        cin >> n;
        if(n == 1){
            c1++;
        }else if(n == 5){
            c5++;
        }else if(n == 10){
            c10++;
        }
    }
    cout << c1 << endl;
    cout << c5 << endl;
    cout << c10 << endl;
    return 0;
}