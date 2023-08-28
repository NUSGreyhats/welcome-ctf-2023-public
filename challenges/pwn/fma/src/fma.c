#include <stdio.h>

char flag[] = "greyhats{f0rmAt_5trin9_vuln3rabi1ities_4r3_d4ngerous}";

void vulnerable_function() {
    char buffer[100];
    printf("Flag is at %p\nEnter your input: \n", &flag);
    fgets(buffer, sizeof(buffer), stdin);
    printf(buffer);
    printf("\n");
}

int main() {
	setbuf(stdout, 0);
	setbuf(stdin, 0);
    vulnerable_function();
    return 0;
}
