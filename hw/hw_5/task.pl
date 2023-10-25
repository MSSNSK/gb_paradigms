arr([], 0).
arr([H|T], N) :- arr(T, N1), N is N1+H.

?-arr([1,2,3,4,5,6,7,8,9,10], N), write(N).

