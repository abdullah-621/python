#include <iostream>
#include <deque>
using namespace std;

int main() {
  deque<int> q;

  q.push_back(1);
  q.push_back(2);
  q.push_back(3);

  cout << q[2];
  return 0;
}