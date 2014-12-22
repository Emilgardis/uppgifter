% variabeln t, i 250 steg fr ̊an 0 till 6pi
t = linspace(0,6*pi,250);
% variabeln t, i 250 steg fr ̊an 0 till 6pi t=linspace(0,6*pi,250);
%a
xa=t.*cos(t); ya=t.*sin(t);
%b
xb=1.2.^t.*cos(t); yb=1.2.^t.*sin(t); %c
xc=t-sin(t); yc=1-cos(t);
   subplot(2,2,1);
   plot(xa,ya);
   title('Arkimedes spiral');
   axis([-17 20 -19 16]);
   subplot(2,2,2);
   plot(xb,yb);
   title('Logaritmisk spiral');
   axis([-19 32 -25 14]);
   subplot(2,2,3);
   plot(xc,yc);
   title('Cykloid');
   axis([0 6*pi 0 2.2]);
   print('treplotar.png')
