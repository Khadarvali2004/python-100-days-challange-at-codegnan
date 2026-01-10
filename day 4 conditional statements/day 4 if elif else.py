#if elif else
num=int(input())
if num%2==0 and num>=0:
    print("number is even and positive")
elif num%2!=0 and num<0:
    print("number is odd and negative")
elif num%2!=0 and num>=0:
    print("number is odd and poistive")
else:
    print("number is odd and negative")
