def say_hello(username, age):
  print(f"Hello, {username}.")
  print(f"Your age is {age}.")
  print("-" * 20)

  if age <= 18:
    print("- you`re younger!")
  elif age == 18:
    print("- you`re an adult!")
  else:
    print("- you`re older than all of them!")

say_hello("Sonja", 15)
say_hello("Max", 20)
say_hello("Leon", 30)