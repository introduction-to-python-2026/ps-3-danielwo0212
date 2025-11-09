def approximate_pi(n_terms):
  l = []
  for n in range(n_terms):
    l.append(((-1)**n)/(2*n+1))
  π = 4 * sum(l)
  return π
