#include <iostream>
#include<cmath>
using namespace std;
int main()
{
	int x,a;
	cin >> x >> a;
	if (x > 10) {
		cout << 1 / x;
	}
	else if ((x >= -10) && (x <= 10)) {
		cout << a * (x ^ 2);
	}else{
		cout << sin(x);
	}
	
}