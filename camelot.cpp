/*
ID: wrwwctb1
TASK: camelot
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

#define FOR( i, N ) for( int (i) = 0; (i) < (N); (i)++ )
//#define FOR_( i, start, endplusone ) for( int (i) = (start); (i) < (endplusone); (i)++ )
const double EPS = 1e-6;
const double PI = 3.141592653589793;
using namespace std;









const string filename("camelot");






int Ato1(char ch){
    return int(ch) - 64;
}

void bfs(vector<vector<int>> &board, int R, int C, int r, int c){
    vector<pair<int, int>> oldlayer;
    oldlayer.emplace_back(r, c);
    int layernum = 0;
    int deli[8] = {2, 1, -1, -2, -2, -1, 1, 2};
    int delj[8] = {-1, -2, -2, -1, 1, 2, 2, 1};
    while (!oldlayer.empty()){
        vector<pair<int, int>> newlayer;
        layernum += 1;
        for (auto ij: oldlayer){
            int i = ij.first;
            int j = ij.second;
            FOR (d, 8){
                int curri = i + deli[d];
                int currj = j + delj[d];
                if (1 <= curri && curri <= R &&
                    1 <= currj && currj <= C &&
                    board[curri][currj] == -1){
                    board[curri][currj] = layernum;
                    newlayer.emplace_back(curri, currj);
                }
            }
        }
        oldlayer.swap(newlayer);
    }
}

void avalanche(vector<vector<int>> &mark, vector<vector<int>> &board,
               int currlayer, int knightr, int knightc, int R, int C){
    if (mark[knightr][knightc])
        return;

    mark[knightr][knightc] = 1;

    int delr[8] = {2, 1, -1, -2, -2, -1, 1, 2};
    int delc[8] = {-1, -2, -2, -1, 1, 2, 2, 1};

    FOR (d, 8){
        int currr = knightr + delr[d];
        int currc = knightc + delc[d];
        if (1 <= currr && currr <= R &&
            1 <= currc && currc <= C &&
            !mark[currr][currc] &&
            board[currr][currc] == currlayer-1)
            avalanche(mark, board, currlayer-1, currr, currc, R, C);
    }
}

int kingbfs(vector<vector<int>> &mark, int kingr, int kingc, int R, int C){
    int deli[8] = {1, 0, -1, -1, -1, 0, 1, 1};
    int delj[8] = {-1, -1, -1, 0, 1, 1, 1, 0};
    vector<pair<int, int>> oldlayer;
    oldlayer.emplace_back(kingr, kingc);
    vector<vector<int>> state(R+1, vector<int>(C+1, 0));
    int layernum = 0;
    while (!oldlayer.empty()){
        vector<pair<int, int>> newlayer;
        for (auto ij: oldlayer){
            int i = ij.first;
            int j = ij.second;
            if (mark[i][j] == 1)
                return layernum;
            state[i][j] = 2;
            FOR (d, 8){
                int curri = i + deli[d];
                int currj = j + delj[d];
                if (1 <= curri && curri <= R &&
                    1 <= currj && currj <= C &&
                    mark[curri][currj] != -1 &&
                    state[curri][currj] == 0){
                    newlayer.emplace_back(curri, currj);
                    state[curri][currj] = 1;
                }
            }
        }
        oldlayer.swap(newlayer);
        layernum += 1;
    }
    return INT_MAX;
}


int main(int argc, char **argv){

    string filenameo = filename + ".out";
    string filenamei = filename + ".in";
    ofstream fout(filenameo.c_str());
    ifstream fin(filenamei.c_str());







    int R, C;
    fin >> R >> C;
    char A;
    int i;
    fin >> A >> i;
    int kingr = i;
    int kingc = Ato1(A);

    vector<pair<int, int>> knights;







    while (fin >> A >> i){
        knights.emplace_back(i, Ato1(A));
    }


    // printf(" %d %d %d %d\n", R, C, kingr, kingc);
    // for (auto knight: knights){
    //     printf(" %d %d ", knight.first, knight.second);
    // }



    int best = INT_MAX;
    vector<vector<int>> board(R+1, vector<int>(C+1, -1));
    vector<vector<int>> mark(R+1, vector<int>(C+1, 0));

    for (int r = 1; r <= R; r++){
        for (int c = 1; c <= C; c++){
            FOR (i, R+1)
                FOR (j, C+1)
                    board[i][j] = -1;
            board[r][c] = 0;
            bfs(board, R, C, r, c);

            bool canreach = true;
            for (auto knightrc: knights){
                auto knightr = knightrc.first;
                auto knightc = knightrc.second;
                if (board[knightr][knightc] == -1){
                    canreach = false;
                    break;
                }
            }
            if (!canreach)
                continue;


            FOR (i, R+1)
                FOR (j, C+1)
                    mark[i][j] = 0;
            mark[r][c] = 1;
            for (auto knightrc: knights){
                auto knightr = knightrc.first;
                auto knightc = knightrc.second;
                avalanche(mark, board, board[knightr][knightc], knightr, knightc, R, C);
            }

            int cand = kingbfs(mark, kingr, kingc, R, C);

            for (auto knightrc: knights){
                auto knightr = knightrc.first;
                auto knightc = knightrc.second;
                cand += board[knightr][knightc];
            }


            if (cand < best)
                best = cand;
        }
    }
    // cout << best << endl;
    fout << best << endl;








    //system("pause");
    return 0;
}
