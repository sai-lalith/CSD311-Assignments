element_at(H, [H | _], 1).
element_at(H, [_ | T], N) :- element_at(H, T, NMinus1), N is NMinus1 + 1.
%element_at(7,[1,2,3,4,5,6,7,8],X).