from matrix_vector_operations import determinant

def replace_column_with_vector(matrix, vector, pos):
  if len(matrix) != len(vector):
    raise ValueError("nr of columns needs to equal nr of elems in vector")

  clone = [row[:] for row in matrix]

  for i, _ in enumerate(matrix):
    clone[i][pos] = vector[i]

  return clone


def solve_cramer(matrix, vector):
  det_x = determinant(matrix)
  if det_x == 0:
    raise ValueError("system has no unique solution")

  cramer_result = [0] * len(vector)
  
  for i in range(len(vector)):
    new_matrix = replace_column_with_vector(matrix, vector, i)
    cramer_result[i] = determinant(new_matrix) / det_x

  return cramer_result