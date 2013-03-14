#lang racket
(require math/base)

;; fibonacci.rkt
;; Written by James Wang
;; Project Euler Problem 2

;; By considering the terms in the Fibonacci sequence whose values 
;; do not exceed four million, find the sum of the even-valued terms.


;; Stream that generates even fibonacci sequence
(define even-fib
  (letrec ([fib-calc (lambda (x) (round (/ (expt phi.0 x) (+ phi.0 2))))]
           [fib-thunk (lambda (x) (cons (fib-calc x)
                                      (lambda () (fib-thunk (+ x 3)))))])
    (lambda() (fib-thunk 4))))

;; Sums stream until stream output is equal to or greater than max
(define (sst stream max acc)
  (let* ([pr (stream)]
         [curr (car pr)]
         [next (cdr pr)])
    (if (>= (car pr) max) acc (sst next max (+ acc curr)))))
 
;; Answer
(write (sst even-fib 4000000 0))