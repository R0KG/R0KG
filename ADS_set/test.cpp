#include <iostream>

int main() {
    int x = 42;
    int* ptr1 = &x; // pointer to int
    int** ptr2 = &ptr1; // pointer to a pointer to int

    std::cout << "x: " << x << std::endl;
    std::cout << "*ptr1: " << *ptr1 << std::endl;
    std::cout << "**ptr2: " << **ptr2 << std::endl;

    return 0;
}
                                                                                            