"""
Convert KB to bits, bytes, MB and GB

"""

#prompt the user to enter file size in kilobytes
input_kb = float(input("Enter a file size, in kilobytes (KB): "))
print()

#print user's input
print(input_kb, "KB ...")
print()

#convert input into bits
bits_calc = input_kb * (1024 * 8)

#convert input into bytes
bytes_calc = input_kb * 1024

#convert input into megabytes
megabytes_calc = input_kb/1024

#convert input into gigabytes
gigabytes_calc = input_kb/(1024**2)

#format values to be strings
f_bits = format(bits_calc, ",.2f")
f_bytes = format(bytes_calc, ",.2f")
f_megabytes = format(megabytes_calc, ",.2f")
f_gigabytes = format(gigabytes_calc, ",.2f")


#output - bits
print(format("... in bits", "<25s"), end="")
print(format(f_bits, ">15s"), "bits")

#bytes
print(format("... in bytes", "<25s"), end="")
print(format(f_bytes, ">15s"), "bytes")

#megabytes
print(format("... in megabytes", "<25s"), end="")
print(format(f_megabytes, ">15s"), "MB")

#gigabytes
print(format("... in gigabytes", "<25s"), end="")
print(format(f_gigabytes, ">15s"), "GB")

"""
FIVE WAYS TO CRASH THIS PROGRAM

1. this would cause a sneaky syntax error because the nested format()
is missing an end parenthesis

print(format("... in megabytes", "<25s", end="")


2. this would also cause a syntax error because the format()'s
command is missing a delmiter

f_bits = format(bits_calc, ,.2f")


3. The following line would cause a runtime error - the program would run as
usual up to here because the variable name is misspelled, and therefore the
variable is undefined in the program. Python would have no way of referencing
a calculation that doesn't exist. 

print(format(f_metabytes, ">15s"), "MB")


4. This line would also cause a runtime error, since the format() is missing.
All of the calculations that take place depend on the information that the
user inputs, and since input() only takes things and turns them into strings
we need to use float() to turn it into a float. Without float(), the calculations
will return an error. 

input_kb = input("Enter a file size, in kilobytes (KB): ")


5. a logic error would occur here - even though the program functionally runs,
it would produce the incorrect result (it would convert to megabytes instead of gigabytes)

print(format("... in gigabytes", "<25s"), end="")
print(format(f_megabytes, ">15s"), "GB")

"""
