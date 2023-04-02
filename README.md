# django-feed-poc
A POC for django notifications, feed with OOB solutions like django-notifications-hq, django-activity-stream, self built solutions and send email etc.,

## users
user1/2/3/4/5 - djangouser (regular users)
admin - admin - (adminuser)
## Teams
|Team|admin|members|
|---|---|---|
|admin|admin|admin <br> All|
|user1|user1|user1 <br> user2 <br> user3|
|user4|user4|user4 <br> user5|


# TODO
- adding resources sends alerts to team leader and user
- removing resources sends notification to user
- adding users to teams sends notifications to the team and user
- removing users from team will send notification to the user and team leader
- read notifications