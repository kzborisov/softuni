# Task 02. Next Version

curr_version = list(map(int, input().split(".")))

if curr_version[-1] < 9:
    curr_version[-1] = curr_version[-1] + 1
else:
    curr_version[-1] = 0
    if curr_version[-2] < 9:
        curr_version[-2] = curr_version[-2] + 1
    else:
        curr_version[-2] = 0
        curr_version[-3] = curr_version[-3] + 1

print(*curr_version, sep=".")


# Solution From the Exercise:
curr_version = input().split(".")
curr_version = list(str(int("".join(curr_version)) + 1))
print(*curr_version, sep=".")
