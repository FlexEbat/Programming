#include <iostream>

using namespace std;


int main () {
    unsigned u = 10;
    int i = -42;
    cout << i + i << endl; // выводит -84
    cout << u + i << endl; // при 32 битовом int, выводит 4294967264
cout << "" << endl;
    unsigned u1 = 42, u2 = 10;
    cout << u1 - u2 << endl; // ok: result = 32
    cout << u2 - u1 << endl; // ok: но с обращение значения
    cout << "" << endl;

    // Цикл никогда не закончится.
    // for (unsigned i = 10; i >=0; --i)
    // cout << i << endl;
    cout << "" << endl;

    unsigned v = 11;

    while (v > 0) {
        --v;
        cout << v << endl;
    }

    return 0;
}