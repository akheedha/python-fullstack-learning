# Boolean variables
has_account = True
email_verified = False

# Basic login check
can_login = has_account and email_verified

# Email validation
email = "g@example.com"
is_email_valid = "@" in email

# Age validation
user_age = 17
is_age_valid = user_age >= 18

# Final login condition
can_login_final = has_account and email_verified and is_email_valid and is_age_valid

# Print results
print("Can login (basic):", can_login)
print("Is email valid:", is_email_valid)
print("Is age valid:", is_age_valid)
print("Can login (final):", can_login_final)

# Identity operator check
print("Has account is True:", has_account is True)