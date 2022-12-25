(car (cdr ( cons 1 (cons 2 3 ) ) ) )
(define a (cons 7 8) )
(define b (cons 1 a) )
(cdr (cdr b ))
(define a (delay (+ 4 5)))
a
(a)
(force a)
