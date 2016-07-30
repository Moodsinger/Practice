#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  cout << "Ham Sandwich\n";
  char x;
  cout << "Enter a string please: ";
  cin << x;
  cout << "You entered " + char(x) + " right?" << endl;
  return 0;
}
