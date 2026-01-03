from datetime import datetime
from xmlrpc.client import DateTime

user_input = input("Tarih Giriniz : (YYYY-MM-DD)")

date_object = datetime.strftime(user_input, "%Y/%m/%d")

print(f"Güncel Tarih Formatı : {date_object}")