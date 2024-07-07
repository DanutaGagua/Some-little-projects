#include <stdio.h>
#include <stdlib.h>

struct Ring
{
    int num;
    struct Ring* next;
    struct Ring* pred;
};

void add(struct Ring **head, int x);
void show(struct Ring *head, int dir);
void del(struct Ring **head, int k);
void sort(struct Ring *head, int dir);

int main()
{
    struct Ring *head = NULL;
    int x, k, s;

    while (1)
    {
        printf("Select operation:\n");
        printf("1 - Add node to ring\n");
        printf("2 - Delete node from ring\n");
        printf("3 - Show ring clockwise\n");
        printf("4 - Show ring counter clockwise\n");
        printf("5 - Sort values in ring clockwise\n");
        printf("6 - Sort values in ring counter clockwise\n");
        printf("7 - Close program\n");

        scanf("%d", &s);
        switch(s)
        {
        case 1:
            printf("Enter number: ");
            scanf("%d", &x);
            add(&head, x);
            break;
        case 2:
            printf("Enter index after head of ring: ");
            scanf("%d", &k);
            del(&head, k);
            break;
        case 3:
            show(head, 1);
            break;
        case 4:
            show(head, 0);
            break;
        case 5:
            sort(head, 1);
            break;
        case 6:
            sort(head, 0);
            break;
        case 7:
            return 0;
        }

        printf("\n");
    }

    return 0;
}

// do work
void add(struct Ring **head, int x)
{
    if ((*head) == NULL)
    {
        (*head) = (struct Ring*)malloc(sizeof(struct Ring));
        (*head)->num = x;
        (*head)->next = (*head);
        (*head)->pred = (*head);
    }
    else
    {
        struct Ring *p, *tail = (*head)->pred;

        p = (struct Ring*)calloc(1, sizeof(struct Ring));
        p->next = (*head);
        p->num = x;
        p->pred = tail;

        tail->next = p;
        (*head)->pred = p;
        (*head) = p;
    }

    printf("Added\n");
}

void show(struct Ring *head, int dir)
{
    if (head == NULL)
    {
        printf("Ring is empty.\n");
        return;
    }

    printf("\nRing nodes:\n");

    struct Ring *curr = head;
    do
    {
        printf("%p %d %p %p\n", curr, curr->num, curr->next, curr->pred);
        curr = dir ? curr->next : curr->pred;
    } while (curr != head);
}

void del(struct Ring **head, int k)
{
    if ((*head) == NULL)
    {
        printf("Ring is empty.\n");
        return;
    }

    if ((*head) == (*head)->next)
    {
        free(*head);
    }
    else
    {
        struct Ring *pred = *head, *curr = *head, *next;
        int i;

        for (i = 0; i < k; i++)
        {
            curr = curr->next;
        }

        next = curr->next;
        pred = curr->pred;

        pred->next = next;
        next->pred = pred;

        if (curr == (*head))
        {
            (*head) = next;
        }

        free(curr);
    }

    printf("Deleted\n");
}

void sort(struct Ring *head, int dir)
{
    if (head == NULL)
    {
        printf("Ring is empty.\n");
        return;
    }

    struct Ring *curr, *next;

    curr = head;

    while (curr->next != head && dir || curr->pred != head && !dir)
    {
        next = curr;

        do
        {
            next = dir ? next->next : next->pred;

            if (next->num < curr->num)
            {
                int x = next->num;
                next->num = curr->num;
                curr->num = x;
            }
        } while (next->next != head && dir || next->pred != head && !dir);

        curr = dir ? curr->next : curr->pred;
    }

    printf("Sorted\n");
}
