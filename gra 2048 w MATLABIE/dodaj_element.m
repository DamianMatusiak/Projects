function K=dodaj_element(macierz)
%Funkcja pomocnicza zamieniaj¹ca losowy element macierzy, bêd¹cy zerem na 2
%lub 4
K=macierz;
X=find(K==0);%szukamy zer w naszym polu gry(dostajemy indeksy)
i=datasample(X,1);%wybieramy losowy indeks dla ktorego element macierzy==0
r=rand(1);%zmienna pomocnicza
if r>=0.5%jesli jest wieksza lub rowna 0.5 to
    K(i)=2;%nasz losowy element ktory jest zerem zamieniamy na 2
else %w przeciwnym przypadku to bêdzie 4
    K(i)=4;
end
end




