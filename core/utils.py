from datetime import datetime
import random

def generate_unique_id():
    now = datetime.now()

    # random 4-digit number
    random_number = random.randint(1000, 9999)
    # datetime to create a base unique ID
    unique_base = now.strftime("%Y%m%d%H%M%S%f")

    # Combine the datetime string and random number to form the unique ID
    unique_id = f"{unique_base}{random_number}"

    return unique_id
