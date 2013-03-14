#lang racket

;; multiples3and5.rkt
;; Written by James Wang
;; Project Euler Problem 1

;; Find the sum of all the multiples of 3 or 5 below 1000

(define (ans x y acc)
  (if (>= x y)
      acc
      (if (or (= (remainder x 3) 0) (= (remainder x 5) 0))
          (ans (+ x 1) y (+ acc x))
          (ans (+ x 1) y acc))))
 
(write (ans 3 1000 0))