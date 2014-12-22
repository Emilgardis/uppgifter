printf('Laddar Värden...\n')
clear
load VaderData.mat %Innehållet T

data = [81 82 83 84 85 86 87 88 89 90 ]; %Rad 1 är åren, rad 2 är max-, rad 3 är min- och slutligen rad 4 är medel-


for n = 1:10
  data(2, n) = round(max(T(:,n,:))); %Max-värdet varje år 
  data(3, n) = round(min(T(:,n,:))); %Minsta-värdet varje år
  data(4, n) = round(mean(T(:,n,:))); %Medelvärdet varje år
end 
printf("Max      temperatur år -81 till -90: \n")
fprintf(1,'%4d',data(2,:))
subplot(3,3,1)
bar(data(2,:))
title('Max temp 89 - 90')
ylim([0 30])
xlim([1 10])

printf("\nMinsta temperatur år -81 till -90: \n")
fprintf(1,'%4d',data(3,:))
subplot(3,3,2)
bar(data(3,:))
title('Min temp 89 - 90')
xlim([1 10])

printf("\nMedel  temperatur år -81 till -90: \n")
fprintf(1,'%4d',data(4,:))
subplot(3,3,4)
bar(data(4,:))
title('Medel temp 89 - 90')
ylim([0 30])
xlim([1 10])
legend("Hello","Hi","lol")

[varmastT, iVarmastT] = max(data(2,:));
[kallastT,iKallastT] = min(data(3,:));
printf('År %d var varmast med en temperatur på %d',iVarmastT,varmastT)
printf('År %d var kallast med en temperatur på %d',iKallastT,kallastT)


subplot(3,3,5)
imagesc(T)
title('Temperaturen genom alla tio år')
%delete('imagescT.png')
%print('imagescT.png')
colorbar('EastOutside')
%delete('imagescTVert.png')
%print('imagescTVert.png')

for i = 1:10
  jan(i,:) = T(1:31,i,:); %januari 1-31
  feb(i,:) = T(32:59,i,:); %februari 32 - 5
  mar(i,:) = T(60:90,i,:); %mars
  apr(i,:) = T(91:120,i,:); %april
  maj(i,:) = T(122:151,i,:); %maj
  jun(i,:) = T(152:181,i,:); %juni
  jul(i,:) = T(182:212,i,:); %juli
  aug(i,:) = T(213:243,i,:); %augusti
  sep(i,:) = T(244:273,i,:); %september
  okt(i,:) = T(274:304,i,:); %oktober
  nov(i,:) = T(305:334,i,:); %november
  dec(i,:) = T(335:365,i,:); %december
end


%jan(1,30) = januari år 81 dag 30
[kJTemp, iKJTemp ] = min(min(jan))
printf('Kallast januari var år %d, med en temperatur på %d', iKJTemp, kJTemp)
subplot(3,3,5)
bar(min(jan(:,:,:)))
title('Januari 89 - 90 -- Kallaste Dagarna')
xlabel("year")
ylabel("temp")
fig = gcf()
