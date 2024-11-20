def search_subarray(arr, subarr):

for i in range(len(arr) len(subarr) + 1):

if arr[i:i+len(subarr)] == subarr:

return i

return -1

def main():

arr = [1, 2, 3, 4, 5, 6] 
subarr = [3, 4, 5]

result = search_subarray(arr, subarr)

if result != -1:

print(f"Subarreglo encontrado en el índice (result}")

else:

print("Subarreglo no encontrado.")

if_name == "main":

main()