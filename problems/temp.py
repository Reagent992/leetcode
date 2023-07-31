d = dict(pair.split('=') for pair in input().split())
for key in ('False', '3'):
    d.pop(key, 'Да не очень то и надо')
print(*sorted(d.items()))