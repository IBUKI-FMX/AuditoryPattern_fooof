% set filename 
route = cell(6*19,1);
for i = 1:114
    route{i} = join({'C:/Users/18146/Desktop/study/data/py_resultALL/power_spectrum',num2str(i),'.mat'},'');
end

target = zeros(19,6); targetSlope = zeros(19,6);
for index = 1:114
    data = load(route{index}{1});
    Rsquare = data.r_squared;
    if mod(index,6)
        target(ceil(index/6), mod(index,6)) = Rsquare;
    else
        target(ceil(index/6), 6) = Rsquare;
    end
end

figure
subplot(2,3,1)
histogram(target(:,1),7)
xlim([0,1])
xlabel('R^2')
ylabel('frequency')
title('REG5 R^2')

subplot(2,3,2)
histogram(target(:,2),7)
xlim([0,1])
xlabel('R^2')
ylabel('frequency')
title('REG10 R^2')

subplot(2,3,3)
histogram(target(:,3),7)
xlim([0,1])
xlabel('R^2')
ylabel('frequency')
title('REG20 R^2')

subplot(2,3,4)
histogram(target(:,4),7)
xlim([0,1])
xlabel('R^2')
ylabel('frequency')
title('RAND5 R^2')

subplot(2,3,5)
histogram(target(:,5),7)
xlim([0,1])
xlabel('R^2')
ylabel('frequency')
title('RAND10 R^2')

subplot(2,3,6)
histogram(target(:,6),7)
xlim([0,1])
xlabel('R^2')
ylabel('frequency')
title('RAND20 R^2')

% filename = 'C:/Users/18146/Desktop/study/data/ANOVA/R_square.xlsx';
% writematrix(target,filename,'Sheet',1,'Range','A1')


