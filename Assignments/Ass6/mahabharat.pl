male(dashrath).
male(ram).
male(lakshman).
male(shatrugan).
male(bharat).
male(janak).

female(kaushalya).
female(kaikeyi).
female(sumitra).
female(sita).
female(sunaina).

parent(dashrath, ram).
parent(dashrath, bharat).
parent(dashrath, lakshman).
parent(dashrath, shatrugan).

parent(kaushalya, ram).
parent(kaikeyi, bharat).
parent(sumitra, lakshman).
parent(sumitra, shatrugan).

parent(ram, luv).
parent(ram, kush).
parent(sita, luv).
parent(sita, kush).

father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).

husband(X, Y) :- male(X), parent(X, Z), parent(Y, Z).
wife(X, Y) :- husband(Y, X).

stepmother(X, Y) :- female(X), father(Z, Y), husband(Z, X).
    /*, not(parent(X, Y)).*/

sibling(ram, bharat).
sibling(ram, lakshman).
sibling(ram, shatrugan).
sibling(X, Y) :- sibling(Y, X).

brother(X, Y) :- male(X), sibling(X, Y).
brotherinlaw(X, Y) :- male(X), sibling(Y, Z), husband(X, Z).
sisterinlaw(X, Y) :- female(X), sibling(Y, Z), husband(X, Z).

grandfather(X, Y):- father(X, Z), father(Z, Y).
grandfather(X, Y):- father(X, Z), mother(Z, Y).

grandmother(X, Y):- mother(X, Z), father(Z, Y).
grandmother(X, Y):- mother(X, Z), mother(Z, Y).

/*stepgrandmother(X, Y) :- parent(Y, Z), aunt(X, Z).*/