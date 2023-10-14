function F = BirdsRatsCatsVectorField(V,a,b,c,d,e,f,g,h,S)
B = V(1); R = V(2); C = V(3);
F1 = a.*B.*(1-R./d) - B.*e.*R./(S+B) - B.*g.*C./(B+R);
F2 = b.*R.*(1-e.*f.*R./(e.*S+f.*B)) - R.*h.*C./(B+R);
F3 = c.*C.*(1-g.*h.*C./(h.*B+g.*R));
F = [F1, F2, F3];