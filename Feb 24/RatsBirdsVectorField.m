
function F = RatsBirdsVectorField(V,a,b,c,d)
X = V(1); Y= V(2);
F1 = a*X - b*X.*Y;
F2 = c*X.*Y - d*Y;
F = [F1, F2];