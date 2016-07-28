#include <iostream>
using namespace std;

int fact(int x) {

  return fact(x-1);
}

int main(int argc, char const *argv[]) {
  cout << fact(5) << endl;
  return 0;
}
