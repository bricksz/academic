// terry huang
// 4/18/2018
// assignment 59

#include <iostream>
using namespace std;

int main()
{
	int x;
	cout << "Please enter age: ";
	cin >> x;
	
	while (x < 0)
	{
		cout << "Entered a negative number.\n";
		
		int y;
		cout << "Please enter age: ";
		cin >> y;
		
		x = y;
		}

	cout << "You entered your age as: " << x <<"\n";
		
	return 0;
}
