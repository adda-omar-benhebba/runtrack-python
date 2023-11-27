def custom_round(number):
    decimal_part = number - int(number)
    if decimal_part >= 0.5:
        return int(number) + 1
    else:
        return int(number)

def custom_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
rounded_numbers = [custom_round(num) for num in numbers]
sorted_rounded_numbers = custom_sort(rounded_numbers)

print("Liste arrondie et triée :", sorted_rounded_numbers)
