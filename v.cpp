#include <iostream>
using namespace std;

string greatest(int x, int y, int z)
{
  if (x > y && x > z)
  {
    return "x is greatest";
  }
  else if (y > x && y > z)
  {
    return "y is greatest";
  }
  else
  {
    return "z is greatest";
  }
}

int main()
{
  int x, y, z;

  cout << "Enter x: ";
  cin >> x;

  cout << "Enter y: ";
  cin >> y;

  cout << "Enter z: ";
  cin >> z;

  string result = greatest(x, y, z);
  cout << result << endl;

  return 0;
}