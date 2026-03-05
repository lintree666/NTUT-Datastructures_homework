pair = {}
while True:
    option = input("請輸入操作選項(a 註冊, b 登入, c 退出) ?")
    
    if option.lower() == "a":
        account = input("請輸入帳號： ")
        if account in pair:
            print("帳號已存在，請重新輸入！")
        else:
            password = input("請輸入密碼： ")
            pair[account] = password
            print("註冊成功！")
            
    elif option.lower() == "b":
        log_account = input("請輸入帳號： ")
        if log_account in pair:
            log_password = input("請輸入密碼： ")
            if pair[log_account] == log_password:
                print("登入成功！")
            else:
                print("密碼輸入錯誤！")
        else:
            print("帳號不存在")
            
    elif option.lower() == "c":
        print("程式已結束運行")
        break
    else:
        print(" 無效選項，請輸入操作選項(a 註冊, b 登入, c 退出) ? ")