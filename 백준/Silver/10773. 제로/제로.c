#include <stdio.h>

int stack[1000000];
int top = -1;

void push(int n){
  top++;
  stack[top] = n;
}

void pop(){
  top --;
}

int main(void) {
  int K, tmp, i, sum = 0;
  scanf("%d", &K);
  for(i = 0; i < K; i++){
    scanf("%d", &tmp);
    if(tmp == 0) pop();
    else push(tmp);
  }
  
  for(i = 0; i <= top; i++) sum += stack[i];
  printf("%d\n", sum);
  return 0;
}