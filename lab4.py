"""Patrick Robinson
9/16/22
This code calculates the amount of perfect numbers, abundant numbers, and deficient numbers in a number that the user inputs."""

properDivisorcount=0
perfectNumbercount=0
abundantNumbercount=0
deficientNumbercount=0
sumofproper=0
upperBound=int(input("Enter an upper bound for a check: "))

for i in range(1, upperBound+1): #calculates amount of proper divisors
	for num in range(1, i):
		if i % num == 0:
			sumofproper += num
		
	if sumofproper == i: #Calculates amount of perfect numbers
		perfectNumbercount += 1
	elif sumofproper < i: #Calculates amount of deficient numbers
		deficientNumbercount += 1
	elif sumofproper > i: #Calculates amount of abundant numbers
		abundantNumbercount += 1
	sumofproper = 0
	

print("Between 1 and ", upperBound, "there are :")
print(deficientNumbercount, "Deficient numbers")
print(perfectNumbercount, "Perfect numbers")
print(abundantNumbercount, "Abundant numbers")
