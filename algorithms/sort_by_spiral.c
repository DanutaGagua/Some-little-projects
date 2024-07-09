#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define n 5
#define m 10

void change(int a[n][m], int x1, int y1, int x2, int y2);
void init(int a[n][m]);
void subm(int a[n][m], int i, int j, int i1, int i2, int j1, int j2);

int main()
{
    int a[n][m], i, j, i1 = 0, i2 = n, j1 = 0 , j2 = m, x, y;

    init(a);

    i = 0;
    j = 0;
    while (i1 < i2 && j1 < j2)
    {
        i = i1;
        i1++;
        for (j = j1; j < j2; j++)
        {
            for (x = j+1; x < j2; x++)
            {
                if (a[i][j] > a[i][x])
                {
                    change(a, i, j, i, x);
                }
            }

            subm(a, i, j, i1, i2, j1, j2);
        }

        j2--;
        j = j2;

        for (i = i1; i < i2; i++)
        {
            for (x = i+1; x < i2; x++)
            {
                if (a[i][j] > a[x][j])
                {
                    change(a, i, j, x, j);
                }
            }

            subm(a, i, j, i1, i2, j1, j2);
        }

        i2--;
        i = i2;

        for (j = j2-1; j >= j1; j--)
        {
            for (x = j1; x < j; x++)
            {
                if (a[i][j] > a[i][x])
                {
                    change(a, i, j, i, x);
                }
            }

            subm(a, i, j, i1, i2, j1, j2);
        }

        j = j1;
        j1++;

        for (i = i2-1; i >= i1; i--)
        {
            for (x = i1; x < i; x++)
            {
                if (a[i][j] > a[x][j])
                {
                    change(a, i, j, x, j);
                }
            }

            subm(a, i, j, i1, i2, j1, j2);
        }

    }

    printf("\n");
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }

    return 0;
}

void change(int a[n][m], int x1, int y1, int x2, int y2)
{
    int t = a[x1][y1];
    a[x1][y1] = a[x2][y2];
    a[x2][y2] = t;
}

void init(int a[n][m])
{
    int i, j;

    srand(time(NULL));

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            a[i][j] = rand()%100;
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }
}

void subm(int a[n][m], int i, int j, int i1, int i2, int j1, int j2)
{
    int x, y;

    for (x = i1; x < i2; x++)
    {
        for (y = j1; y < j2; y++)
        {
            if (a[i][j] > a[x][y])
            {
                change(a, i, j, x, y);
            }
        }
    }
}
