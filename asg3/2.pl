slow_max(L, Max) :-
   select(Max, L, Rest), \+ (member(E, Rest), E > Max).
 %slow_max([1,2,3,4,5,6,10,7,8],X).