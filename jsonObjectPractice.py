
# log =   {
#   "logs": [
#     {"user": "alice", "action": "login"},
#     {"user": "bob", "action": "logout"},
#     {"user": "alice", "action": "upload"},
#     {"user": "alice", "action": "logout"},
#     {"user": "bob", "action": "login"}
#   ]
# }

# # returns a hashmap with user and num of actions
# def getUserAction(log):
#     user_actions = {}
#     for user in log["logs"]:
#         user_actions[user["user"]] = user_actions.get(user["user"],0)+1

#     return user_actions
# print(getUserAction(log))

# data = {"events":[{"type":"ERROR","service":"auth"},{"type":"INFO","service":"payments"},{"type":"ERROR","service":"auth"},{"type":"ERROR","service":"payments"},{"type":"WARN","service":"auth"}]}

# def countServiceErrors(data):
#     result = {}
#     for events in data["events"]:
#         service = events["service"]
#         type = events["type"]
#         if type == "ERROR":
#             result[service] = result.get(service,0)+1
    
#     return result

# print(countServiceErrors(data))

# data_2 = {
#   "orders": [
#     {"user": "u1", "total": 12.5, "status": "PAID"},
#     {"user": "u2", "total": 10.0, "status": "CANCELLED"},
#     {"user": "u1", "total": 7.5,  "status": "PAID"},
#     {"user": "u3", "total": 20.0, "status": "PAID"}
#   ]
# }

# def returnTotalPaid(data_2):
#     total_paid = {}

#     for orders in data_2["orders"]:
#         user = orders["user"]
#         status = orders["status"]
#         total = orders["total"]

#         if status == "PAID":
#             total_paid[user] = total_paid.get(user,0)+total
        
#     return total_paid

# print(returnTotalPaid(data_2))


data_3 = {
  "users": [
    {"id": "u1", "transactions": [{"amount": 10}, {"amount": 40}, {"amount": 5}]},
    {"id": "u2", "transactions": [{"amount": 25}]},
    {"id": "u3", "transactions": []},
    {"id": "u4", "transactions": [{"amount": 15}, {"amount": 15}]}
  ]
}


def returnHighestTotalTransactionAmount(data_3):
    users = data_3["users"]
    #set base case
    highest_num = 0
    highest_usr = ""
    for id in users:
        total = 0
        for transaction in id["transactions"]:
            total += transaction["amount"]
        if total > highest_num:
            highest_usr = id["id"]
            highest_num = total
        elif total == highest_num and highest_num != 0:
            if id["id"] < highest_usr:
                highest_usr = id["id"]
        

    
    return highest_usr
print(returnHighestTotalTransactionAmount(data_3))