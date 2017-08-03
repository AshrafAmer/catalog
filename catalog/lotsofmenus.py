from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem, User


#engine = create_engine('sqlite:///restaurantmenuwithusers.db')
engine = create_engine('postgresql://catalog:11111@localhost/catalog')

Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)


session = DBSession()


# Create dummy user
User1 = User(
    name="Robo Barista",
    email="tinnyTim@udacity.com",
    picture='https://pbs.twimg.com/profile_images/'\
    '2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Menu for UrbanBurger
restaurant1 = Restaurant(user_id=1, name="Urban Burger")

session.add(restaurant1)
session.commit()

menuItem2 = MenuItem(
    user_id=1, name="Veggie Burger",
    description="Juicy grilled veggie patty with tomato mayo and lettuce",
    price="$7.50", course="Entree",
    restaurant=restaurant1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(user_id=1,
                     name="French Fries",
                     description="with garlic and parmesan",
                     price="$2.99",
                     course="Appetizer",
                     restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(
    user_id=1,
    name="Chicken Burger",
    description="Juicy grilled chicken patty with tomato mayo..",
    price="$5.50",
    course="Entree",
    restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1,
                     name="Chocolate Cake",
                     description="fresh baked and served with ice cream",
                     price="$3.99",
                     course="Dessert",
                     restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1,
                     name="Sirloin Burger",
                     description="Made with grade A beef",
                     price="$7.99",
                     course="Entree",
                     restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1,
                     name="Root Beer",
                     description="16oz of refreshing goodness",
                     price="$1.99",
                     course="Beverage",
                     restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1,
                     name="Iced Tea",
                     description="with Lemon",
                     price="$.99",
                     course="Beverage",
                     restaurant=restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1,
                     name="Grilled Cheese Sandwich",
                     description="On texas toast with American Cheese",
                     price="$3.49",
                     course="Entree",
                     restaurant=restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1,
                     name="Veggie Burger",
                     description="Made with freshest of ingredients..",
                     price="$5.99",
                     course="Entree",
                     restaurant=restaurant1)

session.add(menuItem8)
session.commit()


# Menu for Super Stir Fry
restaurant2 = Restaurant(user_id=1, name="Super Stir Fry")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(user_id=1,
                     name="Chicken Stir Fry",
                     description="With your choice of noodles vegetables",
                     price="$7.99",
                     course="Entree",
                     restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1,
                     name="Peking Duck",
                     description=" A famous duck dish from Beijing[1]",
                     price="$25",
                     course="Entree",
                     restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(
    user_id=1,
    name="Spicy Tuna Roll",
    description="Seared rare ahi, avocado, edamame,...",
    price="15",
    course="Entree",
    restaurant=restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(
    user_id=1,
    name="Nepali Momo ",
    description="Steamed dumplings made with vegetables, spices and meat. ",
    price="12",
    course="Entree",
    restaurant=restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(
    user_id=1,
    name="Beef Noodle Soup",
    description="A Chinese noodle soup made of stewed or red braised beef.",
    price="14",
    course="Entree",
    restaurant=restaurant2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(
    user_id=1, name="Ramen",
    description="a Japanese noodle soup dish.",
    price="12",
    course="Entree",
    restaurant=restaurant2)


session.add(menuItem6)
session.commit()


# Menu for Panda Garden
restaurant1 = Restaurant(user_id=1, name="Panda Garden")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(
    user_id=1, name="Pho",
    description="a Vietnamese noodle soup consisting of...",
    price="$8.99",
    course="Entree",
    restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(
    user_id=1,
    name="Chinese Dumplings",
    description="a common Chinese dumpling which generally consists of meat.",
    price="$6.99",
    course="Appetizer",
    restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(
    user_id=1,
    name="Gyoza",
    description="light seasoning of Japanese gyoza with salt and soy sauce.",
    price="$9.95",
    course="Entree",
    restaurant=restaurant1)


session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(
    user_id=1,
    name="Stinky Tofu",
    description="Taiwanese dish, deep fried fermented tofu served with..",
    price="$6.99",
    course="Entree",
    restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(user_id=1,
                     name="Veggie Burger",
                     description="Juicy grilled veggie patty with tomato..",
                     price="$9.50",
                     course="Entree",
                     restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Thyme for that
restaurant1 = Restaurant(user_id=1, name="Thyme for That Vegetarian Cuisine ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(
    user_id=1,
    name="Tres Leches Cake",
    description="Rich, luscious sponge cake soaked in sweet milk.",
    price="$2.99",
    course="Dessert",
    restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(
    user_id=1,
    name="Mushroom risotto",
    description="Portabello mushrooms in a creamy risotto",
    price="$5.99",
    course="Entree",
    restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(
    user_id=1,
    name="Honey Boba Shaved Snow",
    description="Milk snow layered with honey boba",
    price="$4.50",
    course="Dessert",
    restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(
    user_id=1,
    name="Cauliflower Manchurian",
    description="Golden fried cauliflower florets in a midly spiced soya,...",
    price="$6.95",
    course="Appetizer",
    restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1,
                     name="Aloo Gobi Burrito",
                     description="Vegan goodness. Burrito filled with rice,.",
                     price="$7.95",
                     course="Entree",
                     restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem2 = MenuItem(
    user_id=1,
    name="Veggie Burger",
    description="Juicy grilled veggie patty with tomato mayo and lettuce",
    price="$6.80",
    course="Entree",
    restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Tony's Bistro
restaurant1 = Restaurant(user_id=1, name="Tony\'s Bistro ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(
    user_id=1, name="Shellfish Tower",
    description="Lobster, shrimp, sea snails, crawfish, stacked into tower",
    price="$13.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(
    user_id=1, name="Chicken and Rice", description="Chicken... and rice",
    price="$4.95", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(
    user_id=1, name="Mom's Spaghetti",
    description="Spaghetti with some incredible tomato",
    price="$6.95", course="Entree", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(
    user_id=1,
    name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
    description="Milk, cream, salt", price="$3.95",
    course="Dessert", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(
    user_id=1, name="Tonkatsu Ramen",
    description="Noodles in a delicious pork-based broth with egg",
    price="$7.95", course="Entree", restaurant=restaurant1)

session.add(menuItem5)
session.commit()


# Menu for Andala's
restaurant1 = Restaurant(user_id=1, name="Andala\'s")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(
    user_id=1, name="Lamb Curry",
    description="Slow cook that thang in a pool of tomatoes..",
    price="$9.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Chicken Marsala",
                     description="Chicken cooked in Marsala wine sauce ...",
                     price="$7.95", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Potstickers",
                     description="Delicious chicken & veggies encapsulated..",
                     price="$6.50", course="Appetizer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Nigiri Sampler",
                     description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                     price="$6.75", course="Appetizer", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Veggie Burger",
                     description="Juicy grilled veggie patty with tomato ...",
                     price="$7.00", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Auntie Ann's
restaurant1 = Restaurant(user_id=1, name="Auntie Ann\'s Diner' ")

session.add(restaurant1)
session.commit()

menuItem9 = MenuItem(user_id=1, name="Chicken Fried Steak",
                     description="Fresh battered sirloin steak fried ",
                     price="$8.99", course="Entree", restaurant=restaurant1)

session.add(menuItem9)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Boysenberry Sorbet",
                     description="An unsettlingly huge amount of ripe berries",
                     price="$2.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(
    user_id=1, name="Broiled salmon",
    description="Salmon fillet marinated with fresh herbs ...",
    price="$10.95", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Morels on toast (seasonal)",
                     description="Wild morel mushrooms fried in butter",
                     price="$7.50", course="Appetizer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Tandoori Chicken",
                     description="Chicken marinated in yoghurt & seasoned.",
                     price="$8.95", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Veggie Burger",
                     description="Juicy grilled veggie patty with tomato ...",
                     price="$9.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem10 = MenuItem(user_id=1, name="Spinach Ice Cream",
                      description="vanilla ice cream made with organic ...",
                      price="$1.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem10)
session.commit()


# Menu for Cocina Y Amor
restaurant1 = Restaurant(user_id=1, name="Cocina Y Amor ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Super Burrito Al Pastor",
                     description="Marinated Pork, Rice, Beans, Avocado",
                     price="$5.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Cachapa",
                     description="Golden brown, corn-based Venezuelan pancake",
                     price="$7.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


restaurant1 = Restaurant(user_id=1, name="State Bird Provisions")
session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Chantrelle Toast",
                     description="Crispy Toast with Sesame Seeds slathered",
                     price="$5.95", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Guanciale Chawanmushi",
                     description="Japanese egg custard served hot with spicey",
                     price="$6.95", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Lemon Curd Ice Cream Sandwich",
                     description="Lemon Curd Ice Cream Sandwich ",
                     price="$4.25", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

print "added menu items!"
