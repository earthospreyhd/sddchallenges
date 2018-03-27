#include <stdio.h>//include library which has printf so we can print to standard output

int main () {
    //declare int array with 100 values
    int doors[100];
    //declare int which will hold the amount of open doors
    int openDoorCount;

    for (int i = 0; i < 100; i++) {
        //initalize all values to 1
        doors[i] = 1;
    }
    //iterate for all of the people (1 - 100)
    for (int i = 1; i < 101; i++) {
        //iterate in multiples of the person's number
        for (int y = i; y < 101; y+= i) {
                //change the value of the door from open to closed or vice versa
                doors[y - 1] = doors[y - 1] * -1;
        }
    }
    //interate over the doors array
    for (int j = 0; j < 101; j++) {

        if (doors[j] == -1) {

            //if the door is open (is equal to -1) increase the counter of open doors
            //and print out the current door
            printf("door %d is open\n", j + 1);
            openDoorCount++;
            
        }
    }
    //print how many open doors there are
    printf("There are %d open doors\n", openDoorCount);
}