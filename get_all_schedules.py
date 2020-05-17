from time import time
from looker_sdk import client
from lookerapi.rest import ApiException

start_time = time()

# client calls will now automatically authenticate using the
# api3credentials specified in 'looker.ini'
sdk = client.setup("looker.ini")
looker_api_user = sdk.me()

print("------------------------------------------")

schedule_ids=[]
value = sdk.all_scheduled_plans(all_users=True)
for i in range(0, len(value)):
    try:
        schedule_ids.append(value[i].id)
        print(
            "Schedule ID:",
            value[i].id,
            ", Dashboard ID:",
            value[i].dashboard_id,
            ", Dashboard name:",
            value[i].name,
            ", User ID:",
            value[i].user_id,
            ", Schedule address:",
            value[i].scheduled_plan_destination[0].address,
        )
    except ApiException as e:
        print("Exception when calling UserApi->get_all_schedules: %s\n" % e)

end_time = time()

print("------------------------------------------")
print(schedule_ids)
print("The process took", round(end_time - start_time, 2), "seconds to run")
