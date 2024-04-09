% Facts about family relationships
parent(alice, bob).
parent(bob, charlie).
parent(alice, david).

% Rule to determine if someone is a grandparent
grandparent(X, Y) :-
    parent(X, Z), % X is the parent of Z
    parent(Z, Y).   % Z is the parent of Y
