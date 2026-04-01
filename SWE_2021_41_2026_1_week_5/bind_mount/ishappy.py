def isHappy(n):
  unhappy = set()

  while n != 1:

    if n in unhappy:
      return False

    unhappy.add(n)

    ss = 0
    while n > 0:
      ss += (n%10)**2
      n = int(n/10)

    n = ss

  return True

if __name__ == "__main__":
    sample0_output = isHappy(19) 
    sample1_output = isHappy(2) 
    
    with open("/app/bind_mount/output.txt", "w") as f: 
        f.write(f"19: {sample0_output}\n") 
        f.write(f"2: {sample1_output}\n") 
        print("Results saved to /app/bind_mount/output.txt")