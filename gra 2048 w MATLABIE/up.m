function A = up(A)

for i = 1:4-1
    for j = 1:4
        if A(i,j) == A(i+1,j) & A(i+1,j) ~= 0            % Sprawd�, czy 2 s�siednie niezerowe elementy s� takie same
            A(i,j) = 2*A(i,j);                           % Je�li tak, to je zsumuj
            A(i+1,j) = 0;                                % Wyzeruj 1 element z nich
        elseif A(i+1,j) == 0 & i < 3                     % W innym przypadku, gdy mi�dzy elementami jest 0:
            if A(i,j) == A(i+2,j) & A(i+2,j) ~= 0        % Sprawd�, czy niezerowe elementy po obu stronach 0 s� takie same
            A(i,j) = 2*A(i,j);                           % Je�li tak, to je zsumuj
            A(i+2,j) = 0;                                % Wyzeruj 1 element z nich
            elseif A(i+2,j) == 0 & i == 1                % W innym przypadku, je�li pomi�dzy elementami s� 2 zera:
                if A(i,j) == A(i+3,j) & A(i+3,j) ~= 0    % Sprawd�, czy te niezerowe elementy s� takie same
                    A(i,j) = 2*A(i,j);                   % Je�li tak, to je zsumuj
                    A(i+3,j) = 0;
                end
            end
        end
    end
end
for i = 1:4
        nz = find(A(:,i)~=0);                                % Sprawd�, kt�re elementy s� niezerowe (nz)
        if length(nz) ~= 4                                   % Przesu� te wiersze, kt�re maj� zero
            A(:,i) = vertcat(A(nz,i), zeros(4-length(nz),1));% Przesu� wszystkie niezerowe elementy w g�r�
        end
end
end