power = [];
for index = 1:114
    if mod(index,6) == 1||mod(index,6) == 2||mod(index,6) == 3
        filename = ['C:/Users/18146/Desktop/study/data/mat_pick/power_spectrum' num2str(index)];
        data = load(filename);
        power = [power,data.allP];
    end
end
freq = data.freq;

slope = 1./(freq.^2);

loglog(freq,slope)