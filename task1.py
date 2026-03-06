good = r"""
 /|
        /\/ |/\
        \  ^   | /\  /\
  (\/\  / ^   /\/  )/^ )
   \  \/^ /\       ^  /
    )^       ^ \     (
   (   ^   ^      ^\  )
    \___\/____/______/
    [________________]
     |              |
     |     //\\     |
     |    <<()>>    |
     |     \\//     |
      \____________/
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
  """

bad=r"""
  _.--,_
   .-'      '-.   [nabis]
  /            \
 '          _.  '
 \      "" /  ~(
  '=,,_ =\__ `  &
        "  "'; \\\
    """
torch_lit= True
if torch_lit:
    outcome= "Flicker: TORCH WORKS"
    print(good)
else:
    outcome= "Doom: MYYYYY TORCHHHH"
    print(bad)
    print(outcome)
