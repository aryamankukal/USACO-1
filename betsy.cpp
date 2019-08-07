/*
ID: wrwwctb1
TASK: betsy
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
#include <ctime> // time(nullptr) returns time_t, int seconds
#include <chrono>
#include <climits>
#include <iomanip>
#include <cstring>

#define FOR( i, N ) for( int (i) = 0; (i) < (N); (i)++ )
//#define FOR_( i, start, endplusone ) for( int (i) = (start); (i) < (endplusone); (i)++ )
const double EPS = 1e-6;
const double PI = 3.141592653589793;
using namespace std;
// profile: 27196474












const int Nmax = 7;
const int Nmax2 = 49;
int N;
int N2;
int board[Nmax+1][Nmax+1];
int acc[Nmax+1][Nmax+1];


int dfs(int Nfilled, int i, int j){
    if (i == N && j == 1)
        if (Nfilled == N2)
            return 1;
        else
            return 0;

    int ijneigsX[4];
    int ijneigsY[4];
    int ijneigsN = 0;

    for (int x = i - 1; x <= i + 1; x += 2){
        if (x < 1 || N < x || board[x][j])
            continue;
        ijneigsX[ijneigsN  ] = x;
        ijneigsY[ijneigsN++] = j;
    }

    for (int y = j - 1; y <= j + 1; y += 2){
        if (y < 1 || N < y || board[i][y])
            continue;
        ijneigsX[ijneigsN  ] = i;
        ijneigsY[ijneigsN++] = y;
    }

    FOR (k, ijneigsN){
        int x = ijneigsX[k];
        int y = ijneigsY[k];
        if (acc[x][y] == 0)
            if (!(x == N && y == 1 && Nfilled == N2 - 1))
                return 0;
    }

    if (ijneigsN == 3 && 1 <= i && i <= N && 1 <= j && j <= N)
        if      (board[i + 1][j] && (board[i - 1][j - 1] || board[i - 1][j + 1]))
            return 0;
        else if (board[i - 1][j] && (board[i + 1][j - 1] || board[i + 1][j + 1]))
            return 0;
        else if (board[i][j - 1] && (board[i - 1][j + 1] || board[i + 1][j + 1]))
            return 0;
        else if (board[i][j + 1] && (board[i - 1][j - 1] || board[i + 1][j - 1]))
            return 0;

    if (ijneigsN == 2)
        if (ijneigsX[0] == ijneigsX[1] || ijneigsY[0] == ijneigsY[1])
            return 0;

    FOR (k, ijneigsN){
        int x = ijneigsX[k];
        int y = ijneigsY[k];
        if (acc[x][y] == 1 && !(x == N && y == 1)){
            ijneigsX[0] = x;
            ijneigsY[0] = y;
            ijneigsN = 1;
            break;
        }
    }

    if (ijneigsN == 3)
        if       (i == 2     && board[3    ][j    ]){
            ijneigsX[0] = 2;
            ijneigsY[0] = j - 1;
            ijneigsN = 1;
        }else if (i == N - 1 && board[N - 2][j    ]){
            ijneigsX[0] = N - 1;
            ijneigsY[0] = j + 1;
            ijneigsN = 1;
        }else if (j == 2     && board[i    ][3    ]){
            ijneigsX[0] = i - 1;
            ijneigsY[0] = 2;
            ijneigsN = 1;
        }else if (j == N - 1 && board[i    ][N - 2]){
            ijneigsX[0] = i - 1;
            ijneigsY[0] = N - 1;
            ijneigsN = 1;
        }

    int cnt = 0;
    FOR (k, ijneigsN){
        int x = ijneigsX[k];
        int y = ijneigsY[k];

        if (x < 1 || N < x || y < 1 || N < y || board[x][y])
            continue;

        int xyneigsU[4];
        int xyneigsV[4];
        int xyneigsN = 0;

        for (int u = x - 1; u <= x + 1; u += 2)
            if (1 <= u && u <= N){
                xyneigsU[xyneigsN  ] = u;
                xyneigsV[xyneigsN++] = y;
            }

        for (int v = y - 1; v <= y + 1; v += 2)
            if (1 <= v && v <= N){
                xyneigsU[xyneigsN  ] = x;
                xyneigsV[xyneigsN++] = v;
            }

        board[x][y] = Nfilled + 1;
        FOR (l, xyneigsN)
            acc[xyneigsU[l]][xyneigsV[l]] -= 1;

        cnt += dfs(Nfilled + 1, x, y);

        board[x][y] = 0;
        FOR (l, xyneigsN)
            acc[xyneigsU[l]][xyneigsV[l]] += 1;
    }
    return cnt;
}


int dfs_help(){
    if (N == 1)
        return 1;
    if (N == 2)
        return 1;

    for (int i = 2; i < N; i++)
        for (int j = 2; j < N; j++)
            acc[i][j] = 4;
    for (int i = 2; i < N; i++)
        acc[1][i] = acc[i][1] = acc[N][i] = acc[i][N] = 3;
    acc[1][1] = acc[N][1] = acc[1][N] = acc[N][N] = 2;

    acc[1][2] -= 1;
    acc[2][1] -= 1;

    board[1][1] = 1;

    return dfs(1, 1, 1);
}



int main(int argc, char **argv){
    auto ttt = chrono::steady_clock::now();


    const string filename("betsy");




    string filenameo = filename + ".out";
    string filenamei = filename + ".in";
    ofstream fout(filenameo.c_str());
    ifstream fin(filenamei.c_str());




    fin >> N;
    N2 = N * N;

    int ans = dfs_help();

    fout << ans << endl;







    fin.close();
    fout.close();

    printf("~%f\n", ((chrono::duration<double>)(chrono::steady_clock::now() - ttt)).count());
    // system("pause");
    return 0;
}