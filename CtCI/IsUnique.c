/*
Author: Liam Collier
Date: 05.11.2023
Problem: Implement an algorithm to determine if a string has all-unique characters.
Approach: Map each char to an array of booleans to check for duplicates in constant time.
*/

#include <stdbool.h>
#include <string.h>
#include <stdio.h>

#define ARR_LEN 256                         //Set ARR_LEN to 256 for extended ASCII range.

bool isUnique(char*pStr) {
    int len = strlen(pStr);
    if (len > ARR_LEN) {                    //Pigeon hole principle, more chars in str than possible unique chars.
        return false;
    }
    bool Arr[ARR_LEN];                      //Initialise array of 256 false bools.
    for (int i = 0; i < ARR_LEN; i++) {
        Arr[i] = false;
    }
    for (int i = 0; i < len; i++) {         //Iterate over string.
        int ch = *(pStr + i);               //Convert char to ASCII value.
        if (Arr[ch]) {                      //Char already found, not unique string.
            return false;
        }
        Arr[ch] = true;                     //Mark char as found in array.
    }
    return true;                            //No duplicates found.
}

int main(void) {                            //Run for testing.
    char lngstr[260];
    for (int i = 0; i < 260; i++) {
        lngstr[i] = 'a';
    }
    printf("test: %d\n", isUnique("test"));
    printf("uniqestr: %d\n", isUnique("uniqestr"));
    printf("Test: %d\n", isUnique("Test"));
    printf("Long String: %d\n", isUnique(lngstr));
    return 0;
}