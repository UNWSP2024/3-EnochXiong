def weight_conversion(weight):

    shippingCost = 0.0
    
    if weight <= 2:
        shippingCost = weight * 1.50
    elif weight <= 6:
        shippingCost = weight * 3.00
    elif weight <= 10:
        shippingCost = weight * 4.00
    else:
        shippingCost = weight * 4.75
    return shippingCost


if __name__ == '__main__':
    weight = 0.0
    shippingCost = 0.0
    weight = float(input('Enter the weight of the package: '))
    shippingCost = weight_conversion(weight)
    print('Shipping charge: $', format(shippingCost, '.2f'))
