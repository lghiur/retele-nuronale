from math import sqrt

def remove_item_at_index(vector, i):
  return vector[0:i] + vector[i+1:]

def minor(matrix, i, j):
  no_i = remove_item_at_index(matrix, i)
  no_j = []

  for _, row in enumerate(no_i):
    no_j.append(remove_item_at_index(row, j))

  return no_j
  

def validate_matrix(matrix):
  if len(matrix) == 0:
    raise ValueError("matrix must not be empty")
  
  if any(len(row) != len(matrix) for row in matrix):
    raise ValueError("matrix must be square")

def determinant(matrix): 
  det = 0

  validate_matrix(matrix)

  if len(matrix) == 1:
    return matrix[0][0]

  if len(matrix) == 2:
    return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

  for j, val in enumerate(matrix[0]):
    det += (-1) ** (0+j) * val * determinant(minor(matrix, 0, j))

  return det

def trace(matrix):
  validate_matrix(matrix)

  trace_val = 0

  for i, row in enumerate(matrix):
      trace_val += row[i]

  return trace_val

def norm(vector):
  square = 0;
  for _, val in enumerate(vector):
    square += val ** 2

  return sqrt(square)

def transpose(matrix):
  if len(matrix[0]) != len(matrix):
      raise ValueError("use a square matrix")

  nr_rows = len(matrix);
  nr_cols = len(matrix[0])

  new_matrix = []

  for _ in range(nr_cols):
    new_matrix.append([0] * nr_rows)

  for i, row in enumerate(matrix):
    for j, val in enumerate(row):
      new_matrix[j][i] = val

  return new_matrix

def multiply(matrix, vector):
  if len(matrix[0]) != len(vector):
    raise ValueError("number of matrix columns must match vector length")

  result = [0] * len(matrix)

  for i, row in enumerate(matrix):
    for j, val in enumerate(row):
      result[i] += vector[j] * val;

  return result

def sign(i, j):
  if (i+j) % 2 == 0:
    return 1
  else: 
    return -1

def elem_cofactor(matrix, i, j):
  new_matrix = minor(matrix, i, j)
  det = determinant(new_matrix)
  sgn = sign(i, j)

  return sgn * det

def cofactor(matrix):
  clone = [row[:] for row in matrix]
  for i, row in enumerate(matrix):
    for j, _ in enumerate(row):
      clone[i][j] = elem_cofactor(matrix, i, j)

  return clone

def adjoint(matrix):
  return transpose(cofactor(matrix))

def inverse(matrix):
  det = determinant(matrix)
  if det == 0:
    raise ValueError("det of matrix is 0")
  
  inverse = [row[:] for row in matrix]
  adj_matrix = adjoint(matrix)

  for i, row in enumerate(adj_matrix):
    for j, val in enumerate(row):
      inverse[i][j] = (1/det) * val

  return inverse

def solve(matrix, vector):
  return multiply(inverse(matrix), vector)