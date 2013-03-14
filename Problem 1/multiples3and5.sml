(* multiples3and5.sml
   Written by James Wang
   Project Euler Problem #1 *)

(* Find the sum of all the multiples of 3 or 5 below 1000 *)

fun findAns (x, last, acc) =
    if x = last
    then acc
    else 
	if x mod 3 = 0 orelse x mod 5 = 0
	then findAns (x + 1, last, acc + x)
	else findAns (x + 1, last, acc)

val ans = findAns (3, 1000, 0)

