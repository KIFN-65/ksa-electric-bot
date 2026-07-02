import os

# Telegram Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Telegram Chat ID
CHAT_ID = os.getenv("CHAT_ID")

# مدة البحث (كل 10 دقائق)
CHECK_INTERVAL = 600

# الكلمات المفتاحية لوظائف الكهرباء
KEYWORDS = [
    "فني كهرباء",
    "فني صيانة كهربائية",
    "قوى كهربائية",
    "Electrical Technician",
    "Maintenance Electrician",
    "Industrial Electrician",
    "PLC Technician",
    "Control Technician",
    "كهربائي صناعي",
    "فني تشغيل",
    "فني لوحات كهربائية",
    "فني مرافق"
]

# وظائف الحج والعمرة
HAJJ_KEYWORDS = [
    "وظائف الحج",
    "وظائف موسمية",
    "الحج والعمرة",
    "المشاعر المقدسة",
    "موسم الحج",
    "فني كهرباء الحج",
    "تشغيل وصيانة الحج"
]

# جميع مدن المملكة
CITIES = [
    "الرياض",
    "جدة",
    "مكة",
    "المدينة",
    "ينبع",
    "الدمام",
    "الخبر",
    "الجبيل",
    "الطائف",
    "تبوك",
    "أبها",
    "جازان",
    "نجران",
    "حائل",
    "القصيم",
    "عرعر",
    "سكاكا"
]
