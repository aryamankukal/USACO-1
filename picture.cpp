/*
ID: wrwwctb1
TASK: picture
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








const string filename("picture");








int checkEvents(vector<vector<int>> & events){
    int tot = 0;
    vector<int> num(20000, 0);
    for (auto event: events){
        int x = event[0];
        int io = event[1];
        int ym = event[2];
        int yM = event[3];

        vector<int> prev(20000);
        copy(num.begin(), num.end(), prev.begin());

        if (io == 0){
            for (int y = ym+10000; y < yM+10000; y++){
                num[y] += 1;
            }
        }else{
            for (int y = ym+10000; y < yM+10000; y++){
                num[y] -= 1;
            }
        }
        FOR (y, 20000){
            if (!prev[y] && num[y]){
                tot += 1;
            }else if(prev[y] && !num[y]){
                tot += 1;
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






    int N;
    fin >> N;
    vector<vector<int>> rects(N, vector<int>(4));
    FOR (n, N){
        fin >> rects[n][0]
            >> rects[n][1]
            >> rects[n][2]
            >> rects[n][3];
    }

    vector<vector<int>> xevents(2*N, vector<int>(4));
    vector<vector<int>> yevents(2*N, vector<int>(4));
    FOR (i, N){
        int xm = rects[i][0];
        int ym = rects[i][1];
        int xM = rects[i][2];
        int yM = rects[i][3];
        xevents[2*i][0] = xm;
        xevents[2*i][1] = 0;
        xevents[2*i][2] = ym;
        xevents[2*i][3] = yM;
        xevents[2*i+1][0] = xM;
        xevents[2*i+1][1] = 1;
        xevents[2*i+1][2] = ym;
        xevents[2*i+1][3] = yM;
        yevents[2*i][0] = ym;
        yevents[2*i][1] = 0;
        yevents[2*i][2] = xm;
        yevents[2*i][3] = xM;
        yevents[2*i+1][0] = yM;
        yevents[2*i+1][1] = 1;
        yevents[2*i+1][2] = xm;
        yevents[2*i+1][3] = xM;
    }

    sort(xevents.begin(), xevents.end());
    sort(yevents.begin(), yevents.end());

    int totx = checkEvents(xevents);
    int toty = checkEvents(yevents);

    cout << " " << totx + toty << endl;
    fout << totx + toty << endl;





    //system("pause");
    return 0;
}
