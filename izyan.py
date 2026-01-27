import math
bs=float(input("Enter basic salary:"))
da=0.7*bs
ta=0.3*bs
hra=0.1*bs
# gs= bs+da+ta+hra
gs=math.fsum([bs,da,ta,hra])
print(f"Gross salary = RS.{gs}")