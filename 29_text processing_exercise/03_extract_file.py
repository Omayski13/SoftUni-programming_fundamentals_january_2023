name, file_extencion = input().split(".")

name = name.split("\\")

file_name = name[-1]


print(f"File name: {file_name}")
print(f"File extension: {file_extencion}")
