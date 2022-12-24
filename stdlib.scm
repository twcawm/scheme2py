(define cons (lambda (x y) (lambda (m) (m x y ))))
(define car (lambda (z) (z (lambda (p q) p ))) )

