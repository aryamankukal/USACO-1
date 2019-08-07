/*
ID: wrwwctb1
LANG: C++14
TASK: milk4
*/

#include <stdio.h>
#include <stdlib.h>
#define MAXQ 20001
#define MAXP 101
#define INF  0x7fffffff
#include <vector>
int betterSequence (int a, int b, int l[], int n[]);
int compare (const void *a, const void *b);

int Q, P;
int pail[MAXP];
int s[MAXQ];
int l[MAXQ];
int n[MAXQ];

int main (){
    FILE *fin = fopen ("milk4.in", "r");
    fscanf (fin, "%d %d", &Q, &P);
    for (int i = 1; i <= P; i++)
	    fscanf (fin, "%d", &(pail[i]));
    fclose (fin);
    qsort (pail+1, P, sizeof (pail[0]), compare);


    for (int i = 0; i <= Q; i++) {
        s[i] = INF;
        l[i] = 0;
        n[i] = 0;
    }

    s[0] = 0;

    for (int i = 1; i <= P; i++) {
        int ts[MAXQ], tl[MAXQ], tn[MAXQ];

        for (int q = 0; q <= Q; q++) {
            ts[q] = s[q];
            tl[q] = l[q];
            tn[q] = n[q];
        }

        for (int q = pail[i]; q <= Q; q++) {
            int prevq = q - pail[i];

            if (ts[prevq] < INF){
                if (tl[prevq] == pail[i]) {
                    ts[q] = ts[prevq];
                    tl[q] = pail[i];
                    tn[q] = tn[prevq] + 1;
                }else{
                    ts[q] = ts[prevq] + 1;
                    tl[q] = pail[i];
                    tn[q] = 1;
                }

                if (s[prevq] < INF &&
                    (s[prevq] + 1 < ts[q] ||
                     (s[prevq] + 1 == ts[q] &&
                      betterSequence (prevq, q - tn[q] * pail[i], l, n)
                     )
                    )
                   ) {
                    ts[q] = s[prevq] + 1;
                    tl[q] = pail[i];
                    tn[q] = 1;
                }
            }
        }

        for (int q = pail[i]; q <= Q; q++)
            if (ts[q] <= s[q]) {
                s[q] = ts[q];
                l[q] = tl[q];
                n[q] = tn[q];
            }
    }


    int q = Q;
    std::vector<int> traced;
    while (q > 0){
        printf(" %d %d %d\n", q, l[q], n[q]);
	    traced.push_back(l[q]);
	    q -= l[q] * n[q];
    }


    FILE *fout = fopen ("milk4.out", "w");
    fprintf (fout, "%d", s[Q]);

    for (int i = 0; i < s[Q]; i++)
	    fprintf (fout, " %d", traced[i]);
    fprintf (fout, "\n");
    fclose (fin);

    return 0;
}



int betterSequence (int a, int b, int l[], int n[]){
    if (a == b)
        return 0;
    while (a && b) {
        if (l[a] < l[b])
            return 1;
        if (l[a] > l[b])
            return 0;

        a -= n[a] * l[a];
        b -= n[b] * l[b];
    }

    if (a)
	    return 0;
    return 1;
}

int compare (const void *a, const void *b){
    return *(int *) b - *(int *) a;
}
