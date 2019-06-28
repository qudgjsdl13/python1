import telegram

chil_token="123456789:ABCDEFGHIJKLMNOPQRST"
chil=telegram.Bot(token=chil_token)
updates=chil.getupdates()

for u in updates:
    print(u.message)