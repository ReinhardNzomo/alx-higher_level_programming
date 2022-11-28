#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - count the cycles of list
 * @list: pointer to the header lists
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
    listint_t *cur;

    if (list)
    {
        while (list != NULL)
        {
            cur = list;
            list = list->next;

            if (cur <= list)
            {
                return (1);
            }
        }
        
        return (0);
    }
    
    return (0);
}
