% set filename 
route = cell(6*19,1);
for s = 2:20
    for i = 1:6
        route{(s-2)*6+i} = join({'D:/Cond',num2str(i),'_S',num2str(s),'.mat'},'');
    end
end

% basic setting
fs = 600;
t = -1500:1000/fs:5000;
t = t';

% channels picked before
pickedChannel = [102 101 103 97 110 119 112 232 233 231];
pickedChannel = sort(pickedChannel);

Alldata = zeros(3901,6);
for index = 1:114
    data = load(route{index}{1});
    data = data.datamat;
    data = mean(data,3);
    pData = zeros(3901,10);
    i =1;
    for index2 = pickedChannel
        % root mean suqare amplitude
        pData(:,1) = (data(:,index2).^2);
        i =1 +1;
    end
    % plot
    pData = sqrt(mean(pData,2));
    if mod(index,6)
        Alldata(:,mod(index,6)) = Alldata(:,mod(index,6))+pData;
    else
        Alldata(:,6) = Alldata(:,6)+pData;
    end
    index
end 
Alldata = Alldata ./19;

% plot all
figure
plot(t(600:end), Alldata(600:end,1),'Color',[0.74,0.12,0.12]);hold on;
plot(t(600:end), Alldata(600:end,2),'Color',[0.96,0.33,0.08]);hold on;
plot(t(600:end), Alldata(600:end,3),'Color',[0.88,0.85,0.42]);hold on;
plot(t(600:end), Alldata(600:end,4),'Color',[0.57,0.69,0.30]);hold on;
plot(t(600:end), Alldata(600:end,5),'Color',[0.21,0.76,0.79]);hold on;
plot(t(600:end), Alldata(600:end,6),'Color',[0.49,0.18,0.56]);hold off;
ylabel('RMS Power')
xlabel('Time(millisecond)')
legend('REG5','REG10','REG20','RAND5','RAND10','RAND20')

% plot REG5-RAND5
figure
plot(t(600:end), Alldata(600:end,1),'Color',[0.74,0.12,0.12]);hold on;
plot(t(600:end), Alldata(600:end,4),'Color',[0.57,0.69,0.30]);hold off;
ylabel('RMS Power')
xlabel('Time(millisecond)')
title('REG5-RAND5')
legend('REG5','RAND5')

% plot REG10-RAND10
figure
plot(t(600:end), Alldata(600:end,2),'Color',[0.96,0.33,0.08]);hold on;
plot(t(600:end), Alldata(600:end,5),'Color',[0.21,0.76,0.79]);hold off;
ylabel('RMS Power')
xlabel('Time(millisecond)')
title('REG10-RAND10')
legend('REG10','RAND10')

% plot REG20-RAND20
figure
plot(t(600:end), Alldata(600:end,3),'Color',[0.88,0.85,0.42]);hold on;
plot(t(600:end), Alldata(600:end,6),'Color',[0.49,0.18,0.56]);hold off;
ylabel('RMS Power')
title('REG20-RAND20')
xlabel('Time(millisecond)')
legend('REG20','RAND20')

% plot all REG
figure
plot(t(600:end), Alldata(600:end,1),'Color',[0.74,0.12,0.12]);hold on;
plot(t(600:end), Alldata(600:end,2),'Color',[0.96,0.33,0.08]);hold on;
plot(t(600:end), Alldata(600:end,3),'Color',[0.88,0.85,0.42]);hold off;
ylabel('RMS Power')
xlabel('Time(millisecond)')
title('REG')
legend('REG5','REG10','REG20')

% plot all RAND
figure
plot(t(600:end), Alldata(600:end,4),'Color',[0.57,0.69,0.30]);hold on;
plot(t(600:end), Alldata(600:end,5),'Color',[0.21,0.76,0.79]);hold on;
plot(t(600:end), Alldata(600:end,6),'Color',[0.49,0.18,0.56]);hold off;
ylabel('RMS Power')
xlabel('Time(millisecond)')
title('RAND')
legend('RAND5','RAND10','RAND20')


filename = ['C:/Users/18146/Desktop/study/data/Alldata_for_prettyAmplitude'];
save(filename, 'Alldata')