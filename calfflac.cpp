/*
ID: wrwwctb1
TASK: calfflac
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







int main(int argc, char **argv){


    const string filename("calfflac");


    string filenameo = filename + ".out";
    string filenamei = filename + ".in";
    ofstream fout(filenameo.c_str());
    ifstream fin(filenamei.c_str());



    stringstream buffer;
    buffer << fin.rdbuf();

    string rawString = buffer.str();


    const int Nmax = 20000;
    char chars[Nmax];
    int oldLoc[Nmax];
    int N = 0;
    FOR (i, rawString.size()){
        char c = rawString[i];
        if (isalpha(c)){
            chars[N] = tolower(c);
            oldLoc[N] = i;
            N++;
        }
    }
    int isp[3][Nmax] = {};
    FOR (i, N){
        isp[0][i] = true;
    }
    int best;
    if (N > 0){
        best = 1;
    }else{
        best = 0;
    }
    int besti = 0;
    int bestj = 0;
    int d = 1;
    int l = 2;
    FOR (i, N - d){
        int j = i + d;
        if (chars[i] == chars[j]){
            isp[1][i] = true;
            if (best < l){
                best = l;
                besti = i;
                bestj = j;
            }
        }else{
            isp[1][i] = false;
        }
    }


    for (int d = 2; d < N; d++){
        int l = d + 1;
        int currd = d % 3;
        int prevd = (d-2) % 3;
        FOR (i, N - d){
            int j = i + d;
            if (chars[i] == chars[j] && isp[prevd][i+1]){
                isp[currd][i] = true;
                if (best < l){
                    best = l;
                    besti = i;
                    bestj = j;
                }
            }else{
                isp[currd][i] = false;
            }
        }
    }

    fout << best << endl;
    if (best > 0){
        fout << rawString.substr(oldLoc[besti], oldLoc[bestj] - oldLoc[besti] + 1)
             << endl;
    }else{
        fout << endl;
    }






    //system("pause");
    return 0;
}
