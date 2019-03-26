function A = left(A)
% left
for i = 1:4
    for j = 1:4-1
        if A(i,j) == A(i,j+1) & A(i,j+1) ~= 0            % Sprawd�, czy 2 s�siednie niezerowe elementy s� takie same
            A(i,j) = 2*A(i,j);                           % Je�li tak, to je zsumuj
            A(i,j+1) = 0;                                % Wyzeruj 1 element z nich
        elseif A(i,j+1) == 0 & j < 3                     % W innym przypadku, gdy mi�dzy elementami jest 0:
            if A(i,j) == A(i,j+2) & A(i,j+2) ~= 0        % Sprawd�, czy niezerowe elementy po obu stronach 0 s� takie same
            A(i,j) = 2*A(i,j);                           % Je�li tak, to je zsumuj
            A(i,j+2) = 0;                                % Wyzeruj 1 element z nich
            elseif A(i,j+2) == 0 & j == 1                % W innym przypadku, je�li pomi�dzy elementami s� 2 zera:
                if A(i,j) == A(i,j+3) & A(i,j+3) ~= 0    % Sprawd�, czy te niezerowe elementy s� takie same
                    A(i,j) = 2*A(i,j);                   % Wyzeruj 1 element z nich
                    A(i,j+3) = 0;
                end
            end
        end
    end
end
for i = 1:4
        nz = find(A(i,:)~=0);                                % Sprawd�, kt�re elementy s� niezerowe (nz)
        if length(nz) ~= 4                                   % Przesu� te wiersze, kt�re maj� zero
            A(i,:) = [A(i,nz) zeros(1,4-length(nz))];        % Przesu� wszystkie niezerowe elementy w lewo
        end
end
end