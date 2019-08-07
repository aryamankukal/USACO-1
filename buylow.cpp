/*
ID: wrwwctb1
TASK: buylow
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






const string filename("buylow");




const int LEN = 100;

struct BigNum{
    BigNum(int a){
        memset(d, 0, sizeof(char) * LEN);
        int i = 0;
        while (a > 0){
            int rem = a % 10;
            d[i] = rem;
            a /= 10;
            i += 1;
        }
    }
    char d[LEN];
    BigNum& operator+=(const BigNum& rhs){
        char carry = 0;
        FOR (i, LEN){
            char temp = this->d[i] + rhs.d[i] + carry;
            this->d[i] = temp % 10;
            carry = temp / 10;
        }
        assert (carry == 0);
        return *this;
    }
};

ostream &operator<<(ostream &os, const BigNum &bn){
    int i = LEN-1;
    while (i >= 0 && bn.d[i] == 0){
        i--;
    }
    if (i < 0){
        return os << 0;
    }else{
        while (i > 0){
            os << int(bn.d[i]);
            i--;
        }
        return os << int(bn.d[i]);
    }
}


pair<int, BigNum> LDS(vector<int> &aa){
    aa.push_back(-1);

    vector<int> L;
    vector<BigNum> M;
    for (int i = 0; i < aa.size(); i++){
        int aai = aa[i];

        int best = 0;
        FOR (j, i){
            if (aa[j] > aai && best < L[j]){
                best = L[j];
            }
        }
        if (best == 0){
            L.push_back(1);
            M.push_back(1);
        }else{
            L.push_back(best + 1);
            unordered_set<int> got;
            BigNum cnt(0);
            for (int j = i-1; j >= 0; j--){
                if (L[j] == best && aa[j] > aai && got.find(aa[j]) == got.end()){
                    cnt += M[j];
                    got.emplace(aa[j]);
                }
            }
            M.push_back(cnt);
        }
    }
    return make_pair(L[L.size()-1]-1, M[M.size()-1]);
}


int main(int argc, char **argv){

    string filenameo = filename + ".out";
    string filenamei = filename + ".in";
    ofstream fout(filenameo.c_str());
    ifstream fin(filenamei.c_str());


    BigNum ha(1);
    cout << " " << ha << endl;

    int N;
    fin >> N;
    vector<int> aa;
    FOR (n, N){
        int temp;
        fin >> temp;
        aa.push_back(temp);
    }

    // for (auto a: aa)
    //     cout << " " << a << " ";

    auto p = LDS(aa);
    // cout << " " << p.first << " " << p.second;
    fout << p.first << " " << p.second << endl;







    //system("pause");
    return 0;
}
