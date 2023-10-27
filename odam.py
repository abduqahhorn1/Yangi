from pyrogram import Client
# DASTURCHI @MrGayratov Kanal : @KingsOfPy
"""
# PYROGRAM Module orqalik odiygina tayorlangan kod...
# Shunchaki bu kod orqalik guruhdan gurhga odam olib otishingiz mumkin...
# Tushunarli bo'lishi uchun boshlanishiga odiygina yozilgan...
# Ogohlantirish ! Akuntingiz Spam bo'lsa yoki blok bo'lsa dasturchi javob bermaydi...

# Negativ va Senior dasturchilar negativ yozmelar boshlanishiga kod bu...

# Manba bilan olinglar do'stlar...
# 
# DASTURCHI @MrGayratov Kanal : @KingsOfPy

"""
api_id = 25682712  # API ID KIRITING
api_hash = 'fe8bad0e757a156cfdab01142b505e1d' # API HASH KIRITING
app = Client(
    "my_bot",
    api_id=api_id,
    api_hash=api_hash
)

app.start()
# DASTURCHI @MrGayratov Kanal : @KingsOfPy
while True:
    from_chat_id = -1783145194 # A'zo tanlamoqchi bolgan guruhingiz ID raqamini kiritng
    my_chat_id = -1643217918 # A'zolarni qo'shmoqchi bo'lgan guruhingiz ID raqamini kiritng
    members = [] # Foidalanuvchi idlarini ro'yxatga ko'chirish yani olish uchun
    # DASTURCHI @MrGayratov Kanal : @KingsOfPy
    for member in app.get_chat_members(from_chat_id):
        members.append(member.user.id)
    # DASTURCHI @MrGayratov Kanal : @KingsOfPy
    app.add_chat_members(chat_id=my_chat_id, user_ids=members)
# DASTURCHI @MrGayratov Kanal : @KingsOfPy
app_run()
