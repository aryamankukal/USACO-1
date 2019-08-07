/*
ID: wrwwctb1
TASK: stamps
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



const string filename("stamps");



int main(int argc, char **argv){

    string filenameo = filename + ".out";
    string filenamei = filename + ".in";
    ofstream fout(filenameo.c_str());
    ifstream fin(filenamei.c_str());





    int K, N;
    fin >> K >> N;

    int temp;
    vector<int> cent;
    for (int n = 0; n < N; n++){
        fin >> temp;
        cent.push_back(temp);
    }
    assert (cent.size() == N);
    sort(cent.begin(), cent.end());

    const int NN = 10001; // max stamp value + 1. think: at 10000, need info at 0
    int fewest[NN] = {0};
    int need = 1;
    while (true){
        int best = INT_MAX;
        FOR (i, N){
            int prev = need - cent[i];
            if (prev < 0){
                break;
            }else{
                int cand = fewest[prev % NN];
                if (cand < best){
                    best  = cand;
                }
            }
        }
        best += 1;
        if (best > K){
            break;
        }else{
            fewest[need % NN] = best;
            need += 1;


        }
    }
    fout << need-1 << endl;










    //system("pause");
    return 0;
}
