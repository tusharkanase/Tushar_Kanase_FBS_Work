correct_id = "admin"
correct_pass = "1234"

for i in range(3):
  uid = input("Enter ID : ")
  pas =input("Enter Password : ")

  if uid == correct_id and pas == correct_pass:
    print("Login Successful")
    break
  else:
    print("Wrong ID or Password")

    if(i == 2):
        print("program Terminated")
