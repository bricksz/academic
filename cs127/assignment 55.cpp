// terry huang
// 4/16/2018
// assignment 55

#include <iostream>
using namespace std;

int main()
{
    double miles;
    cout << "Enter miles: ";
    cin >> miles;

	double km;
    km = miles * 0.621371;

    cout << miles << " Miles is " << km << " Kilometers\n";
    return 0;
}