#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>

using namespace std;

float num[100001];
int n, k;
void print(int num, int div) {
	num = num / div;
	if (num % 10 >= 5) num += 10;
	num /= 10;
	cout << num / 100 << '.' << (num/10) %10<<num % 10 << '\n';
}
int main() {
	cin >> n >> k;
	
	for (int i = 0; i < n; i++) {
		double t;
		cin >> t;
		num[i]=t*1000;
	}
	sort(num, num+n);
	
	//절사평균
	int sum = 0;
	for (int i = k; i <= n - 1 - k; i++) {
		sum += num[i];
	}
	int sum1 = 0;
	sum1 = sum + k * (num[k] + num[n - k - 1]);
	print(sum, n - 2 * k);
	print(sum1, n);
}


