%% Ancestor program
%

female(sita).
female(rita).
female(nita).
female(muna).
female(juna).
female(luna).

male(ram).
male(sam).
male(hari).
male(ravi).

parent(sita, sam).
parent(sita, muna).
parent(rita, sam).
parent(rita, muna).

parent(nita, hari).
parent(nita, juna).
parent(ram, hari).
parent(ram, juna).

parent(hari, ravi).
parent(hari, luna).
parent(sam, ravi).
parent(sam, luna).

father(Child, Parent) :-
  parent(Child, Parent), male(Parent).
mother(Child, Parent) :-
  parent(Child, Parent), female(Parent).

grandparent(Child, GP) :-
  parent(Child, Parent), parent(Parent, GP).

grandfather(Child, GP) :-
  grandparent(Child, GP), male(GP).

grandmother(Child, GP) :-
  grandparent(Child, GP), female(GP).

ancestor(Child, Ancestor) :-
  parent(Child, Ancestor).
ancestor(Child, Ancestor) :-
  parent(Child, Parent), ancestor(Parent, Ancestor).

sibling(Child, Sibling) :-
  mother(Child, Parent), mother(Sibling, Parent), Child \= Sibling.

sister(Child, Sibling) :-
  sibling(Child, Sibling), female(Sibling).

brother(Child, Sibling) :-
  sibling(Child, Sibling), male(Sibling).

cousin(Child, Cousin) :-
  grandmother(Child, GM), grandmother(Cousin, GM),
  Child \= Cousin, \+sibling(Child, Cousin).
