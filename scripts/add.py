
import os

name = input("Enter your name: ")
sport = input("Enter your favorite sport: ")

with open(os.path.join("input", f"{name}.txt"), "w") as f:
    f.write(f"{name}, {sport}")
