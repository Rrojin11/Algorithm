#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <tuple>
#include <deque>
#include <cmath>
using namespace std;
int a[21];
int n, s;
int ans = 0;
void go(int idx, int tmp) {
	if (idx==n) {
		if(tmp==s) ans++;
		return;
	}

	go(idx + 1, tmp + a[idx]);
	go(idx + 1, tmp);
}
int main(){
	
	cin >> n >> s;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	go(0, 0);
	if (s == 0) ans--;
	cout << ans;
}
