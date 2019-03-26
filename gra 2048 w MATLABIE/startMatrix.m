function A = startMatrix()
A = zeros(4,4);                     % tworzymy macierz 4x4 z samymi zerami
A(randi([1,4]),randi([1,4])) = 2;   % dodajemy liczbê 2 w losowe miejsce tej macierzy
A(randi([1,4]),randi([1,4])) = 2;
end