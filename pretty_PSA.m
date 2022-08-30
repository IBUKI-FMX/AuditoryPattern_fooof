allP1 = [];allP2 = [];allP3 = [];allP4 = [];allP5 = [];allP6 = [];

for index = 61:66
    filename = ['C:/Users/18146/Desktop/study/data/mat_pick/power_spectrum' num2str(index)];
    data = load(filename);
    allP = data.allP;
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
end
freq = data.freq;

allP1 = mean(allP1,2);allP2 = mean(allP2,2);allP3 = mean(allP3,2);allP4 = mean(allP4,2);allP5 = mean(allP5,2);allP6 = mean(allP6,2);

figure
loglog(freq, allP1,'Color',[0.74,0.12,0.12]);hold on;
loglog(freq, allP2,'Color',[0.96,0.33,0.08]);hold on;
loglog(freq, allP3,'Color',[0.88,0.85,0.42]);hold on;
loglog(freq, allP4,'Color',[0.57,0.69,0.30]);hold on;
loglog(freq, allP5,'Color',[0.21,0.76,0.79]);hold on;
loglog(freq, allP6,'Color',[0.49,0.18,0.56]);hold off;
xlim([2,30])
ylabel('Power')
xlabel('frequency')
legend('REG5','REG10','REG20','RAND5','RAND10','RAND20')

filename = 'C:/Users/18146/Desktop/study/data/mat_pick_allGroup/power_spectrum1';
save(filename, 'freq', 'allP1')
filename = 'C:/Users/18146/Desktop/study/data/mat_pick_allGroup/power_spectrum2';
save(filename, 'freq', 'allP2')
filename = 'C:/Users/18146/Desktop/study/data/mat_pick_allGroup/power_spectrum3';
save(filename, 'freq', 'allP3')
filename = 'C:/Users/18146/Desktop/study/data/mat_pick_allGroup/power_spectrum4';
save(filename, 'freq', 'allP4')
filename = 'C:/Users/18146/Desktop/study/data/mat_pick_allGroup/power_spectrum5';
save(filename, 'freq', 'allP5')
filename = 'C:/Users/18146/Desktop/study/data/mat_pick_allGroup/power_spectrum6';
save(filename, 'freq', 'allP6')
