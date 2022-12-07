
    #Đẩy xuống dưới
    khoang_cach_can_sua_tren=h-(H-y2)
    if khoang_cach_can_sua_tren<0:
        khoang_cach_can_sua_tren=0
    if y1-khoang_cach_can_sua_tren<0:
        khoang_cach_can_sua_tren=10**9

    #Đẩy lên trên
    khoang_cach_can_sua_duoi=h-(y1)
    if khoang_cach_can_sua_duoi<0:
        khoang_cach_can_sua_duoi=0
    if y2+khoang_cach_can_sua_duoi>H:
        khoang_cach_can_sua_duoi=10**9

    #Đẩy qua phải:
    khoang_cach_can_sua_trai=w-x1
    if khoang_cach_can_sua_trai<0:
        khoang_cach_can_sua_trai=0
    if x2+khoang_cach_can_sua_trai>W:
        khoang_cach_can_sua_trai=10**9

    #Đẩy qua trái:
    khoang_cach_can_sua_phai=w-(W-x2)
    if khoang_cach_can_sua_phai<0:
        khoang_cach_can_sua_phai=0
    if x1-khoang_cach_can_sua_phai<0:
        khoang_cach_can_sua_phai=10**9
        
    print(min(khoang_cach_can_sua_phai,khoang_cach_can_sua_trai,khoang_cach_can_sua_tren,khoang_cach_can_sua_duoi))

        
    