// Description
// 给定三角形的三边长度，根据海伦公式求出三角形面积。
// _____________________
// 海伦公式：S = √(p*(p-a)*(p-b)*(p-c)) 

// 其中a b c分别表示三角形的三条边的长度，p = (a+b+c)/2
// Input
// 第一行是一个整数n，表示的是输入数据有n行（n < 100）。
// 接下来的n行，每行有3个数，表示三角形的三条边的长度。
// Output
// 对每一个三角形，输出其面积，结果保留2位小数。
// Sample Input
// 1
// 3 4 5
// Sample Output
// 6.00
// Hint
// 开方运算可以使用sqrt函数
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    int n,i;
    float a,b,c,p,r;
    cin >> n;
    if(n < 100 && n > 0)
        for(i = 0; i < n; i++){
            cin >> a >> b >> c;
            if(a == 0 || b == 0 || c == 0 || a + b < c || a + c < b || b + c < a) continue;
            p = (a + b + c) / 2;
            r = (p * (p - a) * (p - b) * (p - c));
            a = 0, b = 0, c = 0;
            cout << fixed << setprecision(2) << sqrt(r) << endl;
        }
    return 0;
}