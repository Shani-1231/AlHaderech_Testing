
# פרויקט אוטומציה עם Selenium ו-Python 🧪🕸️

זהו פרויקט בדיקות אוטומטיות עבור אתר מסחר, כחלק מקורס אוטומציה.

הפרויקט כולל:
- בדיקות התחברות (חיוביות ושליליות)
- שימוש ב־Page Object Model
- הפרדה בין קוד לבדיקה לבין נתוני קלט

---

## 🚀 הרצת הטסטים

יש לוודא שכל הספריות מותקנות:

```bash
pip install -r requirements.txt
```

לאחר מכן ניתן להריץ את כלל הטסטים בעזרת:

```bash
pytest
```

או להריץ טסטים ספציפיים:

```bash
pytest tests/test_login.py
```

---

## 🔐 קובץ התחברות – `config.json`

הפרויקט כולל טסטים הדורשים פרטי התחברות (username + password).

**קובץ `config.json` אינו נמצא בריפוזיטורי מסיבות אבטחה.**  
במקום זאת, מצורף קובץ לדוגמה: `config.json.example`.

יש ליצור קובץ חדש בשם `config.json` לפי הדוגמה הבאה:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

---

## 📁 מבנה התיקיות

```plaintext
project-root/
│
├── pages/                  # מחלקות Page Object
│   └── login_page.py
│
├── tests/                  # קבצי טסטים
│   └── test_login.py
│
├── config.json             # קובץ התחברות פרטי (לא נכלל ב-Git)
├── config.json.example     # קובץ לדוגמה בלבד
├── requirements.txt        # חבילות נדרשות
├── conftest.py             # הגדרות כלליות / פיקצ'רים משותפים
└── README.md               # תיעוד הפרויקט
```

---

## 🧩 טכנולוגיות בשימוש

- Python 3.10+
- Selenium
- Pytest
- Page Object Model

---

## 📌 הערות

- כל הסיסמאות והנתונים האישיים מאוחסנים בקובץ נפרד ולא עולים ל-GitHub
- הטסטים נבדקו על דפדפן Chrome (ניתן להרחיב לדפדפנים נוספים)

---

בהצלחה! 😊
