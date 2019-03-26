function A = right(A)
% left
for i = 1:4
    for j = 4:-1:2
        if A(i,j) == A(i,j-1) & A(i,j-1) ~= 0            % Sprawd�, czy 2 s�siednie niezerowe elementy s� takie same
            A(i,j) = 2*A(i,j);                           % Je�li tak, to je zsumuj
            A(i,j-1) = 0;                                % Wyzeruj 1 element z nich
        elseif A(i,j-1) == 0 & j > 2                     % W innym przypadku, gdy mi�dzy elementami jest 0:
            if A(i,j) == A(i,j-2) & A(i,j-2) ~= 0        % Sprawd�, czy niezerowe elementy po obu stronach 0 s� takie same
            A(i,j) = 2*A(i,j);                           % Je�li tak, to je zsumuj
            A(i,j-2) = 0;                                % Wyzeruj 1 element z nich
            elseif A(i,j-2) == 0 & j == 4                % W innym przypadku, je�li pomi�dzy elementami s� 2 zera:
                if A(i,j) == A(i,j-3) & A(i,j-3) ~= 0    % Sprawd�, czy te niezerowe elementy s� takie same
                    A(i,j) = 2*A(i,j);                   % Je�li tak, to je zsumuj
                    A(i,j-3) = 0;                        % Wyzeruj 1 element z nich
                end
            end
        end
    end
end
for i = 1:4
        nz = find(A(i,:)~=0);                                % Sprawd�, kt�re elementy s� niezerowe (nz)
        if length(nz) ~= 4                                   % Przesu� te wiersze, kt�re maj� zero
            A(i,:) = [zeros(1,4-length(nz)) A(i,nz)];        % Przesu� wszystkie niezerowe elementy w prawo
        end
end
end