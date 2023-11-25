import random
import json
import concurrent.futures
from DataBase import DataBase
import string


def fac_stat():
    data = ["Активен", "Неактивен", "Умеренно-активен"]
    rand = random.randint(0, 2)
    return data[rand]


def fac_inf():
    data = ["new", "old"]
    rand = random.randint(0, 1)
    return data[rand]


def facke_phon_num():
    ish = +79
    rand = random.randint(106004001, 950708959)
    return f"+{ish}{rand}"


def facke_name(male="male"):
    if male == "male":
        with open("first_name_m.json", "r") as fl:
            cont = json.load(fl)
            rand = random.randint(0, len(cont) - 1)
            return cont[rand]
    else:
        with open("first_name_f.json", "r") as fl:
            cont = json.load(fl)
            rand = random.randint(0, len(cont) - 1)
            return cont[rand]


def facke_sname(male="male"):
    with open("last_name.json", "r") as fl:
        cont = json.load(fl)
    if male == "male":
        rand = random.randint(0, len(cont) - 1)
        return cont[rand]
    else:
        rand = random.randint(0, len(cont) - 1)
        return f"{cont[rand]}a"


def facke_fname(male="male"):
    with open("father_name_m.json", "r") as fl:
        cont = json.load(fl)
    if male == "male":
        rand = random.randint(1, len(cont) - 1)
        return cont[rand]
    else:
        with open("father_name_f.json", "r") as fl:
            cont = json.load(fl)
            rand = random.randint(1, len(cont) - 1)
            return cont[rand]


def facke_date(a=1, b=23, who="b"):
    if who == "b":
        year = random.randint(a, b)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        if month >= 10 and day >= 10:
            return f"{year}-{month}-{day}"
        elif month >= 10 and day <= 10:
            return f"{year}-{month}-0{day}"
        elif day >= 10 and month <= 10:
            return f"{year}-0{month}-{day}"
        else:
            return f"{year}-0{month}-0{day}"


def facke_time(a=0, b=23, AT_AM=24):
    hours = random.randint(a, b)
    minyte = random.randint(0, 59)
    sec = random.randint(1, 59)
    result = f"{hours}:{minyte}:{sec}"
    return result


def random_data_name(male, data_bird=(1960, 2002)):
    if male == 1 or male == 0:
        # male
        fake_male_first_name = facke_name()
        fake_male_last_name = facke_sname()
        fake_middle_name = facke_fname()

        fake_birthdate = facke_date(1960, 2002)
        fake_phone_number = facke_phon_num()
        fake_registration_date = f"{facke_date(2010, 2023)} {facke_time()}"
        fake_status = fac_stat()
        fake_cl_inf = fac_inf()
        fake_sec_st = random.randint(0, 1)

        # return - set data
        full_fake_set = (
            fake_male_first_name,
            fake_male_last_name,
            fake_middle_name,
            fake_birthdate,
            fake_phone_number,
        )
        return full_fake_set

    else:
        # female
        fake_female_first_name = facke_name(male="female")
        fake_female_last_name = facke_sname(male="female")
        fake_female_middle_name = facke_fname(male="female")

        fake_birthdate = facke_date(data_bird[0], data_bird[1])
        fake_phone_number = facke_phon_num()
        fake_registration_date = f"{facke_date(2010, 2023)} {facke_time()}"
        fake_status = fac_stat()
        fake_cl_inf = fac_inf()
        fake_sec_st = random.randint(0, 1)

        # return - set data
        full_fake_set = (
            fake_female_first_name,
            fake_female_last_name,
            fake_female_middle_name,
            fake_birthdate,
            fake_phone_number,
        )
        return full_fake_set


class Fakerrr:
    def __init__(self, count=100, male=50) -> None:
        self.count = count
        self.male = male

    def multi_gen(self, count=1, priority="male"):
        if priority == "male":
            ch = [random.randint(0, 2) for _ in range(0, count)]
        elif priority == "female":
            ch = [random.randint(1, 3) for _ in range(0, count)]
        else:
            ch = [random.randint(0, 3) for _ in range(0, count)]
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            results = list(executor.map(random_data_name, ch))
            return results


# cl = Faker()
# rt = cl.multi_gen(count=5, priority="female")
# for i in rt:
#     print(i)

# rt = pass_gen(count=20, lenn=10, unique=50)
# print(rt)


def generate_random_email(count=10):
    res = []
    ch = 0
    while ch < count:
        words = [
            "apple",
            "banana",
            "orange",
            "grape",
            "peach",
            "kiwi",
            "melon",
            "strawber",
            "lemon",
            "lime",
            "bluebe",
            "raspber",
            "blackber",
            "pineapp",
            "waterme",
            "apricot",
            "plum",
            "pear",
            "cherry",
            "fig",
            "pomegra",
            "mango",
            "papaya",
            "nectarine",
            "cantalo",
            "date",
            "coconut",
            "guava",
            "kiwi",
            "passion",
            "tangeri",
            "lime",
            "lemonade",
            "grapef",
            "dragon",
            "persimm",
            "avocado",
            "quince",
            "honeyde",
        ]
        username = "".join(random.sample(words, k=2)) + "".join(
            random.choices(string.digits, k=2)
        )
        domain = random.choice(["gmail.com", "yahoo.com", "hotmail.com", "example.com"])
        res.append(f"{username}@{domain}")
        ch += 1
    return res


def pass_gen(count=10, lenn=10, unique=100):
    result = []
    cd = 0
    while cd <= count:
        res = []
        ch = 0
        while ch <= lenn:
            letters = [
                "QqqWwwEeRrrTttYyyUuIiOooPppAaSsdDdFffGggHhhJjjKkkLlZzzXxxCcVcvBbNnvbMm"
            ]
            num = ["0123456789"]
            simb = ["!#$-_"]
            if unique == 100:
                ras = random.randint(0, 10)
                if ras >= 0 and ras <= 5:
                    res.append(random.choice(letters[0]))
                elif ras >= 5 and ras <= 9:
                    res.append(random.choice(num[0]))
                elif ras == 10:
                    res.append(random.choice(simb[0]))
                ch += 1
            else:
                ras = random.randint(0, 1)
                if ras == 0:
                    res.append(random.choice(letters[0]))
                else:
                    res.append(random.choice(num[0]))
                ch += 1
        result.append("".join(res))
        cd += 1
    return result
