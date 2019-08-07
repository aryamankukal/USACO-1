/*
ID: wrwwctb1
TASK: wissqu
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















const string filename("wissqu");




string filenameo = filename + ".out";
string filenamei = filename + ".in";
ofstream fout(filenameo.c_str());
ifstream fin(filenamei.c_str());



int board[6][6];
int done[6][6];
int cnt;
int toPut[6] = {0, 3, 3, 3, 4, 3};
int hch[17];
int hi[17];
int hj[17];
bool foundFlag;



bool isBadPos(int i, int j, int ch){
    if (board[i  ][j  ] == ch) return true;
    if (board[i-1][j-1] == ch) return true;
    if (board[i+1][j+1] == ch) return true;
    if (board[i-1][j+1] == ch) return true;
    if (board[i+1][j-1] == ch) return true;
    if (board[i-1][j  ] == ch) return true;
    if (board[i+1][j  ] == ch) return true;
    if (board[i  ][j-1] == ch) return true;
    if (board[i  ][j+1] == ch) return true;
    return false;
}

void P(){
    cout << '.' << cnt << endl;
    FOR (i, 6){
        FOR (j, 6)
            cout << board[i][j];
        cout << endl;
    }
    cout << endl;
    FOR (i, 6){
        FOR (j, 6)
            cout << done[i][j];
        cout << endl;
    }
    cout << endl;
    FOR (i, 6)
        cout << toPut[i];
    cout << endl;
}

void recurse(int step){
    if (step == 17){
        cnt++;
        if (!foundFlag){
            for (int i = 1; i <= 16; i++){
                cout << '.' << " ABCDE"[hch[i]] << ' ' << hi[i] << ' ' << hj[i] << endl;
                fout        << " ABCDE"[hch[i]] << ' ' << hi[i] << ' ' << hj[i] << endl;
            }
            foundFlag = true;
        }
        // cout << ' ' << cnt;
        // P();
        return;
    }

    for (int ch = 1; ch < 6; ch++){
        if (!toPut[ch])
            continue;

        for (int i = 1; i < 5; i++){
            for (int j = 1; j < 5; j++){
                if (done[i][j] || isBadPos(i, j, ch))
                    continue;

                if (!foundFlag){
                    hch[step] = ch;
                    hi[step] = i;
                    hj[step] = j;
                }

                int boardijold = board[i][j];
                board[i][j] = ch;
                done[i][j] = 1;
                toPut[ch] -= 1;

                recurse(step + 1);

                board[i][j] = boardijold;
                done[i][j] = 0;
                toPut[ch] += 1;
            }
        }
    }
}

int main(int argc, char **argv){
    time_t ttt = time(nullptr);







    for (int i = 1; i < 5; i++){
        string line;
        fin >> line;
        FOR (j, line.size())
            board[i][j+1] = line[j] - 'A' + 1;
    }

    hch[1] = 4;

    for (int i = 1; i < 5; i++){
        for (int j = 1; j < 5; j++){
            if (isBadPos(i, j, 4))
                continue;

            if (!foundFlag){
                hi[1] = i;
                hj[1] = j;
            }

            int boardijold = board[i][j];
            board[i][j] = 4;
            done[i][j] = 1;
            toPut[4] -= 1;

            recurse(2);

            board[i][j] = boardijold;
            done[i][j] = 0;
            toPut[4] += 1;
        }
    }
    cout << '.' << cnt << endl;
    fout        << cnt << endl;





    fin.close();
    fout.close();


    printf("~%d\n", time(nullptr) - ttt);
    // system("pause");
    return 0;
}