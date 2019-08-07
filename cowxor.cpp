/*
ID: wrwwctb1
TASK: cowxor
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







const string filename("cowxor");





struct Node{
    Node *L = NULL;
    Node *R = NULL;
};

struct Leaf: public Node{
    int X = -1;
};

void makeLeaf(Node *curr, int X, int n){
    for (int i = 20; i >= 0; i--){
        int mask = 1 << i;
        int bit = mask & X;
        if (bit){
            if (!(curr->R)){
                if (i > 0)
                    curr->R = new Node;
                else
                    curr->R = new Leaf;
            }
            curr = curr->R;
        }else{
            if (!(curr->L)){
                if (i > 0)
                    curr->L = new Node;
                else
                    curr->L = new Leaf;
            }
            curr = curr->L;
        }
    }
    Leaf *leaf = static_cast<Leaf*>(curr);
    if (leaf->X == -1){
        leaf->X = X;
    }
}
int findBest(int X, Node *curr){
    for (int i = 20; i >= 0; i--){
        int mask = 1 << i;
        int bit = mask & X;
        if (bit){
            if (curr->L){
                curr = curr->L;
            }else{
                curr = curr->R;
            }
        }else{
            if (curr->R){
                curr = curr->R;
            }else{
                curr = curr->L;
            }
        }
    }
    return static_cast<Leaf*>(curr)->X;
}

int main(int argc, char **argv){

    string filenameo = filename + ".out";
    string filenamei = filename + ".in";
    ofstream fout(filenameo.c_str());
    ifstream fin(filenamei.c_str());







    int N;
    fin >> N;
    Node *root = new Node;
    int X = 0;
    vector<int> Xs(1, X);
    makeLeaf(root, X, 0);
    for (int n = 1; n <= N; n++){
        int temp;
        fin >> temp;
        X ^= temp;
        Xs.push_back(X);
        makeLeaf(root, X, n);
    }

    int best = Xs[1];
    pair<int, int> bestIndices = make_pair(1, 1);
    unordered_map<int, int> lastSeen;
    lastSeen[0] = 0;
    lastSeen[Xs[1]] = 1;
    for (int n = 2; n <= Xs.size(); n++){
        int Xmatch = findBest(Xs[n], root);
        if (lastSeen.find(Xmatch) != lastSeen.end()){
            int cand = Xs[n] ^ Xmatch;
            if (best < cand){
                best = cand;
                bestIndices = make_pair(lastSeen[Xmatch]+1, n);
            }
        }
        lastSeen[Xs[n]] = n;
    }

    fout << best << " "
         << bestIndices.first << " "
         << bestIndices.second << endl;










    //system("pause");
    return 0;
}
