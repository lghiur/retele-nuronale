def split_rows(txt): 
  if txt == "":
    return []

  rows = txt.split("\n")
  return list(filter(None,map(str.strip, rows)))

def split_by_spaces(row):
  items = row.split(" ");
  return list(filter(None, items))

def to_number(text):
  value = float(text)
  if value.is_integer():
    value = int(value)
  return value

def extract_single_coeficient(elem, identifier, prev):
  number = elem.replace(identifier, "")
  if number in ("", "+"):
    new_elem = 1
  elif number == "-":
    new_elem = -1
  else:
    new_elem = to_number(number)

  if prev == '-':
    new_elem = -1 * new_elem
  return new_elem

def extract_row_coeficients(row):
  raw_row = split_by_spaces(row)
  x = 0
  y = 0
  z = 0
  r = 0

  for k, elem in enumerate(raw_row):
    prev = None
    if k > 0:
      prev = raw_row[k-1]
    if("x" in elem):
      x = extract_single_coeficient(elem, "x", prev)
    if("y" in elem):
      y = extract_single_coeficient(elem, "y", prev)
    if("z" in elem):
      z = extract_single_coeficient(elem, "z", prev)
    if("=" in elem):
      r = to_number(raw_row[k+1])
  return [x, y, z], r

def extract_coeficients(txt):
  A = []
  B = []
  rows = split_rows(txt)

  for row in rows:
    temp_a, temp_b = extract_row_coeficients(row)
    A.append(temp_a)
    B.append(temp_b)

  return A, B