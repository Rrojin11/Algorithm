#include "pch.h"
#include <iostream>
#include <cstdlib>
using namespace std;

bool c[10]; //false로 초기화 배열
int a[10]; //0으로 초기화 배열 

void go(int index, int n, int m) {
	if (index == m) {
		for (int i = 0; i < m; i++) {
			cout << a[i];
			if (i != m - 1) cout << ' ';
		}
		cout << '\n';
	}
	for (int i = 0; i < n; i++) {
		if (c[i]) continue;
		c[i] = true; a[index] = i;
		go(index + 1, n, m);
		c[i] = false;
	}

	return;
}
int main() {
	int n, m;
	//cout << a[9];
	cin >> n >> m;
	go(0, n, m);
	return 0;
}
