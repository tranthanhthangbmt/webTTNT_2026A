(define (problem logistics-1)
(:domain logistics)
(:objects 
    truck1 - truck
    package1 - pack
    package2 - pack
    package3 - pack
    location1 - loc
    location2 - loc
    location3 - loc
    location4 - loc
)
(:init 
    (at truck1 location1)
    (at package1 location1)
    (at package2 location1)
    (at package3 location1)

    (connected location1 location2)
    (connected location2 location3)
    (connected location3 location4)
    (connected location4 location1)
    (connected location1 location4)
    (connected location2 location4)
)

(:goal 
    (and 
        (at package1 location4)
        (at package2 location4)
        (at package3 location4)
    )
)   
)