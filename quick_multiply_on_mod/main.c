#include <stdio.h>
#include <stdlib.h>

int quick_multiply_on_mod(n, degree, mod);

int main()
{
    int n, degree, mod;

    printf("Enter numbers:\t");

    while(scanf("%d %d %d", &n, &degree, &mod))
    {
        if (degree >= 0 && mod > 0)
        {
            break;
        }
        else
        {
            printf("Enter right numbers:\t");
        }
    }

    printf("Answer:\t %d", quick_multiply_on_mod(n, degree, mod));
    return 0;
}

int quick_multiply_on_mod(n, degree, mod)
{
    int value;

    if (degree == 0)
    {
        return 1;
    }
    else
    {
        value = quick_multiply_on_mod(n, degree / 2, mod);
    }

    if (degree % 2 == 0)
    {
        return value*value % mod;
    }
    else
    {
        return n*value*value % mod;
    }
}
