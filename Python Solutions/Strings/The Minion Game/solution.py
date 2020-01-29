# Original problem: https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(s):
    s_score = 0
    k_score = 0
    vowels = "AEIOU"
 
    for i in range(len(s)):
        if s[i] in vowels:
            k_score += len(s)-i
        else:
            s_score += len(s)-i
 
    if k_score == s_score:
        print ("Draw")
    elif k_score > s_score:
        print("Kevin "+ str(k_score))
    else:
        print("Stuart "+ str(s_score))

if __name__ == '__main__':
    s = input()
    minion_game(s)