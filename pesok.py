from Faker import generate_random_email, pass_gen
from DataBase import DataBase
from Faker import facke_phon_num

rand_phone_num = facke_phon_num()
rand_pass = pass_gen(count=10, lenn=15, unique=100)
rand_mail = generate_random_email(count=10)
auth_data = tuple(zip(rand_pass, rand_mail))
# for i in auth_data:
#     print(i)

# print(rand_phone_num)

df = (("debit", 6322.5), ("credit", -433.65))


def up_ballans(self):
    pass


db = DataBase(
    host="127.0.0.1",
    port=3306,
    user="Root_Adm",
    password="Koshkin3322!",
    database="test_name",
)

user_id = 4
# запрос данных о счетах юзера
user_bill_information = f"SELECT user_bill.type_bill, user_bill.ballans, user_bill.limit_bill, user_bill.status_bill FROM user_bill JOIN user ON user.id = user_bill.user_id WHERE user.id = {user_id};"
# запрос данных о пользователе
user_informatioin = f"SELECT user.first_name as user_name, user.phone_number as user_phone_number, user_auth.gmail as user_mail, user_document.status_aprove as documet_aprove FROM user JOIN user_auth ON user_auth.user_id = user.id JOIN user_document ON user_document.user_id = user.id WHERE user.id = {user_id};"


# запрос на пополнение баланса
sum_update = float(244.54)
user_id = 6
bill_id = 5456
set_user_ballans = f"UPDATE user_bill SET ballans = {sum_update} WHERE user_id = {user_id} AND bill_id = {bill_id} AND status_bill = 'active'"

# запрос на создание аккаунта
data_acc = ["Вениамин", "Харикин", "Анатольевич", "2000-04-18", "+79826638941"]
set_user = f"INSERT INTO user (first_name, last_name, father_name, date_birt, phone_number) VALUES({data_acc})"

# запрос на создание учетной записи для входа
data_auth = ["Brpvj-1zhZ0t92tY", "limedate23@gmail.com", 11, "+79826638941"]
set_user_auth = f"INSERT INTO user_auth (password, gmail, user_id, user_phone_num) VALUES({data_auth})"

# запрос добавления паспортных данных
data_document = [31507990, 446745943, 11]
set_user_document = f"INSERT INTO user_document (passport_id, SSN_num, user_id) VALUES ({data_document}) "

# запос на создане нового счета
data_user_bill = []
set_user_bill = f"INSERT INTO user_bill (user_id, type_bill, ballans, limit_bill)VALUES ({data_user_bill})"

# запрос на смену пароля, почты, телефона
set_user_auth_update = f""


# res = db.execute_query(user_informatioin)
# for i in res:
#     print(i)
