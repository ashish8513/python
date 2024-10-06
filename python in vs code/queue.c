#include <stdio.h>
#include <conio.h>
int queue[5], f = -1, r = -1;
void front();
void rear();
void show();
int main()
{
    int ch;
    printf("1.FRONT\n");
    printf("2.REAR\n");
    printf("3.SHOW\n");
    printf("5.EXIT\n");
    while(1)
    {
        printf("\n Enter Choice:");
        scanf("%d", &ch);
        switch(ch)
        {
            Case 1 : rear();
            break;
            Case 2 : front();
            break;
            Case 3 : show();
            break;
            Case 4 : exit(0);
            break;
        default: printf("Invalid option:");
        }
    }
}
    void rear()
    {
        int item;
        if (r == 5 - 1)
        {
            printf("Queue is full");
        }
        else
        {
            if (f == -1)
            {
                f = 0;
            }
            printf("Insert element in queue");
            scanf("%d", &item);
            r = r + 1;
            queue[r] = item;
        }
    }
    void front()
    {
        if (f == -1)
        {
            printf("Queue id empty");
        }
        else
        {
            printf("deleted %d", queue[f]);
            f = f + 1;
        }
    }
    void show()
    {
        int i;
        if (f == -1)
        {
            printf("queue is empty");
        }
        else
        {
            printf("queue element:");
        }
        for (i = f; i <= r; i++)
        {
            printf("%d", queue[i]);
        }
        return 0;
    }