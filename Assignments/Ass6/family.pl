father(dashrath, ram).
father(dashrath, lakshman).
father(dashrath, shatrugan).
father(dashrath, bharat).

father(janak, sita).
father(ram, luv).
father(ram, kush).

husband(dashrath, kaushalya).
husband(dashrath, kaikeyi).
husband(dashrath, sumitra).
husband(janak, sunaina).
husband(ram, sita).
husband(X, Y) :-    father(X, Z), mother(Y, Z).
wife(X, Y) :-       husband(Y, X).

mother(kaushalya, ram).
mother(kaikeyi, bharat).
mother(sumitra, lakshman).
mother(sumitra, shatrugan).
mother(sita, luv).
mother(sita, kush).

brother(ram, bharat).
brother(ram, lakshman).
brother(ram, shatrugan).
brother(X, Y) :- brother(Y, X).
brother(X, Y) :- brother(X, Z), brother(Z, Y).

parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).


chacha(X, Y):-      brother(X, Z), father(Z, Y).
mama(X, Y):-        brother(X, Z), mother(Z, Y).

chachi(X, Y):-      sister(X, Z), father(Z, Y).
mami(X, Y):-        sister(X, Z), mother(Z, Y).

uncle(X, Y) :-      chacha(X, Y).
uncle(X, Y) :-      mama(X, Y).

aunt(X, Y) :-       chachi(X, Y).
aunt(X, Y) :-       mami(X, Y).


grandfather(X, Y):- father(X, Z), father(Z, Y).
grandfather(X, Y):- father(X, Z), mother(Z, Y).

grandmother(X, Y):- mother(X, Z), father(Z, Y).
grandmother(X, Y):- mother(X, Z), mother(Z, Y).

stepgrandmother(X, Y) :- parent(Y, Z), aunt(X, Z).