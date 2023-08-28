#include <stdio.h>

char flag[] = "greyhats{REDACTED}";

void vulnerable_function() {
    char buffer[100];
    printf("Flag is at %p\nEnter your input: \n", &flag);
    fgets(buffer, sizeof(buffer), stdin);
    printf(buffer);
    printf("\n");
}

int main() {
	setbuf(stdin, 0);
	setbuf(stdout, 0);
    vulnerable_function();
    return 0;
}
