def computepay(h,r):
    hr=float(h)
    rt=float(r)
    if hr>40:
        return ((40*rt)+(hr-40)*(rt*1.5))
    else:
    	return 40*rt

hrs = input("Enter Hours:")
rate= input("enter rate:")
p = computepay(hrs,rate)
print("Pay",p)