/*
ID: wrwwctb1
TASK: checker
LANG: C++14
*/

#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <cassert>

#include <vector>
#include <deque>
#include <list>
#include <set> // has multiset
#include <map> // has multimap
#include <unordered_set> // has unordered_multiset
#include <unordered_map> // has unordered_multimap
#include <stack>
#include <queue> // has priority_queue

#include <algorithm>
#include <cmath>
#include <cfloat>
#include <ctime>
#include <climits>
#include <iomanip>
#include <cstring>

#define FOR( i, N ) for( int (i) = 0; (i) < (N); (i)++ )
//#define FOR_( i, start, endplusone ) for( int (i) = (start); (i) < (endplusone); (i)++ )
const double EPS = 1e-6;
const double PI = 3.141592653589793;
using namespace std;
// profile: 27196474









const int Nmax = 13;
int d1[2 * Nmax];
int d2[2 * Nmax];
int cc[Nmax + 1];
vector<int> history;
int cnt;
int N;
const string filename("checker");
string filenameo = filename + ".out";
string filenamei = filename + ".in";
ofstream fout(filenameo.c_str());
ifstream fin(filenamei.c_str());

void recurse(int row){
    if (row == N + 1){
        cnt++;
        if (cnt <= 3){
            FOR (i, N){
                fout << history[i];
                if (i < N - 1)
                    fout << ' ';
            }
            fout << endl;
        }
        return;
    }
    for (int col = 1; col <= N; col++){
        if (cc[col]) continue;
        if (d1[N - row + col]) continue;
        if (d2[row + col - 1]) continue;
        if (cnt <= 3)
            history.push_back(col);
        cc[col] = true;
        d1[N - row + col] = true;
        d2[row + col - 1] = true;

        recurse(row + 1);

        if (cnt <= 3)
            history.pop_back();
        cc[col] = false;
        d1[N - row + col] = false;
        d2[row + col - 1] = false;
    }
}


int main(int argc, char **argv){
    time_t ttt = time(nullptr);


    // const string filename("checker");




    // string filenameo = filename + ".out";
    // string filenamei = filename + ".in";
    // ofstream fout(filenameo.c_str());
    // ifstream fin(filenamei.c_str());


    fin >> N;

    recurse(1);

    fout << cnt << endl;







    fin.close();
    fout.close();


    printf("~%d\n", time(nullptr) - ttt);
    // system("pause");
    return 0;
}