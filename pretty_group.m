power = [];
for index = 1:114
    if mod(index,6) == 1||mod(index,6) == 2||mod(index,6) == 3
        filename = ['C:/Users/18146/Desktop/study/data/mat_pick/power_spectrum' num2str(index)];
        data = load(filename);
        power = [power,data.allP];
    end
end
freq = data.freq;
filename = 'C:/Users/18146/Desktop/study/data/groupREG';
save(filename, 'freq', 'power')

power = [];
for index = 1:114
    if mod(index,6) == 4||mod(index,6) == 5||mod(index,6) == 0
        filename = ['C:/Users/18146/Desktop/study/data/mat_pick/power_spectrum' num2str(index)];
        data = load(filename);
        power = [power,data.allP];
    end
end
freq = data.freq;
filename = 'C:/Users/18146/Desktop/study/data/groupRAND';
save(filename, 'freq', 'power')