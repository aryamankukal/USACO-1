/*
ID: wrwwctb1
TASK: fence
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

#include <cmath>
#include <algorithm>
#include <cfloat>
#include <iomanip>
#include <ctime>
#include <climits>

#define FOR( i, N ) for( int (i) = 0; (i) < (N); (i)++ )
//#define FOR_( i, start, endplusone ) for( int (i) = (start); (i) < (endplusone); (i)++ )
const double EPS = 1e-6;
const double PI = 3.141592653589793;
using namespace std;





const string filename("fence");






void eulerian(vector<int> &circuit, vector<multiset<int>> &neig, int start){
    stack<int> st;
    st.push(start);
    while (!st.empty()){
        int u = st.top();
        if (!neig[u].empty()){
            // remove edge
            auto vit = neig[u].begin(); // set is sorted
            int v = *vit;
            auto uit = neig[v].find(u);
            neig[u].erase(vit);
            neig[v].erase(uit);
            // stack
            st.push(v);
        }else{
            // record
            circuit.emplace_back(st.top());
            st.pop();
        }
    }
}


int main(int argc, char **argv){

    string filenameo = filename + ".out";
    string filenamei = filename + ".in";
    ofstream fout(filenameo.c_str());
    ifstream fin(filenamei.c_str());


    const int nmax = 500;


    int F;
    fin >> F;
    vector<pair<int, int>> edge;
    vector<multiset<int>> neig(nmax + 1); // adjacency "set"
    set<int> node;
    FOR (f, F){
        int u, v;
        fin >> u >> v;
        edge.emplace_back(u, v);
        neig[u].emplace(v);
        neig[v].emplace(u);
        node.emplace(u);
        node.emplace(v);
    }

    // FOR (i, edge.size())
    //     cout << " " << edge[i].first << " " << edge[i].second << endl;

    // check deg
    vector<int> odd;
    FOR (i, nmax+1){
        if (neig[i].size() % 2 != 0){
            odd.emplace_back(i);
        }
    }

    // for (auto i: odd){
    //     cout << " " << i << " ";
    // }

    assert(odd.size() == 2 || odd.size() == 0);

    vector<int> circuit;

    if (odd.size() == 2)
        eulerian(circuit, neig, *min_element(odd.begin(), odd.end()));
    else
        eulerian(circuit, neig, *node.begin());

    for (int i = circuit.size()-1; i >= 0; i--){
        // cout << " " << circuit[i] << endl;
        fout << circuit[i] << endl;
    }








    //system("pause");
    return 0;
}
