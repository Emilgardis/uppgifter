%Init
  t = linspace(0,6*pi,200) %skapar en matris från 0 till 6pi, med steg 200.

%beräkningar
  %plot a (aX,aY) (x,y) = (t cos t, t sin t)
    aX=t.*cos(t);
    aY=t.*sin(t);

  %plot b (bX,bY) (x,y) = (1.2^t cos t, 1.2^t sin t)
    bX = 1.2.^t.*cos(t);
    bY = 1.2.^t.*sin(t);

  %plot c (cX,cY) (x,y) = (t - sin t, 1 - cos t)
    cX = t-sin(t);
    cY = 1-cos(t);

%Grafisk rendering
  subplot(2,2,1)
  plot(aX,aY)
  title('Arkimedes spiral');
  subplot(2,2,2);
  plot(bX,bY)
  title('Logaritmisk spiral');
  subplot(2,2,3)
  axis([0 6*pi 0 2.2])
  plot(cX,cY)
  title('Cykloid');
  axis([0, 15])

%printing
  date = strftime("%s", localtime(time))
  file= ["spirals-" date ".png"]
  print(["spirals-" date ".png"])
  print(["Printed to: " "spirals-" date ".png" "[" "]"])
