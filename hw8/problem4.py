pflaw = 0.0002

pfailifyes = 0.995
ppassifno = 0.99

#          Flaw             No Flaw
 
# pass      0.005*0.002    0.99*0.9998 

# fail      0.995*0.002     0.01*0.9998
#     

pflawgivenfail = 0.995 * 0.0002 / (0.995 * 0.0002 + 0.01 * 0.9998)

pnoflawgivenpass = 0.99 * 0.9998 / (0.005 * 0.0002 + 0.99 * 0.9998)

print("P(flaw | fail):", pflawgivenfail)
print("P(no flaw | pass):", pnoflawgivenpass)

# P(flaw | fail): 0.01951554378738845
# P(no flaw | pass): 0.99999898969795

"""
In quality control, the key goal is to never ship a defective product.
If the test occasionally rejects good bottles (false fails), it’s inefficient but safe — those bottles can be re-inspected or recycled.
What would be dangerous is passing flawed bottles, but since 
𝑃(no flaw ∣ pass) is extremely high, the test almost never lets a bad one through.
"""