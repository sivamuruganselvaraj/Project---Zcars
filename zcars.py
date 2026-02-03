from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import sys

# ---------------------- SQL Connection ----------------------
def db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sivA@2020",
        database="zcars"
    )

# -------------------- User Management --------------------
class UserManager:
    def __init__(self):
        self.conn = db_connection()
        self.cursor = self.conn.cursor(dictionary=True)

    def login(self):
        print("\n🔐 Z~Cars User Login")
        attempts = 3

        while attempts > 0:
            username = input("Username: ").strip()

            self.cursor.execute(
                "SELECT * FROM users WHERE username = %s",
                (username,)
            )
            user = self.cursor.fetchone()

            if not user:
                choice = input("User not found. Create account? (yes/no): ").lower()
                if choice == "yes":
                    password = input("Create Password: ")
                    password_hash = generate_password_hash(password)

                    self.cursor.execute(
                        "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
                        (username, password_hash)
                    )
                    self.conn.commit()
                    print("✅ Account created. Please login again.\n")
                continue

            password = input("Password: ")
            if check_password_hash(user["password_hash"], password):
                print("✅ Login successful\n")
                return True
            else:
                attempts -= 1
                print(f"❌ Wrong password. Attempts left: {attempts}")

        print("\n🚫 Too many failed attempts. Exiting.")
        sys.exit()

# -------------------- Admin Management --------------------
class AdminManager:
    def __init__(self):
        self.conn = db_connection()
        self.cursor = self.conn.cursor(dictionary=True)

    def login(self):
        print("\n️ Admin Login")
        username = input("Admin Username: ")
        password = input("Admin Password: ")

        self.cursor.execute(
            "SELECT * FROM admin WHERE username = %s",
            (username,)
        )
        admin = self.cursor.fetchone()

        if not admin or not check_password_hash(admin["password_hash"], password):
            print("❌ Invalid admin login")
            return False
        
        print("✅ Admin login successful")
        return True

 # -------------------- Car Management --------------------
class CarManager:
    def __init__(self):
        self.conn = db_connection()
        self.cursor = self.conn.cursor(dictionary=True)

    def displaycars(self, car_type):
        self.cursor.execute(
            "SELECT * FROM cars WHERE LOWER(car_type) = %s",
            (car_type.lower(),)
        )
        cars = self.cursor.fetchall()

        if not cars:
            print("❌ No cars available in this category.")
            return []

        print(f"\n🚘 Available {car_type.upper()} Cars:")
        print("-" * 60)
        for i, car in enumerate(cars, start=1):
            print(
                f"{i}. {car['name'].title()} | {car['year']} | "
                f"{car['km']} km | ₹{car['price']}"
            )
        return cars

    def wishlist(self):
        search_name = input("\nEnter car name you liked: ").lower()

        self.cursor.execute(
            "SELECT * FROM cars WHERE LOWER(name) LIKE %s",
            (f"%{search_name}%",)
        )
        matched_cars = self.cursor.fetchall()

        if not matched_cars:
            print("❌ Car not available currently.")
            return

        selected_car = matched_cars[0]["name"]
        name = input("Your Name: ")
        phone = input("Contact Number: ")

        self.cursor.execute(
            """
            INSERT INTO enquiries (customer_name, phone, car_name, enquiry_type)
            VALUES (%s, %s, %s, 'buy')
            """,
            (name, phone, selected_car)
        )
        self.conn.commit()

        print(f"\n📞 Hi {name}, our executive will contact you shortly!")

