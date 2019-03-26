function A = up(A)

for i = 1:4-1
    for j = 1:4
        if A(i,j) == A(i+1,j) & A(i+1,j) ~= 0            % Sprawdü, czy 2 sπsiednie niezerowe elementy sπ takie same
            A(i,j) = 2*A(i,j);                           % Jeúli tak, to je zsumuj
            A(i+1,j) = 0;                                % Wyzeruj 1 element z nich
        elseif A(i+1,j) == 0 & i < 3                     % W innym przypadku, gdy miÍdzy elementami jest 0:
            if A(i,j) == A(i+2,j) & A(i+2,j) ~= 0        % Sprawdü, czy niezerowe elementy po obu stronach 0 sπ takie same
            A(i,j) = 2*A(i,j);                           % Jeúli tak, to je zsumuj
            A(i+2,j) = 0;                                % Wyzeruj 1 element z nich
            elseif A(i+2,j) == 0 & i == 1                % W innym przypadku, jeúli pomiÍdzy elementami sπ 2 zera:
                if A(i,j) == A(i+3,j) & A(i+3,j) ~= 0    % Sprawdü, czy te niezerowe elementy sπ takie same
                    A(i,j) = 2*A(i,j);                   % Jeúli tak, to je zsumuj
                    A(i+3,j) = 0;
                end
            end
        end
    end
end
for i = 1:4
        nz = find(A(:,i)~=0);                                % Sprawdü, ktÛre elementy sπ niezerowe (nz)
        if length(nz) ~= 4                                   % PrzesuÒ te wiersze, ktÛre majπ zero
            A(:,i) = vertcat(A(nz,i), zeros(4-length(nz),1));% PrzesuÒ wszystkie niezerowe elementy w gÛrÍ
        end
end
end