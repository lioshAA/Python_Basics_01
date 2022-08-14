
clients = [ ['Берізка', 'Іванов', 3],
                ['Берізка', 'Іванова', 5],
                ['Бриз', 'Іванова', 5],
                ['Морячка', 'Іванова', 5]
]
hotels = dict();

for voucher in clients :
    voucher_hotels = voucher[0]
    voucher_persons = voucher[2]
    if hotels.get(voucher_hotels, 0) == 0:
        hotels[voucher_hotels] = voucher_persons
    else:
        hotels[voucher_hotels] = hotels[voucher_hotels] + voucher_persons
print(hotels)