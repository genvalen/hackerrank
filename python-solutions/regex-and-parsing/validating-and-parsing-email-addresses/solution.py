# Original problem: https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
if __name__ == '__main__':
    import re
    import email.utils

    email_pattern = r'^[a-zA-Z][\w.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

    for _ in range(int(input())):
        user, addr = input().split(" ")
        n_addr = addr.lstrip("<").rstrip(">")
        if re.search(email_pattern, n_addr):
            print(email.utils.formataddr((user, n_addr)))
