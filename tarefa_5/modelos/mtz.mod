param n;
param d{i in 1..n, j in 1..n : i != j} >= 0;

var x{i in 1..n, j in 1..n : i != j} binary;
var u{i in 1..n} integer >=1 , <= n-1;

minimize Z:
    sum{i in 1..n, j in 1..n : i!=j} d[i,j]*x[i,j];

subject to entrada {j in 1..n}:
    sum{i in 1..n: i != j} x[i,j] = 1;

subject to saida {i in 1..n}:
    sum{j in 1..n: j != i} x[i,j] = 1;

subject to mtz {i in 2..n , j in 2..n : i != j}:
    u[i] - u[j] + (n-1) * x[i,j] <= n-2;
