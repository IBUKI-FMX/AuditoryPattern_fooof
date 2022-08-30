route = cell(6,1);
for s = 2:20
    for i = 1:6
        route{(s-2)*6+i} = join({'D:/Cond',num2str(i),'_S',num2str(s),'.mat'},'');
    end
end
fs = 600;
t = -1500:1000/fs:5000;
t = t';

for index = 1:(6*19)
    allP = [];
    pickChannel = [];
    % load data
    data = load(route{index}{1});
    data = data.datamat;
    % pick channels
    pickChannel = pickcha(data);
    % average trial
    data = mean(data,3);
    % power spectrum estimate
    for channel = 1:272
        if ismember(channel,pickChannel) == 1
            % power spectrum estimate    start from 1.5s   
            % window size = 0.5s   overlap = 50%
            % ---  frequency resolution = nfft/fs
            [psa,freq] = pwelch(data(900:end,channel),300,270,6000,600);
            % append to array
            allP = [allP,psa];
        end
    end
    allP = mean(allP,2);
%     filename = ['C:/Users/18146/Desktop/study/data/mat_pickNew/power_spectrum' num2str(index)];
%     save(filename, 'freq', 'allP')
end 


%average trials
function pickedChannel = pickcha(data)
    averageT = mean(data,3);
    C = averageT(1320:3300,:);
    averageC = mean(C,1);

    [value,pickedChannel] = sort(averageC);
    pickedChannel = [pickedChannel(1:5) pickedChannel(268:272)]; 
end