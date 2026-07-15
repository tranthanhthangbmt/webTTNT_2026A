(define (domain logistics)
  (:requirements :strips :negative-preconditions :universal-preconditions :conditional-effects :typing) 
  (:types
      pack vehicle - object
      truck - vehicle
      loc
  )
  (:predicates 	
    (connected ?l1 ?l2 - loc)  ;; nonfluent - does not appear in effects of actions
		(at ?p - object ?l - loc) ;; fluent
		(on ?p - pack ?t - truck)  ;; fluent
)
  
(:action drive
  :parameters (?t - truck ?from ?to - loc)
  :precondition (and (at ?t ?from) (connected ?from ?to))
  :effect (and (at ?t ?to)  (not (at ?t ?from)))
)

(:action load
  :parameters (?p - pack ?t - truck)
  :precondition (exists (?l - loc) (and (at ?t ?l) (at ?p ?l)))
  :effect (and 
            (on ?p ?t)
            (forall (?l - loc) (not (at ?p ?l)))
      ) 
)


(:action unload
  :parameters (?t - truck)
  :precondition (exists (?p - pack) (on ?p ?t))
  :effect (and 
            (forall(?l - loc ?p - pack) (when (and (on ?p ?t) (at ?t ?l)) (at ?p ?l)))
            (forall(?p - pack) (when (on ?p ?t) (not (on ?p ?t))))    
      )
)

)
