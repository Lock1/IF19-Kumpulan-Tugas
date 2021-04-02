S = [int(input()) for i in range(int(input()))]

print(0) if not(len(S) - 1) else print([S[0] - S[i] if S[0] > S[i] else S[i] - S[0] for i in range(1,len(S))][0])
