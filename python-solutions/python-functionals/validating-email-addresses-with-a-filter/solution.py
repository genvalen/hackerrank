# Original problem: https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
import re 

def fun(s):
    """Return true if s matches email pattern, else return False."""
    email_pattern = r'^[\w-]+@[a-zA-Z0-9]+\.[a-zA-Z]{,3}$'
    match = re.match(email_pattern, s)
    return match

def filter_mail(emails):
    """Filter emails to return only the emails macthing email pattern."""
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
