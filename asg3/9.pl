fib(0, [1]).
fib(1, [1, 1]).

fib(N, L) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fib(N1, F1),
    last(F1, L1),
    fib(N2, F2),
    last(F2, L2),
    L_new is L1 + L2,
    append(F1, [L_new], L).  
    sum_list([],0).
 
   sum_list([Head|Tail], Total):-
   sum_list(Tail, Sum1),
   Total is Head+Sum1.
%fib(6,L), sum_list(L,Total).