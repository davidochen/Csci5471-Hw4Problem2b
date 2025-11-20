#!/usr/bin/env python3
"""
CSCI 5471 Homework 4 Problem 2b
INSTRUCTIONS : run 'python3 hw4_problem2b.py' in terminal

used baby-step giant-step algorithm for log(7) n mod p
where n = "CHEN7790"
"""
import hashlib
import math

def baby_step_giant_step_textbook(g, h, p):
  q = p - 1
  t = int(math.isqrt(q))
    
  # Baby steps
  baby_steps = {}
  for i in range(0, (q // t) + 1):
      current_power = pow(g, i * t, p)
      baby_steps[current_power] = i
  
  # Giant steps
  for i in range(1, t + 1):
      giant_step= (h * pow(g, i, p)) % p
      if giant_step in baby_steps:
          k = baby_steps[giant_step]
          return (k * t - i) % q
  
  return None

def main():
  p = 2**31 - 1
  username = "CHEN7790" #use all caps?
  n = int.from_bytes(hashlib.sha256(username.encode('utf-8')).digest(), 'big') % p
  
  print("CHEN7790 as n={}".format(n))
  
  # set log base 7
  g = 7  
  x = baby_step_giant_step_textbook(g, n, p)
  
  print(f"Answer to log(7) {n} mod {p}: {x}")

if __name__ == "__main__":
    main()