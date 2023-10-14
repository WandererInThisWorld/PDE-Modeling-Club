% Modeling Club
clear; clc; close all;

% x'(t) = A*x(t)
% where x(t) is a vector of the coordinates, x'(t) represents the vector
% from the point, and A relates how the flow is relates to the position

% if x is in in R^n, then x' is in R^n, and A is an (n,n) matrix

% for example, given:
%   x' = 2x,
%   y' = -3y
% the equation is represented by
%   [x' = [2  0  * [x
%    y']   0 -3]    y]
% the solutions to these equations are:
%   x(t) = x(0)*exp(2t)
%   y(t) = y(0)*exp(-3t)
% the graph looks has a solution in the form y

