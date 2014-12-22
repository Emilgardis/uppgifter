clear
load co2.data
printf('Year: all: Max co2:%d. Min co2:%d\n',round(max(co2(:))),round(min(co2(:))))
printf('Year 1981: Max co2:%d. Min co2:%d\n',round(max(co2(1:26))),round(min(co2(1:26))))
printf('Year 1990: Max co2:%d. Min co2:%d\n',round(max(co2(209:234))),round(min(co2(209:234))))
printf('Year  all: Mean co2:%d\n',round(mean(co2)))
mean81 = round(mean(co2(1:26)))+0.0;
mean90 = round(mean(co2(209:234)))+0.0;
printf('Year 1981 vs 1990: Difference(%d/%d) = %f%%\n', mean81,mean90,mean81/mean90*100)

