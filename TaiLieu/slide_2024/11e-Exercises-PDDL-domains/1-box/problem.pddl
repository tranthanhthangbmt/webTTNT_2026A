(define (problem box-1)
(:domain box)
(:objects )
(:init
    (not (robotCloseToBox))
    (boxClosed)
    (objInsideBox)
)
(:goal
    (not (objInsideBox))
)
)
