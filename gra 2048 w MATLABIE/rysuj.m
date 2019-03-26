% to b�dzie to!
function [] = rysuj(A)
%A = [2,16,2,128;32,4,64,8;8 128 256 2;2 4 8 16];
fig = figure(1);

imagesc(log(A))  % kwadraciki z kolorkami
caxis([0 log(4096)/log(2)])
set(gca, 'XTick', []);  % wyczy�� o� X
set(gca, 'YTick', []);  % wyczy�� o� Y

for i=1:4
    for j=1:4
        text(j,i,int2str(A(i,j)),'HorizontalAlignment','center','fontsize',35); % wpisuje tekst (liczb�) w kwadrat
    end
end

end