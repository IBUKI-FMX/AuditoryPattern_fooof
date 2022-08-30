% set filename 
route = cell(6*19,1);
for s = 2:20
    for i = 1:6
        route{(s-2)*6+i} = join({'D:/Cond',num2str(i),'_S',num2str(s),'.mat'},'');
    end
end
% basic set
fs = 600;
t = -1500:1000/fs:5000;
t = t';
pickedChannel = [102 101 103 97 110 96 243 109 119 112 118 113 232 233 231 227];
pickedChannel = sort(pickedChannel);
% plot
allP1 = [];allP2 = [];allP3 = [];allP4 = [];allP5 = [];allP6 = [];

figure
for index = 1:(6*19)
    allP = [];
    % load data
    data = load(route{index}{1});
    data = data.datamat;
    % average trial
    data = mean(data,3);
    % power spectrum estimate
    for channel = 1:272
            % power spectrum estimate    start from 1.5s   
            % window size = 0.5s   overlap = 50%
            % ---  frequency resolution = nfft/fs
            [psa,freq] = pwelch(data(900:end,channel),300,270,6000,600);
            % append to array
            allP = [allP,psa];
    end

    allP = mean(allP,2);
    if mod(index, 6) == 1
        allP1 = [allP1,allP];
    elseif mod(index, 6) == 2
          allP2 = [allP2,allP];  
    elseif mod(index, 6) == 3
          allP3 = [allP3,allP]; 
    elseif mod(index, 6) == 4
          allP4 = [allP4,allP];
    elseif mod(index, 6) == 5
          allP5 = [allP5,allP];
    elseif mod(index, 6) == 0
          allP6 = [allP6,allP];
    end
    % show process 
    index
    filename = ['C:/Users/18146/Desktop/study/data/matpickALLCHANNEL/power_spectrum' num2str(index)];
    save(filename, 'freq', 'allP')
end 
allP1 = mean(allP1,2);allP2 = mean(allP2,2);allP3 = mean(allP3,2);allP4 = mean(allP4,2);allP5 = mean(allP5,2);allP6 = mean(allP6,2);
plot(freq,10*log10(allP1))
hold on
plot(freq,10*log10(allP2))
hold on
plot(freq,10*log10(allP3))
hold on
plot(freq,10*log10(allP4))
hold on
plot(freq,10*log10(allP5))
hold on
plot(freq,10*log10(allP6))
hold off
legend("REG5",'REG10','REG20','RAND5','RAND10','RAND20')
