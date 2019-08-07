/*
ID: wrwwctb1
TASK: clocks
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















int clocks2bits(int clocks[],int C){
    int num = 0;
    FOR (i, C)
        num += (clocks[i] / 3 % 4) * (1 << (i << 1));
    return num;
}

int moveLet2bits(string moveLet){
    int move = 0;
    for (char ch: moveLet)
        move += 1 << 2*(ch - 'A');
    return move;
}

int transition(int clocks, int move){
    int b0 = clocks & 0b010101010101010101;
    int b1 = clocks & 0b101010101010101010;
    int a0 = b0 ^ move;
    int a1 = b1 ^ ((b0 & move) << 1);
    return a0 + a1;
}

int main(int argc, char **argv){
    time_t ttt = time(nullptr);


    const string filename("clocks");




    string filenameo = filename + ".out";
    string filenamei = filename + ".in";
    ofstream fout(filenameo.c_str());
    ifstream fin(filenamei.c_str());






    const int C = 9;
    int clocksDig[C];
    FOR (c, C)
        fin >> clocksDig[c];
    int clocks = clocks2bits(clocksDig, C);

    const int M = 9;
    string moveLets[M] = {"ABDE",
                          "ABC",
                          "BCEF",
                          "ADG",
                          "BDEFH",
                          "CFI",
                          "DEGH",
                          "GHI",
                          "EFHI"};

    int moves[M];
    FOR (m, M)
        moves[m] = moveLet2bits(moveLets[m]);

    const int Nstates = 1 << 18;

    bool seen[Nstates] = {};
    seen[clocks] = true;
    queue<int> qq;
    qq.push(clocks);

    int parent[Nstates];
    int *arrivedVia = new int[Nstates]; // SIGSEGV if using array. stack overflow

    memset(parent, -1, sizeof(parent));

    while (!qq.empty()){
        int u = qq.front();
        qq.pop();
        if (u == 0)
            break;
        FOR (i, M){
            int v = transition(u, moves[i]);
            if (seen[v])
                continue;
            seen[v] = true;
            qq.push(v);
            parent[v] = u;
            arrivedVia[v] = i;
        }
    }

    int v = 0;
    vector<int> used;
    while (true){
        int u = parent[v];
        if (u == -1)
            break;
        used.push_back(arrivedVia[v] + 1);
        v = u;
    }

    FOR (i, used.size()){
        fout << used[used.size() - 1 - i];
        if (i != used.size()-1)
            fout << ' ';
    }
    fout << endl;








    fin.close();
    fout.close();


    printf("~%d\n", time(nullptr) - ttt);
    // system("pause");
    return 0;
}