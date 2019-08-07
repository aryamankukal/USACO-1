/*
ID: wrwwctb1
TASK: cryptcow
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
















const int HASH_NUM = 10000000;
bool hashVisited[HASH_NUM];

unsigned int elf_hash(string str){
    unsigned long h = 0, g, i, l;
    l = str.length();
    for (i = 0; i < l; i ++){
        h = (h << 4) + str[i];
        if (g = h & 0xf0000000l)
            h ^= g >> 24;
        h &= ~g;
    }
    return h % HASH_NUM;

    // // slowest
    // hash<int> hasher;
    // size_t seed = 0;
    // FOR (i, str.size())
    //     seed ^= hasher(str[i]) + 0x9e3779b9 + (seed<<6) + (seed>>2);
    // return seed % HASH_NUM;

    // // slower
    // unsigned long hash = 5381;
    // FOR (i, str.size())
    //     hash = (hash << 5) + hash + str[i]; /* hash * 33 + c */
    // return hash % HASH_NUM;
}

void str2map(string given, unordered_map<char, int> &cntGiven){
    for (char ch: given)
        cntGiven[ch] += 1;
}

bool checkLetterCounts(string target, string given){
    if (given.size() < target.size())
        return false;
    int delta = given.size() - target.size();
    if (delta % 3)
        return false;
    unordered_map<char, int> cntTarget;
    unordered_map<char, int> cntGiven;
    str2map(target, cntTarget);
    str2map(given, cntGiven);

    if (delta){
        cntTarget['C'] = delta / 3;
        cntTarget['O'] = delta / 3;
        cntTarget['W'] = delta / 3;
    }
    if (cntTarget != cntGiven)
        return false;
    return true;
}

bool recurse(string &target, string &given){


    int tl = target.size();
    int gl = given.size();
    if (tl == gl)
        return target == given;

    int C0 = given.find('C');
    int W1 = given.rfind('W');
    // assert (C0 >= 0 && W1 >= 0);

    int targetSubEnd = tl-(gl-W1)+1;
    if (targetSubEnd < 0 || tl < targetSubEnd)
        return false;
    if (target.substr(0, C0) != given.substr(0, C0))
        return false;
    if (target.substr(targetSubEnd, tl) != given.substr(W1+1))
        return false;

    string trimmedTarget = target.substr(C0, targetSubEnd-C0);


    int Cs[9];
    int Os[9];
    int Ws[9];
    int Ccnt = 0;
    int Ocnt = 0;
    int Wcnt = 0;
    int prev = -1;
    FOR (i, gl){
        char ch = given[i];
        if (ch == 'C' || ch == 'O' || ch == 'W'){
            if (ch == 'C')
                Cs[Ccnt++] = i;
            else if (ch == 'O')
                Os[Ocnt++] = i;
            else
                Ws[Wcnt++] = i;

            if (prev > -1 && trimmedTarget.find(given.substr(prev+1, i-prev-1)) == string::npos)
                return false;
            prev = i;
        }
    }

    FOR (io, Ocnt){
        FOR (ic, Ccnt){
            FOR (iw, Wcnt){
                int C = Cs[ic];
                int O = Os[io];
                int W = Ws[iw];
                if (C < O && O < W){


                    string cand = given.substr(C0, C-C0) +
                                  given.substr(O+1, W-O-1) +
                                  given.substr(C+1, O-C-1) +
                                  given.substr(W+1, W1-W);

                    int hash = elf_hash(cand);
                    if ( not hashVisited[hash] ){
                        hashVisited[hash] = true;

                        if (recurse(trimmedTarget, cand))
                            return true;
                    }
                }
            }
        }
    }
    return false;
}

void output(ofstream &fout, int a, int b){
    fout << a << ' ' << b << endl;
    cout << '.' << a << ' ' << b << endl;
}

int main(int argc, char **argv){
    time_t ttt = time(nullptr);


    const string filename("cryptcow");


    string filenameo = filename + ".out";
    string filenamei = filename + ".in";
    ofstream fout(filenameo.c_str());
    ifstream fin(filenamei.c_str());



    string target = "Begin the Escape execution at the Break of Dawn";
    string given;
    getline(fin, given);





    if (!checkLetterCounts(target, given))
        output(fout, 0, 0);
    else{
        if (recurse(target, given))
            output(fout, 1, (given.size() - target.size()) / 3);
        else
            output(fout, 0, 0);
    }












    printf("~%d\n", time(nullptr) - ttt);
    //system("pause");
    return 0;
}