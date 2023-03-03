for a in range(210235,210300+1):
    k=0
    for b in range(2,a//2+1):
        if a % b ==0:
            k+=1
        if k>4:
            break
    if k==4:
      for i in range(2,a//2+1):
          if a % i ==0:
              print(i, end=' ')
      print()
