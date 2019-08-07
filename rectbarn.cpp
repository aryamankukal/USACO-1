/*
ID: wrwwctb1
TASK: rectbarn
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








const string filename("rectbarn");









int main(int argc, char **argv){

    string filenameo = filename + ".out";
    string filenamei = filename + ".in";
    ofstream fout(filenameo.c_str());
    ifstream fin(filenamei.c_str());





    int R, C, P;
    fin >> R >> C >> P;

    vector<unordered_set<int>> badpts(R);

    FOR (p, P){
        int i, j;
        fin >> i >> j;
        badpts[i-1].insert(j-1);
    }

    vector<int> height(C, 0);
    vector<int> hl(C, -1);
    vector<int> hr(C,  C);
    int ret = 0;

    FOR (i, R){
        int rowl = -1;
        int rowr = C;
        FOR (j, C){
            if (badpts[i].find(j) == badpts[i].end())
                height[j] += 1;
            else
                height[j] = 0;
        }

        FOR (j, C){
            if (badpts[i].find(j) != badpts[i].end()){
                rowl = j;
                hl[j] = -1;
            } else
                hl[j] = max(rowl, hl[j]);
        }

        for (int j = C - 1; j > -1; j--){
            if (badpts[i].find(j) != badpts[i].end()){
                rowr = j;
                hr[j] = C;
            } else
                hr[j] = min(rowr, hr[j]);
        }

        FOR (j, C)
            ret = max(ret, (hr[j] - hl[j] - 1) * height[j]);
    }
    cout << ret << endl;
    fout << ret << endl;








    //system("pause");
    return 0;
}
