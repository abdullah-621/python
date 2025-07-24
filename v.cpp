#include <iostream>
using namespace std;

int main()
{
  string arr[] = {"abdullah", "al", "masum"};

  // string s = "";

  string s = "";
  for (auto word : arr)
  {
    s += word;
  }

  cout << s;
  return 0;
}