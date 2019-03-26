function A = right(A)
% left
for i = 1:4
    for j = 4:-1:2
        if A(i,j) == A(i,j-1) & A(i,j-1) ~= 0            % SprawdŸ, czy 2 s¹siednie niezerowe elementy s¹ takie same
            A(i,j) = 2*A(i,j);                           % Jeœli tak, to je zsumuj
            A(i,j-1) = 0;                                % Wyzeruj 1 element z nich
        elseif A(i,j-1) == 0 & j > 2                     % W innym przypadku, gdy miêdzy elementami jest 0:
            if A(i,j) == A(i,j-2) & A(i,j-2) ~= 0        % SprawdŸ, czy niezerowe elementy po obu stronach 0 s¹ takie same
            A(i,j) = 2*A(i,j);                           % Jeœli tak, to je zsumuj
            A(i,j-2) = 0;                                % Wyzeruj 1 element z nich
            elseif A(i,j-2) == 0 & j == 4                % W innym przypadku, jeœli pomiêdzy elementami s¹ 2 zera:
                if A(i,j) == A(i,j-3) & A(i,j-3) ~= 0    % SprawdŸ, czy te niezerowe elementy s¹ takie same
                    A(i,j) = 2*A(i,j);                   % Jeœli tak, to je zsumuj
                    A(i,j-3) = 0;                        % Wyzeruj 1 element z nich
                end
            end
        end
    end
end
for i = 1:4
        nz = find(A(i,:)~=0);                                % SprawdŸ, które elementy s¹ niezerowe (nz)
        if length(nz) ~= 4                                   % Przesuñ te wiersze, które maj¹ zero
            A(i,:) = [zeros(1,4-length(nz)) A(i,nz)];        % Przesuñ wszystkie niezerowe elementy w prawo
        end
end
end