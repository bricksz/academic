// terry huang
// 4/18/2018
// assignment 58

#include <iostream>
using namespace std;

int main()
{	
	float x;
	cout << "Enter the starting ammount: ";
	cin >> x;
	
	for (int i = 1 ; i <= 5; i++)
	{	
		x = x + (x * 0.1);
		cout << "Year " << i << " " << x <<"\n";
	}
return 0;
}
