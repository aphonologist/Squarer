squarer = {
    ### 0 is the halt state
    ### 1 is the start state

    ### copy the number, leaving a padding 0 ###
    # pick up first 1
    1 : {
        0 : (0, 1, +1),
        1 : (0, 2, +1)
        },
    # carrying 1, seen no 0
    2 : {
        0 : (0, 3, +1),
        1 : (1, 2, +1)
        },
    # carrying 1, seen one 0
    3 : {
        0 : (1, 4, -1),
        1 : (1, 3, +1)
        },
    # dropped off 1, going back
    4 : {
        0 : (0, 5, -1),
        1 : (1, 4, -1)
        },
    # seen one 0
    5 : {
        0 : (1, 7, -1), # seen two 0s in a row, stop copying
        1 : (1, 6, -1)
        },
    # seen one 0
    6 : {
        0 : (1, 1, +1), 
        1 : (1, 6, -1)
        },
    
    ### multiply the two numbers ###
    # find beginning of first number
    7 : {
        0 : (0, 8, +1), 
        1 : (1, 7, -1)
        },
    # pick up first 1
    8 : {
        0 : (0, 8, +1),
        1 : (0, 9, +1)
        },
    # carrying 1, seen no 0
    9 : {
        0 : (0, 10, +1),
        1 : (1, 9, +1)
        },
    # carrying 1
    10 : {
        0 : (0, 10, +1),
        1 : (0, 11, +1)
        },
    # carrying 11
    11 : {
        0 : (0, 12, +1),
        1 : (1, 11, +1)
        },
    # carrying 11, seen one 0
    12 : {
        0 : (1, 13, -1),
        1 : (1, 12, +1)
        },
    # carrying 1, going back
    13 : {
        0 : (0, 14, -1), 
        1 : (1, 13, -1)
        },
    # carrying 1, going back
    14 : {
        0 : (1, 16, -1), # two 0s in a row
        1 : (1, 15, -1)
        },
    # carrying 1, going back
    15 : {
        0 : (1, 10, +1),
        1 : (1, 15, -1)
        },
    # carrying 1, going back to first number
    16 : {
        0 : (0, 17, -1),
        1 : (1, 16, -1)
        },
    # carrying 1, going back to first number, seen one 0
    17 : {
        0 : (0, 19, -1), # two 0s in a row
        1 : (1, 18, -1)
        },
    # carrying 1, going back to first number, seen one 0
    18 : {
        0 : (0, 8, -1),
        1 : (1, 18, -1)
        },
    # delete remaining second number
    19 : {
        0 : (0, 19, +1),
        1 : (0, 20, +1)
        },
    # delete remaining second number
    20 : {
        0 : (0, 0, +1),
        1 : (0, 20, +1)
        }
}

q = 1
p = 0
i = 2 # set the number to store on the tape
tape = [1] * i
w = 2*i + 4 + i**2
if i < 10: print(tape)
while q in squarer:
  if i < 10:
    out = [' ' for x in tape]
    out[p] = 'q'
    t = ''.join([str(x) for x in out])
    b = ''.join([str(x) for x in tape])
    print('\t', '{:^{width}}'.format(t, width=w), '\t', q)
    print('\t', '{:^{width}}'.format(b, width=w))
  new = squarer[q][tape[p]]
  tape[p] = new[0]
  q = new[1]
  p += new[2]
  if p == len(tape):
    tape += [0]
  if p == -1:
    tape = [0] + tape
    p += 1
if i < 10:
  out = [' ' for x in tape]
  out[p] = 'q'
  t = ''.join([str(x) for x in out])
  b = ''.join([str(x) for x in tape])
  print('\t', '{:^{width}}'.format(t, width=w), '\t', q)
  print('\t', '{:^{width}}'.format(b, width=w))
  print(tape)
print('{}^2 = {}'.format(i, sum(tape)))
