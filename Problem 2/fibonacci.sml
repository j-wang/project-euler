(* fibonacci.sml
   Written by James Wang
   Problem Euler Problem 2 *)

(* By considering the terms in the Fibonacci sequence whose values do *)
(* not exceed four million, find the sum of the even-valued terms. *)


(* n corresp with fib seq #, n = 4 being 2, n = 5 being 5 *)
fun fib n =
    Real.round(Math.pow((1.0+Math.sqrt(5.0))/2.0, Real.fromInt(n))
	       /((1.0+Math.sqrt(5.0))/2.0 + 2.0))
 
fun genEvenFib (start, last, acc) =
    let val n = fib start
    in if n >= last then acc else genEvenFib(start + 3, last, acc + n)
    end

val ans = genEvenFib (4, 4000000, 0)
