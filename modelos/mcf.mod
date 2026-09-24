param n;
param d{i in 1..n, j in 1..n : i != j} >= 0;

var x{i in 1..n, j in 1..n : i != j} binary;
var f{i in 1..n, j in 1..n, k in 2..n : i != j} >= 0;

minimize Z:
    sum{i in 1..n, j in 1..n : i != j} d[i,j] * x[i,j];

subject to entrada {j in 1..n}:
    sum{i in 1..n : i != j} x[i,j] = 1;

subject to saida {i in 1..n}:
    sum{j in 1..n : j != i} x[i,j] = 1;

subject to origem {k in 2..n}:
    sum{j in 1..n : j != 1} f[1,j,k]-sum{j in 1..n : j != 1} f[j,1,k] = 1;

subject to destino {k in 2..n}:
    sum{j in 1..n : j != k} f[k,j,k] - sum{j in 1..n : j != k} f[j,k,k] = -1;

subject to transito {i in 2..n, k in 2..n : i != k}:
    sum{j in 1..n : j != i} f[i,j,k] - sum{j in 1..n : j != i} f[j,i,k] = 0;

subject to acoplamento {i in 1..n, j in 1..n, k in 2..n : i != j}:
    f[i,j,k] <= x[i,j];
