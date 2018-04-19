// terry huang
// 4/18/2018
// assignment 57

#include <iostream>
using namespace std;

int main()
{
	int x;
	cout << "Enter month (as a number): ";
	cin >> x;
	
	if (x < 3 || x > 11)
	{
		cout << "Happy Winter\n";
		}
	else if (x >= 3 && x < 7)
	{
		cout << "Happy Spring\n";
		}
	else if (x >= 7 && x < 9)
	{
		cout << "Happy Summer\n";
		}
	else 
	{
		cout << "Happy Fall\n";
		}
	return 0;
}
