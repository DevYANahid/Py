

with open("semp.txt","r") as f:
    data = f.read()

new_data = data.replace("fahim","my future wife is ")
print(new_data)


with open("semp.txt","w") as f:
    f.write(new_data)