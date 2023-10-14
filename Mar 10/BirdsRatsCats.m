clear; clc; close all;
% Birds-Cats-Rats equations (Prey-Predator-Prey Model)


a = 5; b = 3;
c = 2; d = 100;
e = 1; f = 1;
g = 1; h = 1;
S = 100;

% Finding Equilibria
fun = @(V)BirdsRatsCatsVectorField(V,a,b,c,d,e,f,g,h,S); 
V0 =[1,1,1];

Veq = fsolve(fun,V0);

% Quiver Plot / Vector Plot

[B,R,C] = meshgrid(0:1:30,0:1:30,0:1:30);
T1 = a.*B.*(1-R./d) - B.*e.*R./(S+B) - B.*g.*C./(B+R);
T2 = b.*R.*(1-e.*f.*R./(e.*S+f.*B)) - R.*h.*C./(B+R);
T3 = c.*C.*(1-g.*h.*C./(h.*B+g.*R));

TT = sqrt(T1.^2+T2.^2+T3.^2);


figure(1)
quiver3(B,R,C,T1./TT, T2./TT, T3./TT)
hold on
plot3(Veq(1),Veq(2),Veq(3),'ro','LineWidth',3)
plot3(0,0,0,'ro','LineWidth',3)

hold off
axis([0 20 0 10 0 10])

% Nulclines
% x = 0;
% x = d/c;
% y =0
% y = a/b;

% Solving equation

[t,y] = ode45(@(t,V) BirdsRatsCatsVectorField2(t,V,a,b,c,d,e,f,g,h,S),...
    [0 20],[0.1; 0.1; 0.01]);

figure(3)
plot(t,y(:,1),'LineWidth',1)
hold on
plot(t,y(:,2),'LineWidth',1)
plot(t,y(:,3),'LineWidth',1)
hold off
legend('birds','rats','cats')

figure(4)
plot3(y(:,1),y(:,2),y(:,3),'LineWidth',2)
xlabel('birds')
ylabel('rats')
zlabel('cats')
