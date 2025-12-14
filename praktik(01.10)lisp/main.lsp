; No1
(DEFUN MY_BEGIN(L)
(COND
  ((NULL L) NIL)
  ((NULL (CDR L)) NIL)
  (T (CONS (CAR L) (MY_BEGIN (CDR L))))
)
)

; No2
(DEFUN MY_MEMBER(X L)
(COND
  ((NULL L) NIL)
  ((EQUAL X (CAR L)) T)
  (T (MY_MEMBER X (CDR L)))
)
)

; No3
(DEFUN MY_LEN(L)
(COND
  ((NULL L) 0)
  (T (+ 1 (MY_LEN (CDR L))))
)
)

; No4
(DEFUN MY_LAST(L)
(COND
  ((NULL L) NIL)
  ((NULL (CDR L)) (CAR L))
  (T (MY_LAST (CDR L)))
)
)

; No5
(DEFUN MY_REVERSE(L)
(COND
  ((NULL L) NIL)
  (T (APPEND (MY_REVERSE (CDR L)) (LIST (CAR L))))
)
)

; No6
(DEFUN COUNT_ATOMS(L)
(COND
  ((NULL L) 0)
  ((ATOM (CAR L)) (+ 1 (COUNT_ATOMS (CDR L))))
  (T (COUNT_ATOMS (CDR L)))
)
)

; No7
(DEFUN ONLY_ATOMS(L)
(COND
  ((NULL L) NIL)
  ((ATOM (CAR L)) (CONS (CAR L) (ONLY_ATOMS (CDR L))))
  (T (ONLY_ATOMS (CDR L)))
)
)

; No8
(DEFUN INTO_SORT (X L)
(COND
  ((NULL L) (LIST X))
  ((<= X (CAR L)) (CONS X L))
  (T (CONS (CAR L) (INTO_SORT X (CDR L))))
)
)

; No9
(DEFUN MY_SORT(L)
(COND
  ((NULL L) NIL)
  (T (INTO_SORT (CAR L) (MY_SORT (CDR L))))
)
)

; No10
(DEFUN MY_MERGE (L R)
(COND
  ((NULL L) R)
  ((NULL R) L)
  ((<= (CAR L) (CAR R)) (CONS (CAR L) (MY_MERGE (CDR L) R)))
  (T (CONS (CAR R) (MY_MERGE L (CDR R))))
)
)

; No11
(DEFUN MAX_LIST (L)
(COND
  ((NULL (CDR L)) (CAR L))
  (T (MAX (CAR L) (MAX_LIST (CDR L))))
)
)

; No12
(DEFUN MIN_LIST (L)
(COND
  ((NULL (CDR L)) (CAR L))
  (T (MIN (CAR L) (MIN_LIST (CDR L))))
)
)

; No13
(DEFUN SUM_LIST(L)
(COND
  ((NULL L) 0)
  (T (+ (CAR L) (SUM_LIST (CDR L))))
)
)

; No14
(DEFUN ONION (N)
(COND
  ((= N 0) NIL)
  ((= N 1) (LIST NIL))
  (T (LIST (ONION (- N 1))))
)
)
