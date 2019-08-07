/*
ID: wrwwctb1
TASK: inflate
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

#include <cmath>
#include <algorithm>
#include <cfloat>
#include <iomanip>
#include <ctime>
#include <climits>

#define FOR( i, N ) for( int (i) = 0; (i) < (N); (i)++ )
//#define FOR_( i, start, endplusone ) for( int (i) = (start); (i) < (endplusone); (i)++ )
const double EPS = 1e-6;
const double PI = 3.141592653589793;
using namespace std;



const string filename("inflate");

int t[10001];
// inline int max(int a,int b){
//     return a>b ? a:b;
// }

int main(int argc, char **argv){
    string filenameo = filename + ".out";
    string filenamei = filename + ".in";
    ofstream fout(filenameo.c_str());
    ifstream fin(filenamei.c_str());




    int M, N;
    fin >> M >> N;
    FOR(n, N){
        int p, len;
        fin >> p >> len;
        for(int m = len; m <= M; m++)
            t[m] = max(t[m], t[m - len] + p);
    }
    fout << t[M] << endl;








   //system("pause");
    return 0;
}
