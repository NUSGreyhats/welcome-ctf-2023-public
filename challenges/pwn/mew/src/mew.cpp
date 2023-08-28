#include <iostream>
#include <functional>

#define MAXSZ 100
typedef unsigned long long num;


void sort(num* arr, num len) {
    num tmp = 0;
    for(num i = 0; i <= len; i++) {
        for(num j = i; j <= len; j++) {
            if (arr[i] < arr[j]) continue;
            tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
    }
}

num ARR[MAXSZ];

std::function<int(int)> running_mean;

// ignore
void setup() {
	setbuf(stdin, nullptr);
	setbuf(stdout, nullptr);
}

void win() {
	system("/bin/sh");
}

void init_running_mean() {
	num count = 0;
	num sum = 0;
	running_mean = [&](int v) {
		sum += v;
		count++;
		return sum / count;
	};
}

void run() {
	init_running_mean();
	
	std::cout << "Welcome to Mew, the Mean calculator!" << std::endl;
	
	while (true) {
		std::cout << "1. Enter a number" << std::endl;
		std::cout << "2. Read a number" << std::endl;
		std::cout << "3. Sort" << std::endl;
		std::cout << "4. Re-init running mean" << std::endl;
		std::cout << "5. Statistics" << std::endl;
		std::cout << "> ";

		int opt;
		std::cin >> opt;
		switch(opt) {
			case 1: {
				int index; num value;

				std::cout << "Enter index: ";
				std::cin >> index;
				if (index >= MAXSZ || index < 0) {
					std::cout << "Bad index!" << std::endl;
					continue;
				}
				std::cout << "Enter value: ";
				std::cin >> value;
				ARR[index] = value;
				break;
			}
			case 2: {
				int index;
				std::cout << "Enter index: ";
				std::cin >> index;
				if (index > MAXSZ || index < 0) {
					std::cout << "Bad index!" << std::endl;
					continue;
				}
				std::cout << "Value: " << ARR[index] << std::endl;
				break;
			}
			case 3:
				sort(ARR, MAXSZ);
				break;
			case 4:
				init_running_mean();
				break;
			case 5: {
				std::cout << "Statistics:" << std::endl;
				int t = 0;
				for(int i = 0; i < MAXSZ; i++) {
					t = running_mean(ARR[i]);
				}
				std::cout << "Mean: " << t << std::endl;
				break;
			}
			default:
				return;
		}
	}
}

int main() {
	setup();
	run();
    return 0;
}
