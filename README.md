# django-feed-poc
A POC for django notifications, feed with OOB solutions like django-notifications-hq, django-activity-stream, self built solutions and send email etc.,

# prerequisistes
- create config.py in the same directory as manage.py
- populate the following values in it
    - PG_NAME=''
    - PG_USER=''
    - PG_PASSWORD=''
    - PG_HOST=''
    - PG_PORT=''
    - EMAIL_HOST = ''
    - EMAIL_HOST_USER = ''
    - EMAIL_PORT = 587 # whatever that is relevant in your case
    - EMAIL_USE_TLS = False # or True
## users
user1/2/3/4/5 - djangouser (regular users)
admin - admin - (adminuser)
django - staffuser - (staff user)
## Teams
- perform this from admin panel <br>

|Team |admin  | members|
| --- | --- | --- |
|admin|admin|admin,All|
|user1|user1|user1,user2,user3|
|user4|user4|user4,user5|

## Test
- Bell icon on navbar is red when there are unread notification
- Bell icon on navbar is outline black when there are no unread notification
- When a user is logged in, he gets a notification
- when a user is logged out, he gets a notification
- When a user provisions a resource (vm, k8s, gpu, etc.,) he and his team admin/leader gets a notification
- When a user deletes a resource he gets a notification
- Ajax acknoledgement of notifications
- team leader gets notification when his engineeers provision/de provision something
- team leader can broadcast notification or email

