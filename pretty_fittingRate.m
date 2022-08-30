% set filename 
route = cell(6*19,1);
for i = 1:114
    route{i} = join({'C:/Users/18146/Desktop/study/data/py_600_90over/power_spectrum',num2str(i),'.mat'},'');
end

figure
target = zeros(19,6);
for index = 1:114
%     data = load(route{index}{1});
%     if size(data.peak_params,1) ==1&&data.peak_params(1,1)<=15&&data.peak_params(1,1)>=8&&data.peak_params(1,3)<11
%         alphaP = data.peak_params(1,2);
%     elseif size(data.peak_params,1) ==2&&data.peak_params(1,1)<=15&&data.peak_params(1,1)>=8&&data.peak_params(1,3)<11
%         alphaP = data.peak_params(1,2);
%     elseif size(data.peak_params,1) ==2&&data.peak_params(2,1)<=15&&data.peak_params(2,1)>=8&&data.peak_params(2,3)<11
%         alphaP = data.peak_params(2,2);
%     elseif size(data.peak_params,1) ==3&&data.peak_params(1,1)<=15&&data.peak_params(1,1)>=8&&data.peak_params(1,3)<11
%         alphaP = data.peak_params(1,2);
%     elseif size(data.peak_params,1) ==3&&data.peak_params(2,1)<=15&&data.peak_params(2,1)>=8&&data.peak_params(2,3)<11
%         alphaP = data.peak_params(2,2);
%     elseif size(data.peak_params,1) ==3&&data.peak_params(3,1)<=15&&data.peak_params(3,1)>=8&&data.peak_params(3,3)<11
%         alphaP = data.peak_params(3,2);
%     else
%         alphaP = 0;
%     end
    data = load(route{index}{1});
    if size(data.peak_params,1) ==2&&data.peak_params(1,1)>=19&&data.peak_params(1,1)<=21&&data.peak_params(1,3)<5
        Hz20 = data.peak_params(1,1);
    elseif size(data.peak_params,1) ==2&&data.peak_params(2,1)>=19&&data.peak_params(2,1)<=21&&data.peak_params(2,3)<5
        Hz20 = data.peak_params(2,1);
    elseif size(data.peak_params,1) ==1&&data.peak_params(1,1)>=19&&data.peak_params(1,1)<=21&&data.peak_params(1,3)<5
        Hz20 = data.peak_params(1,1);
    elseif size(data.peak_params,1) ==3&&data.peak_params(2,1)>=19&&data.peak_params(2,1)<=21&&data.peak_params(2,3)<5
        Hz20 = data.peak_params(2,1);
    elseif size(data.peak_params,1) ==3&&data.peak_params(3,1)>=19&&data.peak_params(3,1)<=21&&data.peak_params(3,3)<5
        Hz20 = data.peak_params(3,1);
    else
        Hz20 = 0;
    end
%     if mod(index,6)
%         target(ceil(index/6), mod(index,6)) = Hz20;
%     else
%         target(ceil(index/6), 6) = Hz20;
%     end
%     if mod(index,6)
%         target(ceil(index/6), mod(index,6)) = alphaP;
%     else
%         target(ceil(index/6), 6) = alphaP;
%     end
    if mod(index,6)
        target(ceil(index/6), mod(index,6)) = Hz20;
    else
        target(ceil(index/6), 6) = Hz20;
    end
end

distrution = [sum(target(:,1)~=0) sum(target(:,2)~=0) sum(target(:,3)~=0) sum(target(:,4)~=0) sum(target(:,5)~=0) sum(target(:,6)~=0)];
distrution = distrution ./ 19;

% bar(distrution)
% set(gca,'XTickLabel',["REG5",'REG10','REG20','RAND5','RAND10','RAND20'])
% title('Alpha Fitting Rate')
% ylabel('Percentage')
bar(distrution)
set(gca,'XTickLabel',["REG5",'REG10','REG20','RAND5','RAND10','RAND20'])
title('25% overlap fitting rate')
ylabel('Percentage')
ylim([0,1])

