#include <iostream>
using namespace std;

int Fact(int x) {
	if(x==0||x==1) {
		return 1;
	}
	else {
		return x*Fact(x-1);
	}
}