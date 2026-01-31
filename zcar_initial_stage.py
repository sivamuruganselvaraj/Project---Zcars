#---------------------------------Login Function -------------------------------
def login():
    print("Welcome to Z~Cars Login")
    
    #Existing user
    users = {
        "siva": "print",
        "aathi": "over"
    }
    #user
    username = input("Enter Your Username: ")

    if username not in users:
        print(f" User '{username}' not found.")
        choice = input("Do you want to create a new account? (yes/no): ").strip().lower()

        if choice == "yes":
            new_pass = input("Create a password: ")
            users[username] = new_pass
            print(f" Account created successfully for '{username}'. Please log in now.")
        else:
            print("Login cancelled.")
            return False

    #Login
    password = input("Type Your Password: ")

    if users.get(username) == password:
        print("\n Thanks for choosing Z~Cars!\n")
        return True
    else:
        print("\n✕ T R Y  A G A I N\n")
        return False


#-------------------------------Display Car Listings-----------------------------
def display_cars(car_type, car_list):
    print(f"\nAvailable {car_type.capitalize()} Cars:\n")
    for car in car_list:
        print(f"{car['name'].title()} - {car['year']} Model - {car['km']} km Driven - {car['price']}")
    print()


#------------------------------Wishlist Function -------------------------------
def wishlist():
    selected = input("Enter the car name you liked to add to wishlist: ").lower()

    # Build valid list from all car categories
    all_models = [car["name"].lower() for type_list in cars.values() for car in type_list]

    if selected in all_models:
        name = input("Your Name: ")
        contact = input("Enter Your Contact Number: ")
        

        print(f"\nHi {name}, Thanks for reaching Z~Cars!")
        print("✓ You are our valuable client.")
        print("It seems like you have shown interest in our car.")
        print("📞 Our sales executive will connect with you shortly — please keep your phone handy for a quick call.\n")
    else:
        print("\n The car you're looking for is not currently listed.")
        print("We'll notify you if it becomes available!\n")


#-------------------------------Car Listings Data--------------------------------
cars = {
    "hatchback": [
        {"name": "swift", "year": 2019, "km": "14,537", "price": "₹4,25,000"},
        {"name": "datsun", "year": 2016, "km": "27,000", "price": "₹3,10,000"},
        {"name": "hyundai", "year": 2022, "km": "8,000", "price": "₹5,20,000"},
        {"name": "chevrolet", "year": 2014, "km": "19,875", "price": "₹4,73,000"},
        {"name": "baleno", "year": 2020, "km": "18,430", "price": "₹3,80,000"}
    ],
    "sedan": [
        {"name": "maruti suzuki ciaz", "year": 2019, "km": "14,537", "price": "₹4,25,000"},
        {"name": "skoda slavia", "year": 2016, "km": "27,000", "price": "₹3,10,000"},
        {"name": "hyundai verna", "year": 2022, "km": "8,000", "price": "₹5,20,000"},
        {"name": "honda city", "year": 2014, "km": "19,875", "price": "₹4,73,000"},
        {"name": "maruti suzuki swift dzire", "year": 2020, "km": "18,430", "price": "₹3,80,000"}
    ],
    "suv": [
        {"name": "mahindra scorpio", "year": 2019, "km": "14,537", "price": "₹4,25,000"},
        {"name": "skoda kushaq", "year": 2016, "km": "27,000", "price": "₹3,10,000"},
        {"name": "hyundai alcazar", "year": 2022, "km": "8,000", "price": "₹5,20,000"},
        {"name": "renault duster", "year": 2014, "km": "19,875", "price": "₹4,73,000"},
        {"name": "maruti suzuki fronx", "year": 2020, "km": "18,430", "price": "₹3,80,000"}
    ],
    "mpv": [
        {"name": "toyota vellfire", "year": 2019, "km": "14,537", "price": "₹4,25,000"},
        {"name": "mahindra marazzo", "year": 2016, "km": "27,000", "price": "₹3,10,000"}
    ],
    "jeep": [
        {"name": "mahindra thar", "year": 2019, "km": "14,537", "price": "₹4,25,000"},
        {"name": "jeep compass", "year": 2016, "km": "27,000", "price": "₹3,10,000"},
        {"name": "mahindra thar roxx", "year": 2022, "km": "8,000", "price": "₹5,20,000"}
    ],
    "electric": [
        {"name": "tata curvv ev", "year": 2023, "km": "14,537", "price": "₹4,25,000"},
        {"name": "mahindra be 6e", "year": 2025, "km": "27,000", "price": "₹3,10,000"},
        {"name": "tesla cyber truck", "year": 2024, "km": "8,000", "price": "₹5,20,000"},
        {"name": "mahindra 9e", "year": 2024, "km": "19,875", "price": "₹4,73,000"},
        {"name": "mg hector ev", "year": 2023, "km": "18,430", "price": "₹3,80,000"}
    ]
}


#----------------------------------Main Flow -----------------------------------
def start_flow():
    print("🚘 Welcome to Z~Cars")
    print("We consider you a valuable customer.")
    print("Please let us know why you're here.\n")

    choice = input("Type 'buy' to Buy a Car or 'sell' to Sell your Car: ").lower()

    if choice == "buy":
        car_type = input("What kind of car are you looking for? [eg: hatchback, sedan, suv, mpv, jeep, electric...]:").lower()

        if car_type in cars:
            display_cars(car_type, cars[car_type])
            wishlist()
        else:
            print("✕ We currently don’t have listings for that type.")
        return "buy"

    elif choice == "sell":
        sellname = input("Name: ")
        mobile = input("Please enter your contact number: ")
        brand = input("Your Car Brand: ")
        model = input("Your Car Model: ")
        year = input("Model Year: ")
        variant = input("Enter Variant: ")

        print(f"\nHi {sellname}, Thanks for reaching Z~CARS.")
        print("You are our valuable client.")
        print("It seems like you have shown interest in selling your car.")
        print(f"\nCar Details Collected: {brand.title()} {model.title()} {year} {variant}")
        print("📞 Our Q/C executive will contact you shortly. Kindly be ready to pick up the call.\n")
        return "sell"

    else:
        print("✕ Invalid option. Please enter 'buy' or 'sell'.\n")
        return None


#-------------------------------Advance Action Logic-------------------------------
def action(callback):
    def inner():
        print("\n⇌ IF YOU WANT TO SCHEDULE A TEST DRIVE, TYPE [YES]:")
        response = input().lower()
        if response == "yes":
            callback()
        elif response == "no":
            print("We’d love to get you behind the wheel! Contact us anytime and let’s make it happen!")
        else:
            print("✕ Invalid input. Please type 'yes' or 'no'.")
    return inner


def test_drive():
    print(" Test DRIVE Scheduled!")


#--------------------------------Entry Point--------------------------------------
if __name__ == "__main__":
    if login():
        flow_choice = start_flow()
        if flow_choice == "buy":  # ✅ Only run this if buying
            follow_up = action(test_drive)
            follow_up()

