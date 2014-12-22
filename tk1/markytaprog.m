clear
load markyta.txt;
printf('Highest altitude: %d m\n', round(max(max(markyta))));
subplot(1,2,1);
imagesc(markyta);
colorbar('EastOutside');
subplot(1,2,2);
imagesc(markyta);
axis([65 75 100 105]);
colorbar('EastOutside');
printf('Mean altitude of hill: %d m\n', round(mean(mean(markyta(100:105,65:75)))));
date = strftime("%s", localtime(time));
print(["hills-" date ".png"]);
