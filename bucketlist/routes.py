from bucketlist import api
from bucketlist.user import UserRegistration, UserLogin
from bucketlist.view import BucketlistView, BucketListItemView

api.add_resource(BucketlistView, '/bucketlists/', endpoint='add_bucketlist')
api.add_resource(BucketlistView, '/bucketlists/<int:bucketlist_id>',
                 endpoint='bucketlistview')
api.add_resource(BucketListItemView, '/bucketlists/<int:bucketlist_id>/items/',
                 endpoint='create_bucketlist_item')
api.add_resource(BucketListItemView,
                 '/bucketlists/<int:bucketlist_id>/items/<int:item_id>',
                 endpoint='UpdateDelete_bucketlist_item')
api.add_resource(UserRegistration, '/auth/register', endpoint='register')
api.add_resource(UserLogin, '/auth/login', endpoint='login')
