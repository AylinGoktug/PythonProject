from datetime import datetime

current_time = datetime.now()
print(f"Şimdiki Zaman : {current_time}")

formatter_year_long = current_time.strftime("%Y/%m/%d")
print(f"Güncel Tarih Formatı : {formatter_year_long}")

formatter_year_short = current_time.strftime("%y")
print(f"Güncel Yıl Formatı {formatter_year_short}")