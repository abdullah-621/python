#include <iostream>
#include <stack>
using namespace std;

string makeGreat(string s)
{
  if (s.empty())
    return s;

  stack<char> st;

  for (int i = s.size() - 1; i >= 0; i--)
  {
    if (st.empty() || (abs(st.top() - s[i]) != 32))
    {
      st.push(s[i]);
    }
    else
    {
      st.pop();
    }
  }
  string str;

  while (!st.empty())
  {
    str += st.top();
    st.pop();
  }

  return str;
}

int main()
{
  string s = "LeEeetcode";
  cout << makeGreat(s);
}