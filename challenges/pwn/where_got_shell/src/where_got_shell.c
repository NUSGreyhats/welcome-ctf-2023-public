#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <sys/types.h>

void win() {
  system("cat flag.txt");
}

int main(int argc, char **argv) {

  setvbuf(stdout, NULL, _IONBF, 0);

  char buf[256];
  unsigned long int address;
  unsigned long int value;

  puts("I'll let you write one 8 byte value to memory.\nWhere would you like to write this 8 byte value: ");
  scanf("%lx", &address);

  sprintf(buf, "What value to write to %p: ", address);
  puts(buf);
  scanf("%lx", &value);

  sprintf(buf, "Okay, writing %lx to %p", value, address);
  puts(buf);
  *(unsigned long int *)address = value;

  puts("Okay, exiting now...\n");
  exit(1);
}