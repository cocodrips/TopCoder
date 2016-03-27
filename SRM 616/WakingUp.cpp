#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
#include <typeinfo>
#include <fstream>

using namespace std;

class WakingUp {
    public:
    int maxSleepiness(vector<int> period, vector<int> start, vector<int> volume, int D) {
        int pp = 9 * 8 * 7 * 5;
        int mini = 1000000000;
        int nemuke = 0;

        for (int t = 0; t < pp; ++t){
            for (int i = 0; i < period.size(); ++i){
                int s = start[i];
                int v = volume[i];
                int p = period[i];
                if(t - s >= 0 && (t - s) % p == 0){
                    nemuke -= v;
                }
            }
            mini = min(mini, nemuke);
            nemuke += D;
        }
        int mini1 = mini;

        for (int t = pp; t < pp * 2; ++t){
            for (int i = 0; i < period.size(); ++i){
                int s = start[i];
                int v = volume[i];
                int p = period[i];
                if(t - s >= 0 && (t - s) % p == 0){
                    nemuke -= v;
                }
            }
            mini = min(mini, nemuke);
            nemuke += D;
        }
        int mini2 = mini;

        if (mini1 != mini2 or mini > 0){
            return -1;
        }
        return -mini;

    }
};

// CUT begin
ifstream data("WakingUp.sample");

string next_line() {
    string s;
    getline(data, s);
    return s;
}

template <typename T> void from_stream(T &t) {
    stringstream ss(next_line());
    ss >> t;
}

void from_stream(string &s) {
    s = next_line();
}

template <typename T> void from_stream(vector<T> &ts) {
    int len;
    from_stream(len);
    ts.clear();
    for (int i = 0; i < len; ++i) {
        T t;
        from_stream(t);
        ts.push_back(t);
    }
}

template <typename T>
string to_string(T t) {
    stringstream s;
    s << t;
    return s.str();
}

string to_string(string t) {
    return "\"" + t + "\"";
}

bool do_test(vector<int> period, vector<int> start, vector<int> volume, int D, int __expected) {
    time_t startClock = clock();
    WakingUp *instance = new WakingUp();
    int __result = instance->maxSleepiness(period, start, volume, D);
    double elapsed = (double)(clock() - startClock) / CLOCKS_PER_SEC;
    delete instance;

    if (__result == __expected) {
        cout << "PASSED!" << " (" << elapsed << " seconds)" << endl;
        return true;
    }
    else {
        cout << "FAILED!" << " (" << elapsed << " seconds)" << endl;
        cout << "           Expected: " << to_string(__expected) << endl;
        cout << "           Received: " << to_string(__result) << endl;
        return false;
    }
}

int run_test(bool mainProcess, const set<int> &case_set, const string command) {
    int cases = 0, passed = 0;
    while (true) {
        if (next_line().find("--") != 0)
            break;
        vector<int> period;
        from_stream(period);
        vector<int> start;
        from_stream(start);
        vector<int> volume;
        from_stream(volume);
        int D;
        from_stream(D);
        next_line();
        int __answer;
        from_stream(__answer);

        cases++;
        if (case_set.size() > 0 && case_set.find(cases - 1) == case_set.end())
            continue;

        cout << "  Testcase #" << cases - 1 << " ... ";
        if ( do_test(period, start, volume, D, __answer)) {
            passed++;
        }
    }
    if (mainProcess) {
        cout << endl << "Passed : " << passed << "/" << cases << " cases" << endl;
        int T = time(NULL) - 1411300665;
        double PT = T / 60.0, TT = 75.0;
        cout << "Time   : " << T / 60 << " minutes " << T % 60 << " secs" << endl;
        cout << "Score  : " << 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT)) << " points" << endl;
    }
    return 0;
}

int main(int argc, char *argv[]) {
    cout.setf(ios::fixed, ios::floatfield);
    cout.precision(2);
    set<int> cases;
    bool mainProcess = true;
    for (int i = 1; i < argc; ++i) {
        if ( string(argv[i]) == "-") {
            mainProcess = false;
        } else {
            cases.insert(atoi(argv[i]));
        }
    }
    if (mainProcess) {
        cout << "WakingUp (250 Points)" << endl << endl;
    }
    return run_test(mainProcess, cases, argv[0]);
}
// CUT end
