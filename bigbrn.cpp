/*
ID: wrwwctb1
TASK: bigbrn
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








const string filename("bigbrn");









int main(int argc, char **argv){

    string filenameo = filename + ".out";
    string filenamei = filename + ".in";
    ofstream fout(filenameo.c_str());
    ifstream fin(filenamei.c_str());


    int N, T;
    fin >> N >> T;
    vector<vector<int>> barn(N+1, vector<int>(N+1, -1));
    FOR (t, T){
        int i, j;
        fin >> i >> j;
        barn[i][j] = 0;
    }
    FOR (i, N+1){
        barn[0][i] = barn[i][0] = 0;
    }
    int best = 0;
    for (int i = 1; i <= N; i++){
        for (int j = 1; j <= N; j++){
            if (barn[i][j] == 0){
                continue;
            }else{
                int temp = min({barn[i-1][j],
                                barn[i][j-1],
                                barn[i-1][j-1]}) + 1;
                best = max(best, temp);
                barn[i][j] = temp;
            }
        }
    }
    fout << best << endl;











    //system("pause");
    return 0;
}
