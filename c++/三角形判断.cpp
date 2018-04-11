// Description
// 输入三个正整数表示三条边的长度，判断这三条边能否构成一个三角形，如果能，则输出“yes”，否则输出“no”。
// Input
// 输入是三个正整型数，分别表示三条边的长度。
// Output
// yes 或者 no
// Sample Input
// 3 4 5
// Sample Output
// yes
#include <iostream>
using namespace std;
int main() {
    float a,b,c;
    cin >> a >> b >> c;
    if(a > 0 && b > 0 && c > 0)
        if(a + b > c && a + c > b && b + c > a)
            cout << "yes" << endl;
        else
            cout << "no" << endl;
    return 0;
}