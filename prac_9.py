def merge(left,right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i = i+1 

        else:
            result.append(right[j])
            j = j+1

        #Adding remaining orders
        while i < len(left):
            result.append(left[i])
            i = i+1

        while j < len(right):
            result.append(right[j])
            j = j+1
        return result

def merge_sort(orders):
    #one order or empty list is already sorted
    if len(orders) <=1:
        return orders

    mid = len(orders)//2
    left_half = merge_sort(orders[ :mid])
    right_half = merge_sort(orders[mid: ])

    return merge(left_half,right_half)


def display(orders):
    print("order id dilevery time in minutes")
    print("------")
    for order in orders:
        print(order[0],order[1])

#main programm------
orders = []
n = int (input("Enter the number of orders"))

for i in range(n):
    print("\n Orders ", i+1)
    order_id = input("order id: ")
    time = int(input("Enter delivery time in minutes: "))
    orders.append([order_id,time])


print("\n Orders before sorting: ")
display(orders)

sorted_order = merge_sort(orders)

print("\nOrders after sorting .")

display(sorted_order)
        