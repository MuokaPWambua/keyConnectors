users = [{"id": 0,"name": "Hero"}, {"id": 1,"name": "Dunn"}, {"id": 2,"name": "Sue"},{"id": 3,"name": "Chi"},\
    {"id":4,"name": "Thor"}, {"id": 5,"name": "Clive"}, {"id": 6,"name": "Hicks"}, {"id": 7, "name": "Devin"},\
    {"id": 8,"name": "Kate"}, {"id": 9,"name": "Klein"}]

friendships =[(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)] 

# adding a group of friends to each user

for user in users:
    user['friends'] = [] 

#populating the friends list of user using friendships data

for i, j in friendships:
    users[i]['friends'].append(users[j]) #add i as a friend of j
    users[j]['friends'].append(users[i]) #add j as a friend of i


#total number of connections/friends

def number_of_friends(user):
    return len(user['friends'])

total_connections = sum(number_of_friends(user) for user in users)

print(f'total connections: {total_connections}')

#average connections

average_connections = total_connections/ len(users)

print(f'average connections: {average_connections}')

# sort user with most friends to least friends

num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]

sorted_user_by_friend = sorted(num_friends_by_id, key=lambda(user_id,num_friends):num_friends, reverse=True)

prints(f'sorted friends by most to least: {sorted_user_by_friend}')


