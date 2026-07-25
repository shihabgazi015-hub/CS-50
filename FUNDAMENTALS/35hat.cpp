#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;

class Hat {
public:
    vector<string> houses;

    Hat() {
        houses = {"Shah Paran", "Mujtaba", "Bijoy 24"};
    }

    void sort(const string& name) {
        int index = rand() % houses.size();
        cout << name << " is in " << houses[index] << endl;
    }
};

int main() {
    srand(time(0)); // seed random generator

    Hat hat;
    int i;

    cout << "How many times: ";
    cin >> i;

    for (int j = 0; j < i; j++) {
        hat.sort("Shihab");
    }

    return 0;
}
