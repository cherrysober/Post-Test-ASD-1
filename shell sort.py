import random
def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

data = []

print("Shell Sorting")
n = int(input("Masukkan Jumlah Elemen: "))
for i in range(0,n):
    elemen = random.randrange(50)
    data.append(elemen)

print("Sebelum Sorting")
print(data)
size = len(data)

shellSort(data, n)
print("Setelah Sorting")
print(data)