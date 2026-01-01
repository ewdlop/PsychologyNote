;;; Pyramid Scheme - A Scheme Language Demonstration
;;; This file demonstrates pyramid/hierarchical structures using Scheme

;; Define a person in the pyramid scheme with name and recruits
(define (make-person name)
  (list name '()))

(define (person-name person)
  (car person))

(define (person-recruits person)
  (cadr person))

;; Add a recruit to a person
(define (add-recruit person recruit)
  (list (person-name person)
        (cons recruit (person-recruits person))))

;; Calculate the total number of people in a pyramid
(define (pyramid-size person)
  (if (null? (person-recruits person))
      1
      (+ 1 (apply + (map pyramid-size (person-recruits person))))))

;; Calculate the depth/level of the pyramid
(define (pyramid-depth person)
  (if (null? (person-recruits person))
      1
      (+ 1 (apply max (map pyramid-depth (person-recruits person))))))

;; Count people at a specific level
(define (count-at-level person level)
  (cond
    ((= level 1) 1)
    ((null? (person-recruits person)) 0)
    (else (apply + (map (lambda (recruit)
                          (count-at-level recruit (- level 1)))
                        (person-recruits person))))))

;; Calculate total money flow (demonstrating the scheme)
;; Each person pays $100 upward, receives $100 from each recruit
(define (calculate-profit person)
  (let ((recruit-count (length (person-recruits person))))
    (- (* recruit-count 100) 100)))

;; Display pyramid structure
(define (display-pyramid person indent)
  (display (make-string indent #\space))
  (display (person-name person))
  (newline)
  (for-each (lambda (recruit)
              (display-pyramid recruit (+ indent 2)))
            (person-recruits person)))

;; Example: Build a pyramid scheme structure
(define (build-example-pyramid)
  (let* ((level3-1 (make-person "Alice"))
         (level3-2 (make-person "Bob"))
         (level3-3 (make-person "Carol"))
         (level3-4 (make-person "Dave"))
         (level3-5 (make-person "Eve"))
         (level3-6 (make-person "Frank"))
         
         (level2-1 (add-recruit (make-person "George") level3-1))
         (level2-1 (add-recruit level2-1 level3-2))
         (level2-2 (add-recruit (make-person "Helen") level3-3))
         (level2-2 (add-recruit level2-2 level3-4))
         (level2-3 (add-recruit (make-person "Ivan") level3-5))
         (level2-3 (add-recruit level2-3 level3-6))
         
         (level1 (add-recruit (make-person "Top") level2-1))
         (level1 (add-recruit level1 level2-2))
         (level1 (add-recruit level1 level2-3)))
    level1))

;; Demonstrate mathematical impossibility of pyramid schemes
(define (demonstrate-impossibility initial-people levels)
  (define (people-needed-at-level level branching-factor)
    (expt branching-factor level))
  
  (define (total-people-needed levels branching-factor)
    (let loop ((level 0) (total 0))
      (if (>= level levels)
          total
          (loop (+ level 1) 
                (+ total (people-needed-at-level level branching-factor))))))
  
  (let ((total (total-people-needed levels 3)))
    (display "Pyramid Scheme Mathematics:\n")
    (display (string-append "Levels: " (number->string levels) "\n"))
    (display (string-append "Branching factor: 3 recruits per person\n"))
    (display (string-append "Total people needed: " (number->string total) "\n"))
    (display (string-append "World population (~8 billion): 8000000000\n"))
    (if (> total 8000000000)
        (display "IMPOSSIBLE: Not enough people on Earth!\n")
        (display "Possible, but ethically wrong and mathematically unsustainable.\n"))))

;; Main demonstration
(define (run-pyramid-demo)
  (display "=== Pyramid Scheme Demonstration in Scheme ===\n\n")
  
  (display "Building example pyramid...\n")
  (define pyramid (build-example-pyramid))
  
  (display "\nPyramid Structure:\n")
  (display-pyramid pyramid 0)
  
  (display "\nPyramid Statistics:\n")
  (display (string-append "Total people: " (number->string (pyramid-size pyramid)) "\n"))
  (display (string-append "Pyramid depth: " (number->string (pyramid-depth pyramid)) "\n"))
  
  (display "\nPeople at each level:\n")
  (display (string-append "Level 1: " (number->string (count-at-level pyramid 1)) "\n"))
  (display (string-append "Level 2: " (number->string (count-at-level pyramid 2)) "\n"))
  (display (string-append "Level 3: " (number->string (count-at-level pyramid 3)) "\n"))
  
  (display "\n")
  (demonstrate-impossibility 1 15)
  
  (display "\n=== End of Demonstration ===\n"))

;; Uncomment to run the demonstration
;; (run-pyramid-demo)
