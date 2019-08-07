/*
ID: wrwwctb1
TASK: charrec
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








const string filename("charrec");







int bin2int(string s){
    int out = 0;
    for (int i = 0; i < s.size(); i++){
        if (s[s.size()-1-i] == '1'){
            out += 1 << i;
        }
    }
    return out;
}
int chs2int(vector<char> &chs){
    int out = 0;
    for (int i = 0; i < chs.size(); i++){
        if (chs[chs.size()-1-i] == '1'){
            out += 1 << i;
        }
    }
    return out;
}
int popcount64c(uint64_t x){
    x -= (x >> 1) & 0x5555555555555555;
    //put count of each 2 bits into those 2 bits
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333);
    //put count of each 4 bits into those 4 bits
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f;
    //put count of each 8 bits into those 8 bits
    return (x * 0x0101010101010101) >> 56;
    //returns left 8 bits of x + (x<<8) + (x<<16) + (x<<24) + ...
}
void dp(vector<vector<int>> &match,
        vector<vector<int>> &accMatchF,
        vector<vector<int>> &accMatchB,
        vector<int> &allMinDiff,
        vector<int> &allMinDiffChi,
        vector<int> &allMinDiffHeight,
        int row0){

    if (allMinDiff[row0] == INT_MAX)
        return;

    if (row0 + 19 > allMinDiff.size()-2)
        return;

    int minDiff = INT_MAX;
    int minDiffChi = -1;

    FOR (chi, 27){
        int col0 = 20 * chi;

        int currMinDiff = min(accMatchB[row0  ][col0+1 ],
                              accMatchF[row0+1][col0+18]);
        for (int toSkip = 1; toSkip <= 18; toSkip++){
            int cand19 = accMatchB[row0  ][col0+toSkip+1] +
                         accMatchF[row0+1][col0+toSkip-1];
            currMinDiff = min(currMinDiff, cand19);
        }
        if (currMinDiff < minDiff){
            minDiff    = currMinDiff;
            minDiffChi = chi;
        }
    }

    int cand19 = minDiff + allMinDiff[row0];
    if (cand19 < allMinDiff[row0+19]){
        allMinDiff      [row0+19] = cand19;
        allMinDiffChi   [row0+19] = minDiffChi;
        allMinDiffHeight[row0+19] = 19;
    }





    if (row0 + 20 > allMinDiff.size()-2)
        return;

    minDiff = INT_MAX;
    minDiffChi = -1;

    FOR (chi, 27){
        int col0 = 20 * chi;
        int cand20 = accMatchB[row0+1][col0];
        if (cand20 < minDiff){
            minDiff = cand20;
            minDiffChi = chi;
        }
    }
    int cand20 = minDiff + allMinDiff[row0];
    if (cand20 < allMinDiff[row0+20]){
        allMinDiff      [row0+20] = cand20;
        allMinDiffChi   [row0+20] = minDiffChi;
        allMinDiffHeight[row0+20] = 20;
    }




    if (row0 + 21 > allMinDiff.size()-2)
        return;

    minDiff    = INT_MAX;
    minDiffChi = -1;

    FOR (chi, 27){
        int col0 = 20 * chi;
        int currMinDiff = min(accMatchB[row0+2][col0   ],
                              accMatchF[row0+1][col0+19]);
        FOR (toRepeat, 19){
            int cand21 = accMatchB[row0+2][col0+toRepeat+1] +
                         accMatchF[row0+1][col0+toRepeat  ];
            currMinDiff = min(currMinDiff, cand21);
        }
        if (currMinDiff < minDiff){
            minDiff    = currMinDiff;
            minDiffChi = chi;
        }
    }
    int cand21 = minDiff + allMinDiff[row0];
    if (cand21 < allMinDiff[row0+21]){
        allMinDiff      [row0+21] = cand21;
        allMinDiffChi   [row0+21] = minDiffChi;
        allMinDiffHeight[row0+21] = 21;
    }
}

int main(int argc, char **argv){

    string filenameo = filename + ".out";
    string filenamei = filename + ".in";
    ofstream fout(filenameo.c_str());
    ifstream fin(filenamei.c_str());




    int N;
    fin >> N;
    vector<vector<char>> rawImg;
    FOR (n, N){
        string line;
        fin >> line;
        vector<char> chs;
        for (char ch: line){
            chs.push_back(ch);
        }
        rawImg.push_back(chs);
    }

    // clean(rawImg)



    vector<int> dataImg(1, 0);
    FOR (n, N){
        int line = chs2int(rawImg[n]);
        dataImg.push_back(line);
    }
    dataImg.push_back(0);

    ifstream ffont("font.in");
    int Nfont;
    ffont >> Nfont;
    vector<int> font2d;
    FOR (n, Nfont){
        string s;
        ffont >> s;
        int line = bin2int(s);
        font2d.push_back(line);
    }

    vector<vector<int>> match(dataImg.size(),
                              vector<int>(font2d.size()));
    FOR (i, dataImg.size()){
        FOR (j, font2d.size()){
            match[i][j] = popcount64c(dataImg[i] ^ font2d[j]);
        }
    }

    vector<vector<int>> accMatchF;
    vector<vector<int>> accMatchB;
    FOR (i, dataImg.size()-19){
        vector<int> rowF;
        vector<int> rowB;
        for (int j = 0; j < font2d.size(); j+=20){
            vector<int> accF(1, match[i   ][j   ]);
            vector<int> accB(1, match[i+19][j+19]);
            for (int k = 1; k < 20; k++){
                accF.push_back(accF[accF.size()-1] + match[i   +k][j   +k]);
                accB.push_back(accB[accB.size()-1] + match[i+19-k][j+19-k]);
            }
            reverse(accB.begin(), accB.end());
            rowF.insert(rowF.end(), accF.begin(), accF.end());
            rowB.insert(rowB.end(), accB.begin(), accB.end());
        }
        accMatchF.push_back(rowF);
        accMatchB.push_back(rowB);
    }

    vector<int> allMinDiff(dataImg.size(), INT_MAX);
    allMinDiff[0] = 0;
    vector<int> allMinDiffChi(dataImg.size(), -1);
    vector<int> allMinDiffHeight(dataImg.size(), 0);

    FOR (row0, dataImg.size()){
        dp(match, accMatchF, accMatchB,
           allMinDiff, allMinDiffChi, allMinDiffHeight, row0);
    }

    string chars(" abcdefghijklmnopqrstuvwxyz");

    // debug
    FOR (i, allMinDiff.size()){
        char ch;
        if (allMinDiffChi[i] >= 0)
            ch = chars[allMinDiffChi[i]];
        else
            ch = '@';
        cout << " " << i
             << " " << allMinDiff[i]
             << " " << allMinDiffChi[i]
             << " " << ch
             << " " << allMinDiffHeight[i] << endl;
    }

    vector<char> out;
    int curr = allMinDiffChi.size()-2;
    while (curr > 0){
        cout << " " << curr << " " << chars[allMinDiffChi[curr]] << endl;
        out.push_back(chars[allMinDiffChi[curr]]);
        if (allMinDiffHeight[curr] == 0)
            break;
        curr -= allMinDiffHeight[curr];
    }

    reverse(out.begin(), out.end());
    //cout << '.';
    for (char ch: out){
        cout << ch;
        fout << ch;
    }
    cout << endl;
    fout << endl;
    return 0;







    //system("pause");
    return 0;
}
