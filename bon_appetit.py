def bonAppetit(bill, k, b):
    if len(bill) >= 0:
        no_pay_flg = False
        no_pay_flg = True if k >= 0 and k < len(bill) else False
        if b > 0:
            if no_pay_flg:
                bill.remove(bill[k])
            total_amount = sum(s for s in bill)
            amount_per_head = total_amount/2
            print("Bon Appetit") if b - amount_per_head == 0 else print(int(b - amount_per_head))