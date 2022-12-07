#include "bits/stdc++.h"
using namespace std;

#define TRI_INSIDE 1
#define TRI_ONSIDE -1
#define TRI_OUTSIDE 0
#define EPSILON 0.0001

struct Point2D {
  double x;
  double y;
};

struct Triangle {
  struct Point2D A;
  struct Point2D B;
  struct Point2D C;
};

double area(struct Point2D A, struct Point2D B, struct Point2D C) {
  return 0.5 * fabs(A.x * (B.y - C.y) + B.x * (C.y - A.y) + C.x * (A.y - B.y));
}

int fEqual(double a, double b) {
  return (fabs(a - b) < EPSILON) ? 1 : 0;
}

int checkPosition(struct Triangle tri, struct Point2D pM) {
  const double areaABM = area(tri.A, tri.B, pM);
  const double areaACM = area(tri.A, tri.C, pM);
  const double areaBCM = area(tri.B, tri.C, pM);
  const double areaABC = area(tri.A, tri.B, tri.C);
  const double d = (areaABM + areaACM + areaBCM) - areaABC;
  if (d > 0)
    return TRI_OUTSIDE;
  else if (fEqual(areaABM, 0) || fEqual(areaACM, 0) || fEqual(areaBCM, 0))
    return TRI_ONSIDE;
  else
    return TRI_INSIDE;
}

int main() {
  struct Point2D A, B, C;
  int n;
  cin >> A.x >> A.y >> B.x >> B.y >> C.x >> C.y;
  cin >> n;
  int cnt = 0;
  struct Triangle tri;
  tri.A = A;
  tri.B = B;
  tri.C = C;
  for (int i = 0; i < n; i++){
    int c, d;
    Point2D P;
    cin >> P.x >> P.y;
    if(checkPosition(tri, P) == 1 || checkPosition(tri, P) == -1) cnt++;
  }
    double s = n*area(A, B, C)*10/10;
    cout << setprecision(2) << fixed << s << endl;

  return 0;
}