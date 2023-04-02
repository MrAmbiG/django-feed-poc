# django-feed-poc
A POC for django notifications, feed with OOB solutions like django-notifications-hq, django-activity-stream, self built solutions and send email etc.,

## users
user1/2/3/4/5 - djangouser (regular users)
admin - admin - (adminuser)
## Teams
- perform this from admin panel
|Team|admin|members|
|---|---|---|
|admin|admin|admin <br> All|
|user1|user1|user1 <br> user2 <br> user3|
|user4|user4|user4 <br> user5|

## Test
- Bell icon on navbar is red when there are unread notification
- Bell icon on navbar is outline black when there are no unread notification
- When a user is logged in, he gets a notification
- when a user is logged out, he gets a notification
- When a user provisions a resource (vm, k8s, gpu, etc.,) he and his team admin/leader gets a notification
- When a user deletes a resource he gets a notification

