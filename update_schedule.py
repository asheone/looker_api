from time import time
from looker_sdk import client
from lookerapi.rest import ApiException

start_time = time()

# client calls will now automatically authenticate using the
# api3credentials specified in 'looker.ini'
sdk = client.setup("looker.ini")
looker_api_user = sdk.me()

print("------------------------------------------")

#Provide the user id and schedule id or a list of a schedule ids
user_id = 
schedule_id = []

body = {"user_id":user_id}
for i in schedule_id:
    try:
        sdk.update_scheduled_plan(scheduled_plan_id=i, body=body)
        print(
            "Schedule ID:",
            i,
            ", Status: Done"
        )
    except ApiException as e:
        print("Exception when calling UserApi->set_user_attribute_user_value: %s\n" % e)

end_time = time()

print("------------------------------------------")
print("The process took", round(end_time - start_time, 2), "seconds to run")
