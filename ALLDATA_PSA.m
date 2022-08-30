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
pickedChannel = [102 101 103 97 110 119 112 232 233 231];
pickedChannel = sort(pickedChannel);
% plot

figure
REG5 = [];REG10 = [];REG20 = [];RAND5 = [];RAND10 = [];RAND20 = [];
for index = 1:114
    allP = [];
    %if mod(index,6) == 1
    % load data
    data = load(route{index}{1});
    data = data.datamat;
    % average trial
    data = mean(data,3);
    % power spectrum estimate
    for channel = pickedChannel
        if mod(index,6) ==1 || mod(index,6) ==4
            % power spectrum estimate    start from 1.5s   
            % window size = 0.5s   overlap = 50%
            % ---  frequency resolution = nfft/fs
            [psa,freq] = pwelch(data(1160:3330,channel),900,810,6000,600);
            % append to array
            allP = [allP,psa];
        end
        if mod(index,6) ==2 || mod(index,6) ==5
            % power spectrum estimate    start from 1.5s   
            % window size = 0.5s   overlap = 50%
            % ---  frequency resolution = nfft/fs
            [psa,freq] = pwelch(data(1350:3330,channel),900,810,6000,600);
            % append to array
            allP = [allP,psa];
        end
        if mod(index,6) ==3 || mod(index,6) ==0
            % power spectrum estimate    start from 1.5s   
            % window size = 0.5s   overlap = 50%
            % ---  frequency resolution = nfft/fs
            [psa,freq] = pwelch(data(1830:3330,channel),900,810,6000,600);
            % append to array
            allP = [allP,psa];
        end
        channel
    end
    allP = mean(allP,2);
    filename = ['C:/Users/18146/Desktop/study/data/mat_pick_90overlap_900/power_spectrum' num2str(index)];
    save(filename, 'freq', 'allP')
    % show process 
    index
%     plot(freq,10*log10(allP))
%     hold on
    %end
    if mod(index,6) ==1
        REG5 = [REG5,allP];
    elseif mod(index,6) ==2
        REG10 = [REG10,allP];
    elseif mod(index,6) ==3
        REG20 = [REG20,allP];
    elseif mod(index,6) ==4
        RAND5 = [RAND5,allP];
    elseif mod(index,6) ==5
        RAND10 = [RAND10,allP];
    elseif mod(index,6) ==0
        RAND20 = [RAND20,allP];
    end
end 
REG5 = mean(REG5,2);REG10 = mean(REG10,2);REG20 = mean(REG20,2);RAND5 = mean(RAND5,2);RAND10 = mean(RAND10,2);RAND20 = mean(RAND20,2);
plot(freq,10*log10(REG5))
hold on 
plot(freq,10*log10(REG10))
hold on 
plot(freq,10*log10(REG20))
hold on 
plot(freq,10*log10(RAND5))
hold on 
plot(freq,10*log10(RAND10))
hold on 
plot(freq,10*log10(RAND20))
hold on 
xlabel('Frequency(Hz)')
ylabel('Power')
legend("REG5",'REG10','REG20','RAND5','RAND10','RAND20')
