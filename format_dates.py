from datetime import datetime
final = []

dates = ["04/07/2022", "31/12/2023", "10/01/2021", "22/11/2025"]

for date in dates:
    date_object = datetime.strptime(date,"%d/%m/%Y")
    formatted = date_object.strftime("%B %d,%Y")
    final.append(formatted)
print(final)
