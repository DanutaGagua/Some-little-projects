#include <stdio.h>
#include <stdlib.h>

struct Ring
{
    int num;
    struct Ring* next;
};

void add(struct Ring **head, int x);
void show(struct Ring *head);
void del(struct Ring **head, int k);
void sort(struct Ring *head);

int main()
{
    struct Ring *head = NULL;
    int x, k, s;

    while (1)
    {
        printf("Select operation:\n");
        printf("1 - Add node to ring\n");
        printf("2 - Delete node from ring\n");
        printf("3 - Show ring\n");
        printf("4 - Sort values in ring\n");
        printf("5 - Close program\n");

        //fflush(stdin);
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
            show(head);
            break;
        case 4:
            sort(head);
            break;
        case 5:
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
    }
    else
    {
        struct Ring *p, *tail = *head;

        p = (struct Ring*)calloc(1, sizeof(struct Ring));
        p->next = (*head);
        p->num = x;

        while (tail->next != (*head))
        {
            tail = tail->next;
        }

        tail->next = p;
        (*head) = p;
    }

    printf("Added\n");
}

void show(struct Ring *head)
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
        printf("%d\n", curr->num);
        curr = curr->next;
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
        struct Ring *pred = *head, *curr, * temp;
        int i;
        curr = pred->next;

        for (i = 0; i < k-1; i++)
        {
            pred = curr;
            curr = pred->next;
        }

        temp = curr;
        pred->next = curr->next;
        if (curr == (*head))
        {
            (*head) = pred->next;
        }

        free(temp);
    }

    printf("Deleted\n");
}

void sort(struct Ring *head)
{
    if (head == NULL)
    {
        printf("Ring is empty.\n");
        return;
    }

    struct Ring *curr, *next;

    curr = head;

    while (curr->next != head)
    {
        next = curr;

        do
        {
            next = next->next;

            if (next->num < curr->num)
            {
                int x = next->num;
                next->num = curr->num;
                curr->num = x;
            }
        } while (next->next != head);

        curr = curr->next;
    }

    printf("Sorted\n");
}
