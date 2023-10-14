% Modeling Club - February 24, 2023
clear; clc; close all;

% Bird-Rats Model
% Bdot = a*B(1-B/e) - B*/(S+B) * (c*R)
% Rdot = b*R(1 - c*d*R/(c*S + d*B))
% 


a = 2; b= 3;
c = 1; d = 1;

% Finding Equilibria
fun = @(V)RatBirdsVectorField(V,a,b,c,d); 
V0 =[1,1];

Veq = fsolve(fun,V0);

[a1, a2, a3, a4, a5] = fsolve(fun, V0);






