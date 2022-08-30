% set filename 
route = cell(6*19,1);
for i = 1:114
    route{i} = join({'C:/Users/18146/Desktop/study/data/py_pick_differentcha/power_spectrum',num2str(i),'.mat'},'');
end

targetOff = zeros(19,6); targetSlope = zeros(19,6);
for index = 1:114
    data = load(route{index}{1});
    offSet = data.aperiodic_params(1,1);
    slope = data.aperiodic_params(1,2);
    if mod(index,6)
        targetOff(ceil(index/6), mod(index,6)) = offSet;
        targetSlope(ceil(index/6), mod(index,6)) = slope;
    else
        targetOff(ceil(index/6), 6) = offSet;
        targetSlope(ceil(index/6), 6) = slope;
    end
end
% x = 1:6;
figure
boxplot(targetOff, ["REG5",'REG10','REG20','RAND5','RAND10','RAND20'])
ylabel('Offset')
% Hdl1 = violinChart(gca,x,targetOff,[0 0.447 0.741],0.2);
figure
% Hdl2 = violinChart(gca,x,targetSlope,[0 0.447 0.741],0.2);
boxplot(targetSlope, ["REG5",'REG10','REG20','RAND5','RAND10','RAND20'])
ylabel('Slope')

filename = 'C:/Users/18146/Desktop/study/data/PSAtrial_offset.xlsx';
writematrix(targetOff,filename,'Sheet',1,'Range','A1')
filename = 'C:/Users/18146/Desktop/study/data/PSAtrial_slope.xlsx';
writematrix(targetSlope,filename,'Sheet',1,'Range','A1')

function Hdl=violinChart(ax,X,Y,FaceColor,width)
% @author slandarer
% Hdl: 返回的图形对象句柄结构体
% - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
% Hdl.F_density(i)   | patch   | 核密度分布
% Hdl.F_outlier(i)   | scatter | 离群值点
% Hdl.F_range95(i)   | line    | 去除离群值点后最大值及最小值
% Hdl.F_quantile(i)  | patch   | 四分位数框
% Hdl.F_medianLine(i)| line    | 中位数
%
% Hdl.F_legend       | patch   | 用于生成legend图例的图形对象
% - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
% 请使用如下方式生成图例：
% Hdl1=violinChart(ax,X,Y,... ...)
% Hdl2=violinChart(ax,X,Y,... ...)
% ... ...
% legend([Hdl1,Hdl2,... ...],{Name1,Name2,...})
% ===========================================================
% 以下为使用实例代码：
% - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
% X1=[1:2:7,13];
% Y1=randn(100,5)+sin(X1);
% X2=2:2:10;
% Y2=randn(100,5)+cos(X2);
% 
% Hdl1=violinChart(gca,X1,Y1,[0     0.447 0.741],0.5);
% Hdl2=violinChart(gca,X2,Y2,[0.850 0.325 0.098],0.5);
% legend([Hdl1.F_legend,Hdl2.F_legend],{'randn+sin(x)','randn+cos(x)'});

if nargin<5
    width=0.4;
end

if ~isempty(ax)
else
    ax=gca;
end
hold(ax,'on');

oriX=X;
X=unique(X);
sep=min(diff(X));
for i=1:length(X)
    if length(oriX)==numel(Y)
        tY=Y(oriX==X(i));
    else
        tY=Y(:,i);
    end
    [f,yi]=ksdensity(tY);
    Hdl.F_density(i)=fill([f,-f(end:-1:1)].*sep.*width+X(i),[yi,yi(end:-1:1)],FaceColor);
    
    outliBool=isoutlier(tY,'quartiles');
    outli=tY(outliBool);
    Hdl.F_outlier(i)=scatter(repmat(X(i),[length(outli),1]),outli,20,'filled',...
                    'CData',[1 1 1],'MarkerEdgeColor','none');
    nY=tY(~outliBool);
    Hdl.F_range95(i)=plot([X(i),X(i)],[min(nY),max(nY)],'k','lineWidth',1);
    
    qt25=quantile(tY,0.25);
    qt75=quantile(tY,0.75);
    
    Hdl.F_quantile(i)=fill(X(i)+0.6.*sep.*width.*[-1 1 1 -1].*max(f),...
                    [qt25,qt25,qt75,qt75],[1 1 1],...
                    'EdgeColor',[0 0 0]);
                
    med=median(tY);
    Hdl.F_medianLine(i)=plot(X(i)+0.6.*sep.*width.*[-1 1].*max(f),[med,med],'LineWidth',3,...
                    'Color',[0 0 0]);
end

Hdl.F_legend=Hdl.F_density(1);
end