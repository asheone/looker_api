# Open the list of users from the csv file
from numpy import genfromtxt
import pandas as pd
from looker_sdk import client, models, error

file = genfromtxt("user_to_disable_ids.csv")

# Create a list of user_ids
user_ids = []
for row in file:
    user_ids.append(int(row))
print(user_ids)

# client calls will now automatically authenticate using the
# api3credentials specified in 'looker.ini'
sdk = client.setup("looker.ini")
looker_api_user = sdk.me()

# Updating the user: change first_name and explicitly nullify
update_user = models.WriteUser(is_disabled=True)  # do not use None

# update the user with the client

count = 0
for user in user_ids:
    count += 1
    updated_user = sdk.update_user(user_id=user, body=update_user)
    print(
        count,
        f"Disabled user:({user}) {updated_user.display_name} "
        f"locale:({updated_user.locale})",
        f"email:({updated_user.email})"
    )
