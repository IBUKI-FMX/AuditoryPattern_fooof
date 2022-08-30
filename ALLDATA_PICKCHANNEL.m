route = cell(6,1);
for s = 2:20
    for i = 1:6
        route{(s-2)*6+i} = join({'D:/Cond',num2str(i),'_S',num2str(s),'.mat'},'');
    end
end
fs = 600;
t = -1500:1000/fs:5000;
t = t';

%compare channels
pickedChannel = zeros(19*6,10);
pickedRank1 = [];
pickedRank2 = [];
for index = 1:(19*6)
    data = load(route{index}{1});
    data = data.datamat;
    pickedChannel(index,:) = pickcha(data);
    pickedRank1 = [pickedRank1,pickedChannel(index,1:5)];
    pickedRank2 = [pickedRank2,pickedChannel(index,6:10)];
end
tbl1 = tabulate(pickedRank1);
tbl2 = tabulate(pickedRank2);
figure
bar(tbl1(:,1),tbl1(:,2))
figure
bar(tbl2(:,1),tbl2(:,2))


%average trials
function pickedChannel = pickcha(data)
    averageT = mean(data,3);
    C = averageT(1320:3300,:);
    averageC = mean(C,1);

    [value,pickedChannel] = sort(averageC);
    pickedChannel = [pickedChannel(1:5) pickedChannel(268:272)]; 
end