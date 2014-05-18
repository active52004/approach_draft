close all;
clear all;
clc;
MaxValue = 256;

dir = './tmp/'
file1 = [dir,'frequency_4original1000.csv'];
file2 = [dir,'frequency_shift1000.csv'];
%file3 = [dir,'frequency_xorNonce_3000count.csv'];

S = 21998:22020;
B_S = dec2bin(S);
s_1=S(1):5:S(length(S));
bs1=dec2bin(s_1,16);

M1=csvread(file1);
M2=csvread(file2);
%M3=csvread(file3);

M_live = M1;
least = [];

%find all pattern value in column 1 as x, store in C

A = [0,17,34,51,68, 85, 102, 119, 136, 153, 170, 187,204, 221, 238, 255];
X = 0:255;
%Both no-pattern
B = setdiff(X,A);
D = B;
C = [];
for i=D
    for j=B
       C = [C i*256+j+1];
    end
end
M_tmp = M_live(C,2)/MaxValue;
scatter(C,M_tmp,20,'o','b');
%Both pattern
hold on
C=[];
B = A;
for i=A
    for j=B
       C = [C i*256+j+1];
    end
end
M_tmp = M_live(C,2)/MaxValue;
scatter(C,M_tmp,20,'fill','r');
%pattern and no-pattern
hold on
C=[];
B = setdiff(X,A);
for i=A
    for j=B
       C = [C i*256+j+1];
    end
end

for i=B
    for j=A
       C = [C i*256+j+1];
    end
end

for i=X
    for j=X
       k = i*256+j+1;
       if M_live(k,2)/MaxValue >0 && M_live(k,2)/MaxValue < 0.1
           least = [least k-1];
       end
    end
end
least = least';
str = dec2bin(least,16);
tmp_int = M_live(21845,2)
M_tmp = M_live(C,2)/MaxValue;
scatter(C,M_tmp,20,'v','g');


legend('Both no-pattern','Both pattern', 'Pattern and no-pattern')


set (gcf,'Position',[400,100,1000,400]);


%bar(S,[M1(S+1,2)/MaxValue M2(S+1,2)/MaxValue M3(S+1,2)/MaxValue]);
%{
hold on
bar(S,M2(S+1,2)/MaxValue);
hold on
bar(S,M3(S+1,2)/MaxValue);
legend('Only shift','Two rounds shuffle then shift','Xor the nonce')
set(gca,'XTick',s_1,'XTickLabel',bs1);
h = gca;
rotateticklabel(gca,'x',10);
%}

ylim([0 1]);
xlabel('Decimal Value of Input Message Block');
ylabel('No. of Distinct Tags/ Max No. of Distinct Tags');

%below is useless code

%plot(C,M1,'*');
%scatter(C,M_tmp,5,'fill','g');

%plot(M(:,1),M(:,2)/MaxValue);
%scatter(M(:,1),M(:,2)/MaxValue,5,'fill');
%text(x,y,'\leftarrow0101010111101110');