# -------------------- Admin CRUD --------------------
class AdminCRUD:
    def __init__(self):
        self.conn = db_connection()
        self.cursor = self.conn.cursor(dictionary=True)

    # Cars CRUD
    def view_cars(self):
        self.cursor.execute("SELECT * FROM cars")
        for car in self.cursor.fetchall():
            print(car)

    def add_car(self):
        name = input("Car: ")
        car_type = input("Type: ")
        year = int(input("Year: "))
        km = int(input("KM: "))
        price = int(input("Price: "))

        self.cursor.execute(
            "INSERT INTO cars (name, car_type, year, km, price) VALUES (%s,%s,%s,%s,%s)",
            (name, car_type, year, km, price)
        )
        self.conn.commit()
        print("✅ Car added")

    def update_car_price(self):
        car_id = input("Car ID: ")
        km = int(input("New Km: "))
        price = int(input("New Price: "))

        self.cursor.execute(
            "UPDATE cars SET km=%s, price=%s WHERE id=%s",(km, price, car_id))

        self.conn.commit()
        print("✅ Car updated")

    def delete_car(self):
        car_id = input("Car ID to delete: ")
        self.cursor.execute("DELETE FROM cars WHERE id=%s", (car_id,))
        self.conn.commit()
        print("🗑️ Car as been removed from the cart")

    # Enquiries CRUD
    def view_enquiries(self):
        self.cursor.execute("SELECT * FROM enquiries")
        for enquiry in self.cursor.fetchall():
            print(enquiry)

    def delete_enquiry(self):
        enquiry_id = input("Enquiry ID to delete: ")
        self.cursor.execute("DELETE FROM enquiries WHERE id=%s", (enquiry_id,))
        self.conn.commit()
        print("🗑️ Enquiry deleted")

# -------------------- Application Controller --------------------
class ZCarsApp:
    def __init__(self):
        self.user_manager = UserManager()
        self.car_manager = CarManager()

    def start(self):
        print("\n1. Admin Login")
        print("2. User Login")
        option = input("Choose option: ")

        if option == "1":
            admin = AdminManager()
            if admin.login():
                crud = AdminCRUD()
                while True:
                    print("\n🛠️ Admin Panel")
                    print("1. View Cars")
                    print("2. Add Car")
                    print("3. Update Car Price")
                    print("4. Delete Car")
                    print("5. View Enquiries")
                    print("6. Delete Enquiry")
                    print("7. Logout")

                    ch = input("Choose: ")

                    if ch == "1":
                        crud.view_cars()
                    elif ch == "2":
                        crud.add_car()
                    elif ch == "3":
                        crud.update_car_price()
                    elif ch == "4":
                        crud.delete_car()
                    elif ch == "5":
                        crud.view_enquiries()
                    elif ch == "6":
                        crud.delete_enquiry()
                    elif ch == "7":
                        return
                    else:
                        print("Invalid option")
            return

        # ---- USER FLOW (UNCHANGED) ----
        self.user_manager.login()

        while True:
            print("\n🚗 Welcome to Z~Cars")
            print("1. Buy a Car")
            print("2. Sell a Car")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                car_type = input("Enter car type: ")
                cars = self.car_manager.displaycars(car_type)
                if cars:
                    self.car_manager.wishlist()

            elif choice == "2":
                name = input("Your Name: ")
                phone = input("Contact Number: ")
                brand = input("Brand: ")
                model = input("Model: ")
                year = input("Year: ")

                car_name = f"{brand} {model} {year}"

                conn = db_connection()
                cursor = conn.cursor()

                cursor.execute(
                    """
                    INSERT INTO enquiries (customer_name, phone, car_name, enquiry_type)
                    VALUES (%s, %s, %s, 'sell')
                    """,
                    (name, phone, car_name)
                )
                conn.commit()
                cursor.close()
                conn.close()

                print("\n📞 Our executive will contact you soon!")

            elif choice == "3":
                print("\n👋 Thank you for visiting Z~Cars")
                sys.exit()
            else:
                print("❌ Invalid option")

# -------------------- Entry Point --------------------
if __name__ == "__main__":
    app = ZCarsApp()
    app.start()



















#####creating and checking the hash value/hash password
"""
from werkzeug.security import generate_password_hash, check_password_hash
print(generate_password_hash("avis"))

hashvaluee = "scrypt:32768:8:1$1vf3xAiuaqqwwN2J$5238e6f337a2c8b67f219a31aacc4337e439878e3cf6eea5d3850b12e73ea5db84417ffa2e37409b3949a198c65a0eb15538f35859b5c3141d065856b1fcdc01"
print(check_password_hash(hashvaluee, "avis"))
"""
#####
