% set filename 
route = cell(6,1);
for s = 5
    for i = 1:6
        route{i} = join({'C:/Users/18146/Desktop/study/data/Cond',num2str(i),'_S',num2str(s),'.mat'},'');
    end
end
% basic set
fs = 600;
t = -1500:1000/fs:5000;
t = t';
pickedChannel = [125 126 119 238 247 108 109 110 102 117];
pickedChannel = sort(pickedChannel);
% plot
for index = 1:6
    if mod(index,6) == 1
    % load data
    data = load(route{index}{1});
    data = data.datamat;
    % average trial
    data = mean(data,3);
    % power spectrum estimate
    for channel = 1:272
        if ismember(channel,pickedChannel) == 1
            figure
            spectrogram(data(:,channel),32,16,6000,600)
        end
    end
    end
end 


