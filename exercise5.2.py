try:
    student_name_raw =input("სტუდენტის სახელი: ").strip()
    student_name = f"{student_name_raw[0]}. {student_name_raw}"
    student_score = int(input("მიღებული ქულა: "))
    max_score = int(input("მაქსიმალური ქულა: ")) 
    percentage = (student_score / max_score * 100)
    
    if 100 >= percentage > 90:
        grade = "A"
    elif percentage > 80:
        grade = "B"
    elif percentage > 70:
        grade = "C"
    elif percentage > 60:
        grade = "D"
    elif percentage > 50:
        grade = "E"
    elif percentage > 40:
        grade = "FX"
    else:
        grade = "F"
    
except IndexError:
    print("❌ სახელი ცარიელი ვერ იქნება")
except ValueError:
    print("❌ ქულების შესაყვანად გამოიყენეთ მთელი რიცხვები")
except ZeroDivisionError:
    print("❌ მაქსიმალური ქულა ნულის ტოლი ვერ იქნება")
else: 
    if student_score < 0 or student_score > max_score:
        print("❌ ქულა არასწორ დიაპაზონშია")
    else:
        print(f"✅ {student_name} - {percentage:.1f}% - შეფასება: {grade}")
finally:
    print("შეფასების სისტემამ მუშაობა დაასრულა")
