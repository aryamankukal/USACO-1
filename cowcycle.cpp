/*
ID: wrwwctb1
TASK: cowcycle
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






int a[57]; // front gears
int b[37]; // rear gears
int ansa[57];
int ansb[37];
int F, R, F1, R1, F2, R2;
double ans;
double c[2017]; // ratios. 2017 == 56 * 36 + 1

void find_r(int Rstart, int Rstep){
    if (Rstep == R + 1){
        // prune
        if (a[F] * b[R] < 3 * a[1] * b[1])
            return;

        // calculate ratios
        int cnt = 0;
        for (int i = 1; i <= F; i++)
            for (int j = 1; j <= R; j++)
                c[++cnt] = double(a[i]) / double(b[j]);

        // insertion sort
        for (int i = 1; i < cnt; i++)
            for (int j = i + 1; j <= cnt; j++)
                if (c[i] > c[j]){
                    double t = c[i];
                    c[i] = c[j];
                    c[j] = t;
                }

        // mean
        double sum = 0;
        for (int i = 1; i < cnt; i++){
            c[i] = c[i + 1] - c[i];
            sum += c[i];
        }
        cnt--;
        sum /= cnt;

        // std
        double tot = 0;
        for (int i = 1; i <= cnt; i++)
            tot += (c[i] - sum) * (c[i] - sum);

        if (tot < ans){
            ans = tot;
            memcpy(ansa + 1, a + 1, sizeof(int) * F);
            memcpy(ansb + 1, b + 1, sizeof(int) * R);
            // for (i = 1; i <= F; i++)
            //     ansa[i] = a[i];
            // for (i = 1; i <= R; i++)
            //     ansb[i] = b[i];
        }
        return;
    }
    for (int Ri = Rstart; Ri <= R2 - R + Rstep; Ri++){
        b[Rstep] = Ri;
        find_r(Ri + 1, Rstep + 1);
    }
}

void find_f(int Fstart, int Fstep){
    if (Fstep == F + 1){
        find_r(R1, 1);
        return;
    }
    for (int Fi = Fstart; Fi <= F2 - F + Fstep; Fi++){
        a[Fstep] = Fi;
        find_f(Fi + 1, Fstep + 1);
    }
}

int main(int argc, char **argv){
    time_t ttt = time(nullptr);

    const string filename("cowcycle");




    string filenameo = filename + ".out";
    string filenamei = filename + ".in";
    ofstream fout(filenameo.c_str());
    ifstream fin(filenamei.c_str());

    fin >> F >> R >> F1 >> F2 >> R1 >> R2;

    ans = DBL_MAX;

    find_f(F1, 1);

    for (int i = 1; i < F; i++)
        fout << ansa[i] << ' ';
    fout << ansa[F] << endl;

    for (int i = 1; i < R; i++)
        fout << ansb[i] << ' ';
    fout << ansb[R] << endl;






    printf("~%d\n", time(nullptr) - ttt);
    //system("pause");
    return 0;
}