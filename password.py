password = 'a123456'
count = 3

while count <= 3:
    user_input = input('請輸入密碼(最多3次):')
    if user_input == password:
        print('登入成功')
        break
    else:
        count = count - 1
        print('密碼錯誤,剩下', count, '次機會!!')
        if count == 0:
            print('此帳號已被鎖定!!!')
            break