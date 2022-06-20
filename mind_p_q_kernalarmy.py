# all prime factors
x = [1461849912200000206276283741896701133693, 431899300006243611356963607089521499045809]

# n
n = 631371953793368771804570727896887140714495090919073481680274581226742748040342637

# e
e = 65537

# cipher text
ct = 421345306292040663864066688931456845278496274597031632020995583473619804626233684

# start value for phi(n)
i = 1

# loop through prime factors and multiply them togther with (factor-1)*(nextFactor-1)...
for a in x:
    i = i * (a-1)

# inverse pow (3.8+ syntax, for previous versions of python use gympy.invert)
d = pow(e, -1, i)

# solve for the answer
ans = pow(ct, d, n)

# print the answer
print(bytes.fromhex(hex(ans)[2:]).decode('ascii'))
