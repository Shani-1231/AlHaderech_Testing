# פרויקט אוטומציה עם Selenium ו-Python 🧪🕸️

זהו פרויקט בדיקות אוטומטיות עבור אתר מסחר, כחלק מקורס אוטומציה.

הפרויקט כולל:
- בדיקות התחברות (חיוביות ושליליות)
- בדיקות עמוד הבית, חיפוש, ו"אזור אישי"
- שימוש ב־ Page Object Model (כולל קלאס בסיס)
- שימוש במרקרים להרצות ממוקדות
- תיוגים ל־Allure (Suite, Story, Severity)
- צילום מסך אוטומטי כאשר טסט נכשל

---

## 🚀 הרצת הטסטים

יש לוודא שהחבילות הדרושות מותקנות:

```bash
pip install -r requirements.txt
```

### הרצה רגילה:
```bash
pytest
```

### הרצת טסטים לפי קובץ:
```bash
pytest tests/test_login.py
```

### הרצה לפי מרקר:
```bash
pytest -m search
```

### הרצה עם Allure:
```bash
pytest --alluredir=reports/
allure serve reports/
```

---

## 🔐 קובץ התחברות – `config.json`

הפרויקט כולל טסטים הדורשים פרטי התחברות (username + password).  
**הקובץ אינו כלול בריפוזיטורי מטעמי אבטחה.**

יש ליצור קובץ חדש בשם `config.json` לפי הדוגמה:

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
├── pages/                   # קלאסי Page Object לכל עמוד
│   ├── base_page.py
│   ├── login_page.py
│   ├── home_page.py
│   ├── search.py
│   └── my_account_page.py
│
├── tests/                   # קבצי טסטים + conftest
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_homepage.py
│   ├── test_search.py
│   └── test_my_account.py
│
├── config.json              # קובץ פרטי (לא עולה ל-Git)
├── config.json.example      # קובץ לדוגמה
├── requirements.txt         # כל התלויות של הפרויקט
├── pytest.ini               # הגדרות מרקרים והרצות
├── reports/                 # דוחות Allure (נמצא ב-.gitignore)
├── .gitignore               # קבצים שיש להחריג מגיט
└── README.md                # תיעוד הפרויקט
```

---

## 🧩 טכנולוגיות בשימוש

- Python 3.10+
- Selenium
- Pytest
- Allure
- Page Object Model

---

## 📌 הערות

- הסיסמאות והנתונים האישיים מאוחסנים בקובץ חיצוני (`config.json`) שלא עולה ל־GitHub.
- הטסטים נבדקו על דפדפן Google Chrome.
- חלק ממקרי הבדיקה במסמך STD מכוסים כחלק מטסטים רחבים יותר – לכן ייתכנו פערים במספור.
- תיקיית `reports/` (דוחות Allure) קיימת אך לא נכללת ב־Git לצורך ניקיון והימנעות מקבצים זמניים.

---

בהצלחה! 😊