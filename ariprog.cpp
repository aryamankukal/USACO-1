/*
ID: wrwwctb1
TASK: ariprog
LANG: C++14
*/

#include <iostream>
#include <iomanip>
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

#define FOR( i, N ) for( int (i) = 0; (i) < (N); (i)++ )
//#define FOR_( i, start, endplusone ) for( int (i) = (start); (i) < (endplusone); (i)++ )
const double EPS = 1e-6;
const double PI = 3.141592653589793;
using namespace std;



const string filename("ariprog");


void wrapper(int maxdiff, vector<int> &bsqls, int N, int maxbsq, bool bsqtf[], vector<pair<int, int>> &out){
    for (int b = 1; b <= maxdiff; b++){
        for (auto a: bsqls){
            int last  = a + (N-1) * b;
            if (last > maxbsq)
                break;
            if (!bsqtf[last]) // last not in bsqst
                continue;
            if (!bsqtf[a + b]) // a + b not in bsqst
                continue;

            int founddepth = 1;
            int curr = a;
            while (founddepth < N){
                curr += b;
                if (!bsqtf[curr]) // curr not in bsqst
                    break;
                else
                    founddepth += 1;
            }
            if (N == founddepth){
                out.push_back(make_pair(a, b));
            }
        }
    }
}

int main(int argc, char **argv){
    string filenameo = filename + ".out";
    string filenamei = filename + ".in";
    ofstream fout(filenameo.c_str());
    ifstream fin(filenamei.c_str());




    int N, M;
    fin >> N >> M;
    int maxbsq = M * M *2;
    unordered_set<int> bsqst;
    const int MM2_max = 250 * 250 * 2;

    bool bsqtf[MM2_max + 1] = {false};

    for (int p = 0; p <= M; p++){
        for (int q = p; q <= M; q++){
            int bsq = p * p + q * q;
            bsqst.emplace(bsq);
            bsqtf[bsq] = true;
        }
    }
    vector<int> bsqls(bsqst.begin(), bsqst.end());
    sort(bsqls.begin(), bsqls.end());

    int maxdiff = maxbsq / (N-1);

    vector<pair<int, int>> out;
    wrapper(maxdiff, bsqls, N, maxbsq, bsqtf, out);

    if (out.empty())
        fout << "NONE\n";
    else
        for (auto p: out)
            fout << p.first << " " << p.second << endl;





   //system("pause");
    return 0;
}
