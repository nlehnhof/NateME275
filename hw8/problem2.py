import numpy as np

Pv = 0.15
Pw = 0.05
Pvorw = 0.17

Pand = Pv + Pw - Pvorw
print("P(v and w):", Pand)

Pnone = 1 - Pvorw
print("P(neither v nor w):", Pnone)

Pv_not_w = Pv - Pand
print("P(v and not w):", Pv_not_w)

# P(v and w): 0.03
# P(neither v nor w): 0.83
# P(v and not w): 0.12
