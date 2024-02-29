#include <stdio.h>
#include <algorithm>

int list[1000000];

int main(void) {
  int number, i;
  scanf("%d", &number);
  for(i = 0; i < number; i++) scanf("%d", &list[i]);
  std::sort(list, list+number);
  for(i=0; i<number;i++) printf("%d\n", list[i]);
  return 0;
}