father(dashrath, ram).
father(janak, sita).
father(ram, luv).
father(ram, kush).

husband(ram, sita).

mother(sita, luv).
mother(sita, kush).

grandfather(X, Y):- father(X, Z), father(Z, Y).
grandfather(X, Y):- father(X, Z), mother(Z, Y).

grandmother(X, Y):- mother(X, Z), father(Z, Y).
grandmother(X, Y):- mother(X, Z), mother(Z, Y).

husband(X, Y) :-    father(X, Z), mother(Y, Z).
wife(X, Y) :-       father(X, Z), mother(Y, Z).
# husband(X, Y) :-    wife(Y, X)

# spouse(X, Y) :-     husband(X, Y).
# spouse(X, Y) :-     wife(X, Y).

chacha(X, Y):-      brother(X, Z), father(Z, Y).
mama(X, Y):-        brother(X, Z), mother(Z, Y).

