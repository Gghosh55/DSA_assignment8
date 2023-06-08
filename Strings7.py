def decode_string(s):
  """Decodes an encoded string.

  Args:
    s: The encoded string.

  Returns:
    The decoded string.
  """

  stack = []
  for c in s:
    if c == '[':
      stack.append(c)
    elif c == ']':
      decoded_string = ''
      while stack and stack[-1] != '[':
        decoded_string = stack.pop() + decoded_string
      stack.pop()
      stack.append(decoded_string * int(stack.pop()))
    else:
      stack.append(c)

  return ''.join(stack)

s = "3[a]2[bc]"

print(decode_string(s))
