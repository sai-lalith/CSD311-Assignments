 last([X]):-
        write("\nLast element is : "),
        write(X).
        
    last([Y|Tail]):-
        last(Tail).
%last([a,b,c,d,e]).