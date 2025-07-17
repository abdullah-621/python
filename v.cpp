#include <iostream>
#include <string>
using namespace std;

int main() {
  int n;
  cout << "Enter n : ";
  cin >> n;
  for (int i = 1; i <= n; i++)
  {
    cout << (n - i, ' ') << (2 * i - 1, '*') << endl;
  }
  
  return 0;
}