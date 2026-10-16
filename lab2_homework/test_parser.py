from parser import split_rows, split_by_spaces, extract_row_coeficients, extract_coeficients

def test_split_empty_string():
    text = ""
    rows = split_rows(text);
    assert len(rows) == 0

    text = """2x + 3y - z = 5
x - y + 4z = 6
3x + y + 2z = 7"""
    rows = split_rows(text);
    assert len(rows) == 3

    text = """2x + 3y - z = 5

x - y + 4z = 6

3x + y + 2z = 7


"""
    rows = split_rows(text);
    assert len(rows) == 3

def test_trim_rows():
    text = """   2x + 3y - z = 5   
    x - y + 4z = 6   
    3x + y + 2z = 7  """
    rows = split_rows(text);
    assert rows[0] == "2x + 3y - z = 5"
    assert rows[1] == "x - y + 4z = 6"
    assert rows[2] == "3x + y + 2z = 7"

def test_split_by_spaces():
    text = "2x + 3y - z = 5"
    split_text = split_by_spaces(text);
    assert split_text == ["2x", "+", "3y", "-", "z", "=", "5"]

def test_extract_row_coeficients():
    text = "2x + 3y - z = 5"
    A, B = extract_row_coeficients(text)
    assert A == [2, 3, -1]
    assert B == 5

    text = "-2x + 3y - z = 5"
    A, B = extract_row_coeficients(text)
    assert A == [-2, 3, -1]
    assert B == 5

    text = "3y - z = 5"
    A, B = extract_row_coeficients(text)
    assert A == [0, 3, -1]
    assert B == 5

    text = "3x - z = 5"
    A, B = extract_row_coeficients(text)
    assert A == [3, 0, -1]
    assert B == 5

    text = "3x = 5"
    A, B = extract_row_coeficients(text)
    assert A == [3, 0, 0]
    assert B == 5

    text = "- 3x = 5"
    A, B = extract_row_coeficients(text)
    assert A == [-3, 0, 0]
    assert B == 5

def test_extract_coeficients():
    text = """2x + 3y - z = 5
    x - y + 4z = 6
    3x + y + 2z = 7"""

    A, B = extract_coeficients(text)
    assert A == [[2, 3, -1], [1, -1, 4], [3, 1, 2]]
    assert B == [5, 6, 7]


    text = """3y - z = 5
    x - y + 4z = 6
    3x + y + 2z = 7"""

    A, B = extract_coeficients(text)
    assert A == [[0, 3, -1], [1, -1, 4], [3, 1, 2]]
    assert B == [5, 6, 7]