#include <iostream>
using namespace std;

int main(){
    int n = 13,i,j,count = 0;
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