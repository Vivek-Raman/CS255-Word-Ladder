import word_ladder

if __name__ == '__main__':
  inputs = [
    ('could', 'world'),
  ]

  for inp in inputs:
    path = word_ladder.wordLadder(inp[0], inp[1])
    print(inp[0], '-->', inp[1], '-', len(path), 'steps')
    for step in path:
      print('  -', step);
