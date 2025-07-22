struct Node
{
  // int data;
  // int size;
  // int *arr;

  Node(int n, int data, int size, int *arr){
    data = n;
    size = 0;
    arr = new int[n];
  }
};
