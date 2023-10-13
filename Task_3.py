user_name = input("Enter Your name: ").strip().capitalize()
password = input("Enter Your password=>> ").strip()
Id = input("Enter Your ID (14_number): ")
code = {
    "01": "Cairo",
    "02": "Alexandria",
    "03": "Port Said",
    "04": "Suez",
    "11": "Damietta",
    "12": "Dakahlia",
    "13": "Elsharqia",
    "14": "Qalyubia",
    "15": "Kafr El-Sheikh",
    "16": "Elgharbia",
    "17": "Menoufia",
    "18": "Elbehira",
    "19": "Ismailia",
    "21": "Giza",
    "22": "Beni Suef",
    "23": "Fayoum",
    "24": "Minya",
    "25": "Assiut",
    "26": "Sohag",
    "27": "Qena",
    "28": "Aswan",
    "29": "Luxor",
    "31": "Red Sea",
    "32": "El wady elgedeed",
    "33": "Matrouh",
    "34": "North Sinai",
    "35": "South Sinai",
    "88": "You were born outside Egypt"
}

if len(Id) != 14 or not Id.isalnum():
    print('Wrong Id check it again')
else:
    cen = Id[0:1]
    year = Id[1:3]
    month = Id[3:5]
    day = Id[5:7]
    city = Id[7:9]
    gender = int(Id[12:13])

    if cen == "3" or cen == "2":
        century = "twenty-first century" if cen == "3" else "twenty century"
        print(f"You born in The twenty-first century ")
        print(f"Hi {user_name}\nyour data of birth: {day}-{month}-20{year}")
        if (gender % 2) != 0:
            print("Gender==> Male")
        else:
            print('Gender==> female')
        if city in code:
            print(f"You born in==>{code[city]}")
        else:
            print('City not found in the code dictionary \nyou have an issue in your ID')
    else:
        print('Invalid number of your ID. Please check it again.')