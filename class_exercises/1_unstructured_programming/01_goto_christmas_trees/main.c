#include <stdio.h>

int main(void){
    int height, row, i;
    char c;

begin:
    if (scanf("%d", &height) != 1) goto end;
    if (height < 1) goto begin;
    c = '*';
    if (height % 2) c = '#';
    row = 1;

draw_row:
    printf("%*s", height - row, "");
    i = 0;

draw_char:
    putchar(c);
    i++;
    if (i < 2 * row - 1) goto draw_char;
    putchar('\n');
    row++;
    if (row <= height) goto draw_row;
    if (height != 7) goto begin;

end:
    return 0;
}