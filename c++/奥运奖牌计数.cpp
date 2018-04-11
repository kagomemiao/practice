// Description
// 2008年北京奥运会，A国的运动员参与了n天的决赛项目(1≤n≤17)。现在要统计一下A国所获得的金、银、铜牌数目及总奖牌数。
// Input
// 第1行是A国参与决赛项目的天数n，其后有n行，每一行是该国获得的金、银、铜牌数目，用空格隔开。
// Output
// 1行，包括4个整数，为A国所获得的金、银、铜牌总数及总奖牌数，用空格隔开。
// Sample Input
// 3
// 1 0 3
// 3 1 0
// 0 3 0
// Sample Output
// 4 4 3 11
#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int c1 = 0, c2 = 0, c3 = 0, c4 = 0;
    if(n >= 1 && n <= 17)
        for(int i = 0; i < n; i++){
            int gold,silver,bronze;
            cin >> gold >> silver >> bronze;
            c1 += gold;
            c2 += silver;
            c3 += bronze;
        }
        c4 = c1 + c2 + c3;
        cout << c1 << " " << c2 << " " << c3 << " " << c4 <<endl;
    return 0;
}