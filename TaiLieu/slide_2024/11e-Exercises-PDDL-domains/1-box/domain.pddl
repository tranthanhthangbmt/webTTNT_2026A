(define (domain box)
(:requirements :strips)
(:predicates (boxClosed)
             (robotCloseToBox)
             (objInsideBox)             
)

(:action moveCloseToBox
:parameters ()
:precondition (and (not (robotCloseToBox)))
:effect  (and (robotCloseToBox))
)

(:action openBox
:parameters ()
:precondition (and (robotCloseToBox) (boxClosed))
:effect  (and (not (boxClosed)))
)

(:action extractObject
:parameters ()
:precondition (and (not (boxClosed)) (robotCloseToBox))
:effect  (and (not (objInsideBox)))
)


) 