function A = down(A)

for i = 4:-1:2
    for j = 1:4
        if A(i,j) == A(i-1,j) & A(i-1,j) ~= 0            % SprawdŸ, czy 2 s¹siednie niezerowe elementy s¹ takie same
            A(i,j) = 2*A(i,j);                           % Jeœli tak, to je zsumuj
            A(i-1,j) = 0;                                % Wyzeruj 1 element z nich
        elseif A(i-1,j) == 0 & i > 2                     % W innym przypadku, gdy miêdzy elementami jest 0:
            if A(i,j) == A(i-2,j) & A(i-2,j) ~= 0        % SprawdŸ, czy niezerowe elementy po obu stronach 0 s¹ takie same
            A(i,j) = 2*A(i,j);                           % Jeœli tak, to je zsumuj
            A(i-2,j) = 0;                                % Wyzeruj 1 element z nich
            elseif A(i-2,j) == 0 & i == 4                % W innym przypadku, jeœli pomiêdzy elementami s¹ 2 zera:
                if A(i,j) == A(i-3,j) & A(i-3,j) ~= 0    % SprawdŸ, czy te niezerowe elementy s¹ takie same
                    A(i,j) = 2*A(i,j);                   % Jeœli tak, to je zsumuj
                    A(i-3,j) = 0;                        % Wyzeruj 1 element z nich
                end
            end
        end
    end
end
for i = 1:4
        nz = find(A(:,i)~=0);                                % SprawdŸ, które elementy s¹ niezerowe (nz)
        if length(nz) ~= 4                                   % Przesuñ te wiersze, które maj¹ zero
            A(:,i) = vertcat(zeros(4-length(nz),1), A(nz,i));% Przesuñ wszystkie niezerowe elementy w dó³
        end
    end
end