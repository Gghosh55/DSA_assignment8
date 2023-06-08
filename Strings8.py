def made_equal(s, goal):

  if len(s) != len(goal):
    return False

  for i in range(len(s)):
    for j in range(i + 1, len(s)):
      if s[i] == goal[j] and s[j] == goal[i]:
        return True

  return False

s = "ab"
goal = "ba"

print(made_equal(s, goal))
