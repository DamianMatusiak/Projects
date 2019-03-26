function A = left(A)
% left
for i = 1:4
    for j = 1:4-1
        if A(i,j) == A(i,j+1) & A(i,j+1) ~= 0            % Sprawdü, czy 2 sπsiednie niezerowe elementy sπ takie same
            A(i,j) = 2*A(i,j);                           % Jeúli tak, to je zsumuj
            A(i,j+1) = 0;                                % Wyzeruj 1 element z nich
        elseif A(i,j+1) == 0 & j < 3                     % W innym przypadku, gdy miÍdzy elementami jest 0:
            if A(i,j) == A(i,j+2) & A(i,j+2) ~= 0        % Sprawdü, czy niezerowe elementy po obu stronach 0 sπ takie same
            A(i,j) = 2*A(i,j);                           % Jeúli tak, to je zsumuj
            A(i,j+2) = 0;                                % Wyzeruj 1 element z nich
            elseif A(i,j+2) == 0 & j == 1                % W innym przypadku, jeúli pomiÍdzy elementami sπ 2 zera:
                if A(i,j) == A(i,j+3) & A(i,j+3) ~= 0    % Sprawdü, czy te niezerowe elementy sπ takie same
                    A(i,j) = 2*A(i,j);                   % Wyzeruj 1 element z nich
                    A(i,j+3) = 0;
                end
            end
        end
    end
end
for i = 1:4
        nz = find(A(i,:)~=0);                                % Sprawdü, ktÛre elementy sπ niezerowe (nz)
        if length(nz) ~= 4                                   % PrzesuÒ te wiersze, ktÛre majπ zero
            A(i,:) = [A(i,nz) zeros(1,4-length(nz))];        % PrzesuÒ wszystkie niezerowe elementy w lewo
        end
end
end