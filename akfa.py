import os
import time


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


clear_screen()

# 1-BOSQICH: Ism
print("\033[96m========================================\033[0m")
print("🤖 TIZIM: Xush kelibsiz!")
print(
    "\033[93m🤖 TIZIM: Siz hali ham ism kiritadigan joyni qidiryapsizmi O_O ? Pastga qarang!\033[0m"
)
print("\033[96m========================================\033[0m")

ism = input("\033[92m👉 Ismingizni kiriting: \033[0m")

clear_screen()
time.sleep(0.4)

print("\033[96m========================================\033[0m")
print(
    f"😎 Ko'rdingizmi, \033[92m{ism}\033[0m? Siz hali ham ism kiritadigan joyni qidiryapsizmi O_O ? Tepaga qarang!"
)
print(
    "\033[91m⚠️ ALGORITM: Foydalanuvchi muvaffaqiyatli chalg'itildi va ekrani o'chirildi! 💀🤣🤣\033[0m"
)
print("\033[96m========================================\033[0m\n")

# 2-BOSQICH: Email
print("\033[95m🤫 Balki email ham kiritarsiz 👀?")
print(
    "chunki biz sizni shuncha botlar yoki nomsiz odamlar ichidan topib xabar yuborishimiz kerak..."
)
print("bu sir, hech kimga aytmang 🫣\033[0m")
print("\033[93m (Yana qidirmasligingiz uchun quti ichida qilayapmiz)\033[0m")

print("\033[94m┌────────────────────────────────────────┐\033[0m")
email = input("\033[94m│ 👉 Emailingizni kiriting: \033[0m")
print("\033[94m└────────────────────────────────────────┘\033[0m")

clear_screen()
time.sleep(0.4)

print("\033[94m========================================\033[0m")
print(f"📩 Qabul qilingan email: \033[92m{email}\033[0m")
print(
    "Ko'rdingizmi? Siz hali ham email kiritadigan joyni qidiryapsizmi O_O ? Tepaga qarang! 💀🤣🤣"
)
print("\033[94m========================================\033[0m")

print("\n\033[96m🤖 TIZIM: Foydalanuvchi muvaffaqiyatli chalg'itildi va ekrani o'chirildi! 💀🤣🤣\033[0m")
print(" barchasi uchun uzr shunchaki hazil edi")
print(" sizni chalg'itish uchun shunchaki o'yin qildik")
# Terminalda odamni kuttirib, nuqtalarni sekin-asta chiqarish:
for i in range(3):
    time.sleep(1.2)
    print(".\n" * 10)  # Ekranni sekin pastga suradi

time.sleep(1.5)
print("... nafas oldik ana 🤣🤣🤣")
print("👉 Yaxshi, nafas olib oldik! Endi bo'limni tanlang:")
print("========================================\033[0m")

print("1️⃣ 1-bo'lim: Akfa romlari shablonlari")
print(
    "2️⃣ 2-bo'lim: Brendlar va Akfaga ishlatiladigan materiallar "
    "\n   (Agar topa olsangiz sizni tabriklaymiz, siz Akfa dizaynerisiz! 😎)"
)
print("3️⃣ 3-bo'lim: Akfa dizaynerlarining ishlari (Showcase)")
print("4️⃣ 4-bo'lim: Dizaynerlar ishlari bo'yicha fikr bildirish")
print("5️⃣ 5-bo'lim: Ish jarayonlaridan olingan videolar")
print(
    "6️⃣ 6-bo'lim: Akfa dizaynerlari ishlaridan olingan axlatlar uyumi 🗑️"
    "\n   (Bu bo'limni ko'rish uchun sizda maxsus ruxsat bo'lishi kerak!)"
)
print(
    "\033[90m\n(Albatta bu barchasi hazil... Agar akfachi bo'lmasangiz, bu yerda nima qilyapsiz? 🫢)\033[0m"
)
print("\033[96m========================================\033[0m")

tanlov = input("\033[92m👉 Bo'lim raqamini kiriting (1-6): \033[0m")

time.sleep(0.5)

# Tanlov mantiqi (Backend API routerlariga tayyorgarlik)
match tanlov:
    case "1":
        print("\n📐 Shablonlar yuklanmoqda... (/api/v1/templates)")
    case "2":
        print("\n🔍 Materiallar qidirilmoqda... Topa olsangiz baraka!)")
    case "3":
        print("\n🎨 Dizaynerlar portfoliosi ochilmoqda...")
    case "4":
        print("\n💬 Fikr-mulohazalar bo'limi...")
    case "5":
        print("\n🎥 Videolar ijro etilmoqda...")
    case "6":
        print("\n🗑️ Axlatxona ochildi... Dizaynerlar xatolari to'planmoqda! 💀")
    case _:
        print("\n⚠️ Noto'g'ri bo'lim tanlandi! Siz rostdan ham Akfachi emassiz... 😂")