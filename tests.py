import main as Chatbot

import random
import string

outputs = []

def random_string_generator(str_size, allowed_chars):
  return ''.join(random.choice(allowed_chars) for x in range(str_size))


def mock_input(*args, **kwargs):
  chars = string.digits
  size = 12
  s = random_string_generator(12, chars)
  outputs.append(s)
  return s


def mock_same_input(*args, **kwargs):
  if len(outputs) < 1:
    chars = string.digits
    size = 12
    s = random_string_generator(12, chars)
    outputs.append(s)
  return outputs[0]


def check_ifs():
  """Counts all if/elif/else statements and returns whether or not there are at least two of each."""
  if_count = 0
  elif_count = 0
  else_count = 0
  with open('main.py', 'r') as source:  #open the main.py file
    for l in source:
      l = l.replace('\t', '').replace('  ', '')  # remove tabs and double spaces
      if l.startswith('if'):
        if_count += 1
      elif l.startswith('elif'):
        elif_count += 1
      elif l.startswith('else'):
        else_count += 1
  return if_count >= 2 and elif_count >= 2 and else_count >= 2


def test_at_least_5_input_calls(monkeypatch):
  """This test case checks that your program has 5​ input() ​calls."""

  monkeypatch.setattr('builtins.input', mock_input)

  Chatbot.main()
  assert len(outputs) >= 5


def test_2_ifs_2_elifs_and_2_elses():
  """This test case checks that your program has at least 2 if, 2 elif, and 2 else statements."""
  assert check_ifs()


def test_randomness(monkeypatch, capsys):
  """This test case runs your program 1000 times and checks if there are ever any differences with the same input."""
  monkeypatch.setattr('builtins.input', mock_same_input)

  Chatbot.main()
  c1 = capsys.readouterr().out

  Chatbot.main()
  c2 = capsys.readouterr().out
  count = 2
  while c1 == c2 and count < 1000:
    Chatbot.main()
    c2 = capsys.readouterr().out
    count += 1
  assert c1 != c2
