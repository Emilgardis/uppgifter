
  % ---------------------------------------------------------
  % Program: templab.m
  % Author: Fredrik Jansson, fja@forsmarksskola.se
  % Purpose: Plot temperatures in Forsmark during a short period.
  % Version: 20140114_01
  % ---------------------------------------------------------
  dag = [ 1 2 3 4 5 6 7 8 9];
  temp = [ 5 10 8 8 5 2 -8 -4 -5];
  p1 = polyfit(dag,temp,1)
  p2 = polyfit(dag,temp,2)
  xcurve = 0:0.5:12;
  p1curve = polyval(p1,xcurve);
  p2curve = polyval(p2,xcurve);
  plot(xcurve,p1curve,'--',xcurve,p2curve,'-.', dag,temp,'*')
  xlabel('dagar')
  ylabel('temp')
  box off
  grid on
  title('Temperaturen i Forsmark 2013')
  ylim( [ -10 20 ] )
  print('templab.png')
