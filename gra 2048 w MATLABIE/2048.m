A = startMatrix();
rysuj(A);
[~,~,button]=ginput(1);
while waitforbuttonpress
    value = double(get(gcf,'CurrentCharacter'));
              if value == 28 %leftarrow
                    A = left(A)
                    rysuj(A)
                    A = dodaj_element(A)
                    rysuj(A)  
              elseif value == 29 %rightarrow
                    A = right(A)
                    rysuj(A)
                    A = dodaj_element(A)
                    rysuj(A)
              elseif value == 30 %uparrow
                    A = up(A)
                    rysuj(A)
                    A = dodaj_element(A)
                    rysuj(A)
              elseif value == 31 %downarrow
                    A = down(A)
                    rysuj(A)
                    A = dodaj_element(A)
                    rysuj(A)
              end
end