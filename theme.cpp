/*
ID: wrwwctb1
TASK: theme
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




const string filename("theme");





int main(int argc, char **argv){

    string filenameo = filename + ".out";
    string filenamei = filename + ".in";
    ofstream fout(filenameo.c_str());
    ifstream fin(filenamei.c_str());


    int N;
    fin >> N;

    const int Nmax = 5000;

    int m[Nmax];

    FOR (n, N){
        fin >> m[n];
    }

    // vector<vector<int>> d (N, vector<int>(N, 1));
    // FOR (i, N){
    //     FOR (j, i+1){
    //         d[i][j] = 0;
    //     }
    // }

    int best = 1;
    for (int imax = N-3; imax >= 0; imax--){
        int i = imax;
        int j = N - 2;
        int di1j1 = 1;
        while (i >= 0){
            if (m[i+1] - m[i] == m[j+1] - m[j]){
                int dij = min(1 + di1j1, j-i);
                best = max(best, dij);
                di1j1 = dij;
            }else{
                di1j1 = 1;
            }

            i -= 1;
            j -= 1;
        }
    }

    if (best >= 5){
        fout << best << endl;
    }else{
        fout << 0 << endl;
    }










    //system("pause");
    return 0;
}
