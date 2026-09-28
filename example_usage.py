from client import PauliAlgebra

comm = PauliAlgebra.commutator(PauliAlgebra.X, PauliAlgebra.Y)
print("Commutator [X, Y]:", comm)
