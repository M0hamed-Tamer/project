# ----------------
# -- Generators --
# ----------------
# [1] Generator is a Function With "yield" Keyword Instead of "return"
# [2] It Support Iteration and Return Generator Iterator By Calling "yield"
# [3] Generator Function Can Have one or More "yield"
# [4] By Using next() It Resume From Where It Called "yield" Not From Begining
# [5] When Called, Its Not Start Automatically, Its Only Give You The Control
# -----------------------------------------------------------------

def myGenerator():
  yield 1
  yield 2
  yield 3
  yield 4
  yield 5

myGenerator()

print(next(myGenerator()), end=" ")
print("Hello From Python")
print(next(myGenerator()), end=" ")

# print(myGenerator())
for number in myGenerator():
  print(f"{number}")