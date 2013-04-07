;; multiple3and5.clj
;; Written by James Wang
;; Project Euler Problem 1

;; Find the sum of all the multiples of 3 or 5 below 1000

(defn ans [x y acc]
  (if (>= x y)
    acc
    (if (or (= (mod x 3) 0) (= (mod x 5) 0))
      (ans (+ x 1) y (+ acc x))
      (ans (+ x 1) y acc))))

(println (ans 3 1000 0))
