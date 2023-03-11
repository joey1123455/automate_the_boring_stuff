#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {
    'email': 'foddd@gmail.com',
    'blog': 'WerGTHYdfeTGNBMesD',
    'luggage': '12345'
}

import sys, pyperclip
if len(sys.argv) < 2:
    print('usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'password for {account} copied to clipboard')
else:
    print(f'there is no account named {account}')