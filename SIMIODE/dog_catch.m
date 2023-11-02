%% Code from Kyle

clc
clf
clear
g=9.81;
tf=10;
dt=0.01;
x0=0;
y0=5;
v0=sqrt(2)/2;
theta=45;
%EOM
t=0:dt:tf;
x=x0+v0*cosd(theta)*t;
y=y0+v0*sind(theta)*t-0.5*g*t.^2; %
%delete negative y values
aa=find(y<0);
t(aa)=[];
x(aa)=[];
y(aa)=[];
%Adjusting Plot 
plot(x,y,'--');
hold on
h=plot(x(1),y(1), 'ro', 'MarkerfaceColor', 'r');
line=plot([0 10],[0 y(1)], 'k', 'LineWidth', 2);
plot([0 x(length(x))], [0 y(length(y))], 'b', 'LineWidth', 2);
hold on;
plot([0 0],[0 50], 'b', 'Linewidth', 2); 
hold on;
for ii=1:1:length(x)
    set (h, 'XData',x(ii));
    set (h, 'YData' ,y(ii));
    %drawnow:
    set (line, 'XData', [0 x(ii)]); 
    set (line, 'YData', [0 y(ii)]);
    %drawnow;
    area(1,5)
    pause (0.001);
end


%% Course correction

