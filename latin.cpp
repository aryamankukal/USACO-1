/*
ID: wrwwctb1
TASK: latin
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












const int Nmax = 7;
int FACT[Nmax + 1] = {1, 1, 2, 6, 24, 120, 720, 5040};

struct Node{
    Node(int val): val(val){}
    int val = -1;
    Node *nxt = nullptr;
};

Node *createList(int N, int skip){
    Node *root = new Node(-1);
    Node *curr = root;
    for (int n = 1; n <= N; n++){
        if (n == skip)
            continue;
        curr->nxt = new Node(n);
        curr = curr->nxt;
    }
    return root;
}

long long Ln(Node *roots[], int occ[][Nmax + 1], int N, int row=2, int col=2){
    if (col == N + 1){
        if (row == N - 1)
            return 1;
        row ++;
        col = 2;
    }

    Node *prev = roots[row];
    Node *curr = roots[row]->nxt;
    long long cnt = 0;
    while (curr){

        if (occ[curr->val][col]){
            occ[curr->val][col] = 0;
            prev->nxt = curr->nxt;

            cnt += Ln(roots, occ, N, row, col + 1);

            prev->nxt = curr;
            occ[curr->val][col] = 1;
        }
        prev = curr;
        curr = curr->nxt;
    }
    return cnt;
}

int checkGroups(int row2[], int N){
    bool seen[Nmax + 1] = {};
    int groups[Nmax];
    int groupsN = 0;

    int group[Nmax] = {1};
    int groupN = 1;
    seen[1] = true;
    int cur = 1;

    while (true){
        int nxt = row2[cur];
        if (nxt == group[0]){
            groups[groupsN++] = groupN;
            int firstUnseen = 2;
            while (firstUnseen <= N and seen[firstUnseen])
                firstUnseen ++;
            if (firstUnseen > N)
                break;
            group[0] = firstUnseen;
            groupN = 1;
            seen[firstUnseen] = true;
            cur = firstUnseen;
        }else{
            group[groupN++] = nxt;
            seen[nxt] = true;
            cur = nxt;
        }
    }
    int hsh = 0;
    sort(groups, groups+groupsN);
    FOR (i, groupsN)
        hsh += (1 << 3*i) * groups[i];
    return hsh;
}

bool notGoodPerm(int perm[], int Nperm){
    FOR (i, Nperm)
        if (perm[i] == i + 2)
            return true;
    return false;
}

long long Ln3_help(int N){
    if (N == 2 || N == 3)
        return 1;

    Node *roots[Nmax + 1];
    for (int n = 3; n <= N; n++)
        roots[n] = createList(N, n);

    int occ[Nmax + 1][Nmax + 1] = {};
    FOR (i, Nmax + 1)
        FOR (j, Nmax + 1)
            occ[i][j] = 1;
    for (int n = 1; n <= N; n++)
        occ[n][n] = 0;
    occ[2][1] = 0;

    unordered_map<int, int> memo;

    int cnt = 0;
    int row2[Nmax + 1] = {-1, 2, 1};
    for (int n = 3; n <= N; n++)
        row2[n] = n;

    do{
        if (notGoodPerm(row2 + 2, N - 1))
            continue;

        int groupsHash = checkGroups(row2, N);

        if (memo.find(groupsHash) == memo.end()){ // not found
            for (int i = 2; i <= N; i++)
                occ[row2[i]][i] = 0;
            memo[groupsHash] = Ln(roots, occ, N, 3, 2);

            for (int i = 2; i <= N; i++)
                occ[row2[i]][i] = 1;
        }
        cnt += memo[groupsHash];
    }while (next_permutation(row2 + 2, row2 + N + 1));

    return cnt;
}

int main(int argc, char **argv){
    time_t ttt = time(nullptr);


    const string filename("latin");




    string filenameo = filename + ".out";
    string filenamei = filename + ".in";
    ofstream fout(filenameo.c_str());
    ifstream fin(filenamei.c_str());


    int N;
    fin >> N;
    // N = 7;

    long long cnt = Ln3_help(N);

    cnt *= FACT[N - 1];

    printf(" %lld", cnt);
    fout << cnt << endl;








    fin.close();
    fout.close();


    printf("~%d\n", time(nullptr) - ttt);
    // system("pause");
    return 0;
}