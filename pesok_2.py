from DataBase import DataBase
from decimal import Decimal


def up_ballans(id: int, summ: float, bill_up="debit"):
    db = DataBase(
        host="127.0.0.1",
        port=3306,
        user="Root_Adm",
        password="Koshkin3322!",
        database="test_name",
    )
    qwer = f"SELECT user_bill.type_bill, user_bill.ballans, user_bill.limit_bill, user_bill.status_bill, user_bill.bill_idd FROM user_bill JOIN user ON user.id = user_bill.user_id WHERE user.id = {id};"
    g_d = db.execute_query(query=qwer)
    for i in g_d:
        if bill_up in i:
            try:
                sum_update = round(i[1] + summ, 2)
                id_bill = i[4]
                set_user_ballans = f"UPDATE user_bill SET ballans = {sum_update} WHERE user_id = {id} AND bill_idd = {id_bill} AND status_bill = 'active'"
                g_d = db.execute_query(query=set_user_ballans)
            except Exception as e:
                print(f"операция отменена по причине {e}")
            else:
                print("pending")
            finally:
                qwer = f"SELECT user_bill.type_bill, user_bill.ballans, user_bill.limit_bill, user_bill.status_bill, user_bill.bill_idd FROM user_bill JOIN user ON user.id = user_bill.user_id WHERE user.id = {id};"
                g_d = db.execute_query(query=qwer)
                for i in g_d:
                    if bill_up in i:
                        if sum_update == i[1]:
                            print('Asepted')
                        else:
                            print(f'eror in ransaction, check status your bill - {i[3]}')
                return g_d
        else:
            raise Exception("Нету доступных счетов для пополнения")


def transfer_money(self):
    pass


def operations(self):
    pass


def exter(data):
    pass


rt = up_ballans(4, 213.42, 'credit')
print(rt)
# (
#     ("credit", -213.42, "limit_2", "de_active", 5668),
#     ("debit", 322.89, "no_limit", "active", 7873),
# )
# ballans = -213.42
# result = round(ballans + 213.42, 2)
# print(result)
