from threading import Thread
import requests, json
from asyncio import sleep, run
with open("proxies.txt", "r") as f:
  data = f.read().split("\n")
done = []
alf = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
r255 = range(255)
def gen():
  global done
  e = ""
  for _ in range(16):
    e += alf[randint(0, 58)]
  if e in done:
    return gen()
  done.append(e)
  return e
def nitro_gen(*proxi):
  co = gen()
  response = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{co}?with_application=false&with_subscription_plan=true", proxy=json.loads(proxi))
  if response.status_code == 200:
    print(f"Valid discord nitro code : {co}")
    exit()
  print(f"Invalid discord nitro : {co}")
while True:
  for i in data:
    for _ in r255:
      Thread(target=nitro_gen, args=(i)).start()
    run(sleep(1))
