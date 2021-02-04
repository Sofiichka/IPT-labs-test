#include <iostream>
#include <cmath>

using namespace std;
int main()
{
	double result, x, a;
	cout << "Input variables x and a"<<endl;
	cin >> x >> a;
	if (((x - a) == 0) || ((2*x + 3*a)<0)) {
		cout << "Invalid variables (x-a = 0) or sqrt <0"; 
		return 0;
	}else{
		result = tan(1 / (x - a)) - sqrt(2 * x + 3 * a);
		cout << result << endl;
	}	
	return 0;
}
