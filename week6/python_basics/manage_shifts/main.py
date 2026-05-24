from cli import BaseMenu
from data import Unit


def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
    unit = Unit()
    base_menu = BaseMenu(unit)
    base_menu.run()


if __name__ == "__main__":
    main()
