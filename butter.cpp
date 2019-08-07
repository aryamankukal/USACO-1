/*
ID: wrwwctb1
TASK: butter
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



const string filename("butter");








int dijk(vector<vector<pair<int, int>>> &neig,
         int s,
         int P,
         vector<int> &cowlocs){

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.emplace(0, s);
    vector<bool> seen(P+1, false);
    vector<int> est(P+1, INT_MAX);
    est[s] = 0;

    int tot = 0;

    while (!pq.empty()){
        pair<int, int> est_u = pq.top();
        pq.pop();
        int estu = est_u.first;
        int u = est_u.second;

        if (seen[u])
            continue;

        seen[u] = true;

        if (cowlocs[u])
            tot += estu * cowlocs[u];

        for (auto wv: neig[u]){
            int w = wv.first;
            int v = wv.second;

            if (seen[v])
                continue;

            if (estu + w < est[v]){
                est[v] = estu + w;
                pq.emplace(estu+w, v);
            }
        }
    }
    return tot;
}

int main(int argc, char **argv){

    string filenameo = filename + ".out";
    string filenamei = filename + ".in";
    ofstream fout(filenameo.c_str());
    ifstream fin(filenamei.c_str());


    int N, P, C;
    fin >> N >> P >> C;

    // const int Nmax = 500;
    // const int Pmax = 800;
    // const int Cmax = 1450;
    vector<int> cowlocs(P+1, 0);
    FOR(n, N){
        int loc;
        fin >> loc;
        cowlocs[loc] += 1;
    }

    vector<vector<pair<int, int>>> neig(P+1);
    int u, v, w;
    FOR(c, C){
        fin >> u >> v >> w;
        neig[u].push_back(make_pair(w, v));
        neig[v].push_back(make_pair(w, u));
    }

    // // check input
    // cout << " " << N << " " << P << " " << C << endl;
    // for (auto c: cowlocs)
    //     cout << " " << c;
    // cout << endl;
    // for (auto v: neig){
    //     for (auto p: v)
    //         cout << " " << p.first << " " << p.second << " ";
    //     cout << endl;
    // }

    int best = INT_MAX;
    for (int sugar = 1; sugar <= P; sugar++){
        int tot = dijk(neig, sugar, P, cowlocs);
        if (tot < best)
            best = tot;
    }

    fout << best << endl;







    //system("pause");
    return 0;
}
