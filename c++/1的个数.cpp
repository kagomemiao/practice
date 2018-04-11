// Description
// 给定一个十进制正整数n，写下从1开始到n的所有整数，然后数一下其中所有出现的“1”的个数。例如当n=2时，写下1,2。这样只出现了1个“1”；当n=12时，写下1，2，3，4，5，6，7，8，9，10，11，12。这样出现了5个“1”。
// Input
// 正整数n
// Output
// “1”的个数
// Sample Input
// 12
// Sample Output
// Number of one in 12 is 5.
#include <iostream>
using namespace std;
int main(){
    int n,i,j,count = 0;
    cin >> n;
    for(i = 0; i <= n; i++){
        j = i;
        while(j != 0){
            if(j % 10 == 1)
                count++;
            j = j / 10;
        }
    }
    cout << "Number of one in " << n << " is " << count << endl;
    return 0;
}