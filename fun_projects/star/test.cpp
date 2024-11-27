/**
 * C++ - a data race and synchronization.
 *
 * This example demonstrates a data race in C++ and some possible solutions.
 *
 */

#include <iostream>
#include <thread>
#include <atomic>
#include <mutex>
#include <vector>

unsigned int max = 10000000; // 10M 

int counter = 0;

// try swithing this atomic variable to unsigned int, long
// and check what you need to change in the code to make it work
std::atomic<int> counter_atomic = 0; 

std::mutex m;

void incr_counter_race()
{
    for (int i = 0; i < max; i++ ) {
        ++counter; // data race if not pretected
    }
}

void incr_counter_mutex()
{
    std::lock_guard lock(m); // lock
    for (int i = 0; i < max; i++ ) {
        // std::lock_guard lock(m); // which one is better?
        ++counter; // data race if not pretected
    }

    // we could have used the std::unique_lock
    // then we can unlock() explicity if needed
    // std::unique_lock lock(m); 
    
}

void incr_counter_atomic()
{
    for (int i = 0; i < max; i++ ) {
        ++counter_atomic; 
    }
}

int main()
{
    // spawn threads
    std::thread th0(incr_counter_race);
    std::thread th1(incr_counter_race);
    
    // wait for the threads to complete
    th0.join();
    th1.join();
    
    std::cout << "counter (no synchronization): " << counter << std::endl;

    counter = 0; // reset counter 

    std::thread th2(incr_counter_mutex);
    std::thread th3(incr_counter_mutex);
    
    th2.join();
    th3.join();

    std::cout << "counter (mutex): " << counter << std::endl;

    std::thread th4(incr_counter_atomic);
    std::thread th5(incr_counter_atomic);
    
    th4.join();
    th5.join();

    std::cout << "counter (atomic): " << counter_atomic << std::endl; 

    return 0;
}
