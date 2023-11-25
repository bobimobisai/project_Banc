class VerifUserInput:
    def verif_gmail(self, mail):
        try:
            if (
                all((type(mail) is str, "@" in mail, len(mail) < 60))
                and mail.isdigit() is False
            ):
                return mail
        except TypeError:
            return "name -> only str"
        else:
            return False

    def verif_password(self, pasw):
        try:
            if type(pasw) is str and len(pasw) <= 60:
                return pasw
        except TypeError:
            return "password -> max 60"
        else:
            return False

    def verif_phone_num(self, phone_num):
        try:
            if type(phone_num) is str and len(phone_num) >= 12 and phone_num[0] == "+":
                return phone_num
        except Exception as e:
            print(f"Error - {e}")
        else:
            return False
