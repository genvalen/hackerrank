# Original problem: https://www.hackerrank.com/challenges/validating-uid/problem
if __name__ == '__main__':
    import re

    t = int(input())

    for i in range(t):
        uid = "".join(sorted(input()))

        try:
            assert uid.isalnum()
            assert len(uid) == len(set(uid))
            assert re.search(r'[A-Z]{2}', uid)
            assert re.search(r'\d{3}', uid)
            print("Valid")

        except:
            print("Invalid")
            