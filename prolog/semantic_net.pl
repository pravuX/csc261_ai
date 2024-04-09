%% Semantic Net
%
isa(mat1, mat).
isa(cat1, cat).
isa(tom, cat).
isa(bird1, bird).
isa(cat, mammal).
isa(bird, animal).
isa(mammal, animal).

sat(cat1, mat1).
sat(cat, mat).
caught(tom, bird1).

hasa(tom, owner(john)).
hasa(tom, color(ginger)).
hasa(cat, like(cream)).
hasa(mammal, fur).
