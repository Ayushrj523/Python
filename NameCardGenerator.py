print("=== Name Card Generator ===")

name = input("Enter your name: ")
email = input("Enter your email: ")
contact = input("Enter your contact: ")

line1 = f"| Name   : {name}"
line2 = f"| Email  : {email}"
line3 = f"| Contact: {contact}"

max_length = max(len(line1), len(line2), len(line3))
border = "+" + "-" * (max_length - 1) + "+"

line1 = line1 + " " * (max_length - len(line1)) + "|"
line2 = line2 + " " * (max_length - len(line2)) + "|"
line3 = line3 + " " * (max_length - len(line3)) + "|"

print("\nYour Name Card:\n")
print(border)
print(line1)
print(line2)
print(line3)
print(border)

save = input("\nDo you want to save it as a .txt file? (y/n): ").lower()
if save == 'y':
    filename = input("Enter filename (without extension (i.e. .txt)): ")
    with open(filename + ".txt", "w") as file:
        file.write(border + "\n")
        file.write(line1 + "\n")
        file.write(line2 + "\n")
        file.write(line3 + "\n")
        file.write(border + "\n")
    print(f"Name card saved as {filename}.txt")