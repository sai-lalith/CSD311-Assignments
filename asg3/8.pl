split([], [], []).
split([Head|Tail], [Head|List1], List2) :- Head>=0, split(Tail, List1, List2).
split([Head|Tail], List1, [Head|List2]) :- Head<0, split(Tail, List1, List2).
sum_list([],0).

sum_list([Head|Tail], Total):-
sum_list(Tail, Sum1),
Total is Head+Sum1.
%split([1,-2,3,5,-7],Pos,Neg),sum_list(Pos,Pos_Sum),sum_list(Neg,Neg_Sum).