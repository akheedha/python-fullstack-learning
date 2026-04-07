# Boolean variables
is_logged_in = True
is_subscribed = False

# Credit values
user_credits = 100
max_credits = 200
min_credits = 50

# Check valid credit range (>= min, <= max, and not equal to min)
credits_valid = (user_credits >= min_credits and user_credits <= max_credits) and (user_credits != min_credits)

# Bonus eligibility (either subscribed OR credits > min_credits)
bonus_eligible = is_subscribed or (user_credits > min_credits)

# Modify user_credits step by step
user_credits += 50   # 150
user_credits -= 20   # 130
user_credits *= 2    # 260
user_credits %= 150  # 110

# Power calculation
power_result = user_credits ** 2

# Full access check
full_access = is_logged_in and is_subscribed

# Identity operator check
is_true_login = (is_logged_in is True)

# Operator precedence check
access_result = is_logged_in or is_subscribed and False

# Print results
print("is_logged_in:", is_logged_in)
print("is_subscribed:", is_subscribed)
print("credits_valid:", credits_valid)
print("bonus_eligible:", bonus_eligible)
print("user_credits:", user_credits)
print("power_result:", power_result)
print("full_access:", full_access)
print("is_true_login:", is_true_login)
print("access_result:", access_result)