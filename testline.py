from songline import Sendline

# token สำหรับบ็อทที่ชื่อว่า....ส่งเข้าไปในกลุ่มชื่อ RPA 2023
token = 'T7NH2gEKyWSV4VA2bRGfsfuYrkbDZ15Juh9nopSpYll'

m = Sendline(token)
m.sendtext('Hello')

# https://uncle-engineer.com/api/sticker.pdf
# m.sticker(222,3,'อุณหภูมิร้อนมากแล้ว เปิดปั้มได้แล้ว!')

# m.sendimage('https://static.thairath.co.th/media/dFQROr7oWzulq5FZUEh0Nz618JDNM6KUa11heACMVB8Xv3HERnORb6OBktFdurPV8Oy.jpg')

# path = r'C:\Users\Uncle Engineer\Desktop\RPA 2023\rain.png'
# # path = 'C:\\Users\\Uncle Engineer\\Desktop\\RPA 2023\\rain.png'
# m.sendimage_file(path)


