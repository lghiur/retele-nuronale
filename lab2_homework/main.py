from pathlib import Path
from parser import extract_coeficients
from matrix_vector_operations import determinant, trace, norm, transpose, multiply, solve
from cramer import solve_cramer

def load_system(path: Path):
  text = path.read_text()
  return extract_coeficients(text)

A, B = load_system(Path(__file__).parent / "input.txt")

print(f"{A=} {B=}")
print(f"{determinant(A)=}")
print(f"{trace(A)=}")
print(f"{norm(B)=}")
print(f"{transpose(A)=}")
print(f"{multiply(A, B)=}")
print(f"{solve_cramer(A, B)=}")
print(f"{solve(A, B)=}")