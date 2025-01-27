# def greet(name = 1, city = 2):
#     print(f"Hello, {name}!")
#     print(f"Welcome to {city}!")
    
# greet(city="wonderland", name="Alice")

# def life_in_weeks(age, max_age=90):
#     # Calculate the remaining years based on the given max_age
#     years_left = max_age - age
#     # Convert years to weeks
#     weeks_left = years_left * 52
#     # Output the result
#     print(f"You have {weeks_left} weeks left.")
    
# life_in_weeks(20, 100)
# life_in_weeks(30, 100)
# life_in_weeks(40, 100)

def calculate_love_score(name1, name2):
    combined_name = (name1 + name2).lower() 
    t_count = combined_name.count("t")
    r_count = combined_name.count("r")
    u_count = combined_name.count("u")
    e_count = combined_name.count("e")
    true_count = t_count + r_count + u_count + e_count
    
    l_count = combined_name.count("l")
    o_count = combined_name.count("o")
    v_count = combined_name.count("v")
    e_count = combined_name.count("e")
    love_count = l_count + o_count + v_count + e_count
    
    total_count = str(true_count) + str(love_count)
    love_score = int(total_count)
    print(love_score)

calculate_love_score("Emmanuel Ohwoka", "Ajanaku Christiana")

    
    