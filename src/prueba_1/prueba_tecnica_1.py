import json,pandas as pd
import time
import math
import numpy as np
from websocket import create_connection

def get_json() -> list[dict]:
  ws = create_connection("ws://209.126.82.146:8080")
  list_res = []
  init = time.time()
  while len(list_res)< 60000:
    list_res.append(json.loads(ws.recv()))
  print(f"\n\tSe demoró {round((time.time() - init)/60,1)} segundos")
  ws.close()
  return list_res

@np.vectorize
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

while True:
  df =pd.DataFrame(get_json())
  print(json.dumps({
  "_max_number":int(df["b"].max()),
  "min_number":int(df["b"].min()),
  "first_number": int(df["b"][0]),
  "last_number":int(df["b"][len(df)-1]),
  "number_of_prime_numbers": int(df[is_prime(df["b"])]["b"].count()),
  "number_of_even_numbers": int(df[df["b"] % 2 == 0]["b"].count()),
  "number_of_odd_numbers": int(df[df["b"] % 2 != 0]["b"].count())
      },indent=3))