from DataBase import DataBase


class Verif_user:
    """
    Проверяет есть ли аккаунт в базе, и есть ли
     - user id и ВЕРЕНЫ - логигн и пароль
    если нет - False, возвращает id и gmail
    """

    def __new__(cls, phone_number: str, log: str, pas: str):
        db = DataBase(
            host="127.0.0.1",
            port=3306,
            user="Root_Adm",
            password="Koshkin3322!",
            database="test_name",
        )
        ap_info = cls.aprovied_phone_num(phone_number, db)
        if ap_info:
            extract = cls.unpack_tuple(ap_info)
            data_auth = cls.get_auth_data(extract, db)
            if data_auth:
                extract_auth_data = cls.unpack_tuple(data_auth)
                if (log, pas) == extract_auth_data:
                    return extract, extract_auth_data[0]
                else:
                    print("Логин и пароль для входа не совпдают")
                    return False
            else:
                print("По id который передан нету данных для входа в Л/К")
                return False
        else:
            print("По номеру который указан, нету не одного аккауната в базе")
            return False

    @staticmethod
    # функция возвращает id по номеру телефона
    def aprovied_phone_num(phone_num, conect):
        query = f"SELECT user.id FROM user WHERE phone_number={phone_num}"
        result = conect.execute_query(query)
        return result

    @staticmethod
    # функция возвращает почту и пароль по id
    def get_auth_data(user_id, conect):
        query = f"SELECT user_auth.gmail, user_auth.password FROM user_auth WHERE user_id={user_id}"
        result = conect.execute_query(query)
        return result

    @classmethod
    # функция распаковки данных из БД
    def unpack_tuple(self, data):
        if isinstance(data, tuple) and len(data) == 1:
            return self.unpack_tuple(data[0])
        else:
            return data
