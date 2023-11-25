from typing import Any
from DataBase import DataBase
from authentic_user import Verif_user
from verifi_input import VerifUserInput


class SingletonMeta(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Banc(metaclass=SingletonMeta):
    def __init__(self, user_id, gmail):
        if not hasattr(self, "_initialized"):
            self._user_id = user_id
            self._status = "user"
            self._owner_gmail = gmail
            self._info()
            self._initialized = True

    def _info(self):
        init_user_info = self._initialize()
        init_data_bill = self._initialize(type_qwery="user_bill")
        if init_data_bill is None and init_user_info is None:
            return "данные не полные"
        else:
            format_user = self.executer(init_user_info)
            format_bill = self.executer(init_data_bill, output="user_bill")
            print(format_user)
            print(format_bill)

    def _initialize(self, type_qwery="user_info"):
        db = DataBase(
            host="127.0.0.1",
            port=3306,
            user="Root_Adm",
            password="Koshkin3322!",
            database="test_name",
        )
        try:
            #  AND user_bill.status_bill != 'de_active'
            if type_qwery == "user_info":
                user_informatioin = f"SELECT user.first_name as user_name, user.phone_number as user_phone_number, user_auth.gmail as user_mail, user_document.status_aprove as documet_aprove FROM user JOIN user_auth ON user_auth.user_id = user.id JOIN user_document ON user_document.user_id = user.id WHERE user.id = {self._user_id};"
                full_data = db.execute_query(user_informatioin)
            elif type_qwery == "user_bill":
                user_bill_information = f"SELECT user_bill.type_bill, user_bill.ballans, user_bill.limit_bill, user_bill.status_bill FROM user_bill JOIN user ON user.id = user_bill.user_id WHERE user.id = {self._user_id};"
                full_data = db.execute_query(user_bill_information)
        except Exception as e:
            print(f"Error - {e}")
        else:
            if full_data == () or full_data == ((0),) or full_data == ((),):
                return None
            else:
                return full_data

    def executer(self, data: tuple, output="user_info"):
        if data is None:
            return "Data is None"
        else:
            if output == "user_info":
                if len(data) < 2:
                    for i in data:
                        if i[3] == "pending":
                            ch = [
                                {"Name": i[0]},
                                {"Phone": i[1]},
                                {"Email": i[2]},
                                {"BILL STATUS": {i[3]}},
                            ]
                            return ch
                        else:
                            ch = [{"Name": i[0]}, {"Phone": i[1]}, {"Email": i[2]}]
                            return ch
                else:
                    raise Exception(
                        "НЕ МОЖЕТ БЫТЬ 2-Х ПОЛЬЗОВАТЕЛЕЙ, скорее всего ошибка"
                    )
            elif output == "user_bill":
                result = []
                if len(data) >= 2:
                    for i in data:
                        ch = res = [
                            {"Bill": i[0]},
                            {"Ballance": i[1]},
                            {"Limits": i[2]},
                            {"Bill_status": i[3]},
                        ]
                        result.append(ch)
                    return result
                else:
                    for i in data:
                        res = [
                            {"Bill": i[0]},
                            {"Ballance": i[1]},
                            {"Limits": i[2]},
                            {"Bill_status": i[3]},
                        ]
                    return res

    def up_ballans(self, summ: float, bill_up="debit"):
        db = DataBase(
            host="127.0.0.1",
            port=3306,
            user="Root_Adm",
            password="Koshkin3322!",
            database="test_name",
        )
        qwer = f"SELECT user_bill.type_bill, user_bill.ballans, user_bill.limit_bill, user_bill.status_bill, user_bill.bill_idd FROM user_bill JOIN user ON user.id = user_bill.user_id WHERE user.id = {self._user_id};"
        g_d = db.execute_query(query=qwer)
        for i in g_d:
            if bill_up in i:
                try:
                    sum_update = round(i[1] + summ, 2)
                    id_bill = i[4]
                    set_user_ballans = f"UPDATE user_bill SET ballans = {sum_update} WHERE user_id = {self._user_id} AND bill_idd = {id_bill} AND status_bill = 'active'"
                    g_d = db.execute_query(query=set_user_ballans)
                except Exception as e:
                    print(f"операция отменена по причине {e}")
                else:
                    print("pending")
                finally:
                    qwer = f"SELECT user_bill.type_bill, user_bill.ballans, user_bill.limit_bill, user_bill.status_bill, user_bill.bill_idd FROM user_bill JOIN user ON user.id = user_bill.user_id WHERE user.id = {self._user_id};"
                    g_d = db.execute_query(query=qwer)
                    for i in g_d:
                        if bill_up in i:
                            if sum_update == i[1]:
                                print("Asepted")
                            else:
                                print(
                                    f"eror in ransaction, check status your bill - {i[3]}"
                                )
                    return g_d
            else:
                raise Exception("Нету доступных счетов для пополнения")

    def transfer_money(self):
        pass

    def operations(self):
        pass


class NewUser:
    def create_account(self):
        pass

    def get_aprove_passport(self):
        pass

    def create_bill(self):
        pass


gmail = "hoklin43@gmail.com"  # input("Введите gmail: ")
passw = "RTY345retyy"  # input("Введие пароль: ")
phon_num = "+79215501110"  # input("Введите номер телефона: ")


# первый этап проверки на правильность ввода
vr = VerifUserInput()
mail = vr.verif_gmail(gmail)
pasw = vr.verif_password(passw)
ph_num = vr.verif_phone_num(phon_num)

# вход в аккаунт пользователся
if mail and pasw and ph_num:
    ap = Verif_user(ph_num, log=mail, pas=pasw)
if ap:
    cl = Banc(ap[0], ap[1])
