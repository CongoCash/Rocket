## Django-REST-Framework Missions

#### Django Model Preparations
1. Create a Django app called todo
1. Create a Django model called Todo
1. Add todo Django app to settings.py
1. The model should have the following fields:
  1. title as CharField (Required)
  1. content as TextField (Nullable)
  1. user as ForeignKey to User model (Required)
1. Create DB migrations and apply them
1. Create Django superuser called admin
1. Create ModelAdmin class for Todo and register it
1. Go to Django Admin page and create some dummy Todo items!

#### Mission A - Create a simple API View
1. Go to todo app folder and create api folder
1. Create ______init______.py and views.py Python file in api folder
1. Create TodoListAPIView class using APIView from rest_framework.views
1. Create get method that returns ```{“message”: “Hello!”}``` with HTTP 200 status
1. Add your TodoListAPIView class in Django url pattern
1. Create urls.py Python file in api folder
1. Add your TodoListAPIView class in url_pattern on urls.py Python file
  1. Set the url as r’^$’
1. Include urls.py from api folder in root urls.py Python file with r’^api/todos/’ pattern

#### Mission B - Create and change your API View to ListAPIView by the serializer for Todo Model
1. Create serializers.py Python file in api folder
1. Create a TodoSerializer class using serializers.ModelSerializer
1. Set Model to your Todo model in Meta class
1. Use TodoSerializer in your APIView
  1. Import your TodoSerializer class to api/views.py Python file
  1. Create a serializer in your APIView’s get method
  1. Initialize your serialize with Todo Queryset and many=True
    * By default, a serializer only takes one item. If we give many=True argument, the serializer automatically understands that it needs to have many items
1. Return the serializer data in your Response with HTTP 200 status

#### Mission C - Create a Detail API View
1. Create TodoDetailAPIView class
1. Add your TodoDetailAPIView in Django url pattern
1. Make sure the APIView accepts keyword argument on the url: todo_id as integer
1. Load a single Todo object from Todo Model
  * You can use ORM get method or django shortcut get_object_or_404
1. Load TodoSerializer from serializers.py into TodoDetailAPIView class
1. Add above Todo object as Serializer argument
1. Return the serializer data in your Response with HTTP 200 status

#### Mission D - Use a serializer inside a serializer for foreign keys
1. Create UserSerializer class
1. Override the user field in TodoSerializer to use UserSerializer class to represent

#### Mission E - Create a Create API View by generic CreateAPIView
1. Create TodoCreateAPIView class
1. Set serializer_class for this class

Right now, user is required for Todo model. Moreover, TodoSerializer uses UserSerializer, thus DRF API browser will be User model fields + Todo model fields. This is somewhat overwhelming to send POST request with lots of fields to do.

1. Make user field read_only so that User data will only be displayed for GET requests

However, we still need to supply User object when creating Todo model. We can override create method to implement this custom validation.

* Override create method to assign user to self.request.user for now

#### Mission F - Use more generic API views

1. ListAPIView
  * Use get_queryset method to control a queryset result
1. RetrieveUpdateAPIView
  * Use get_queryset method to pick a single object from
  * Add lookup_field to set the keyword argument for primary key in url pattern

#### Mission G - Make your List API View to display partial information
* Modify your Serializer to limit the fields to display
* You can use read_only attribute for the fields you want to hide

#### Mission H - Let one APIView return more than one Serializer data
1. Create a new Django model called TodoActivity
  1. title as CharField (Required)
  1. feedback as TextField (Nullable)
  1. Add a new foreign key to TodoActivity Model in Todo Model (Required, related_name=”todos”)
1. Create DB migrations and apply them
1. Create ModelAdmin class for TodoActivity and register it
1. Go to Django Admin page and create some dummy TodoActivity items with Todo attached!
1. Create a serializer class called TodoActivitySerializer
1. Exclude a foreign key to TodoActivity in TodoSerializer class
1. Use a barebone APIView class to create TodoActivityDetailAPIView class.
1. Get a single TodoActivity object.
1. Store the TodoActivity object’s Todo objects into a variable. Now we have two querysets.
1. Serialize each queryset with its own serializer class.
1. Create a dictionary to store each serializer data.
1. Return Response object with above dictionary and HTTP 200 status.

#### Mission I - API Error handling and returning an error JSON
Instead of assigning to current user when creating Todo item, let's make TodoCreateAPIView class to accept User ID from POST request and assign it

* Add a if statement to check 'user_id' from request.data.
* If 'user_id' is not supplied, then create Response object with ```{"error": "user_id is required."}``` and HTTP 400 error
* If there is no User with the given user_id, then create a Response with ```{"error": "Not Found"}``` and HTTP 404 error
* If we found a User object, then pass it to serializer.save method.

#### Mission J - Advanced Serializer features
1. Make TodoSerializer object in TodoCreateAPIView to create Todo item with partial POST data
  * partial as Serializer parameter
1. Customize some of TodoSerializer fields with any of below
  * max_length
  * min_value
  * max_value
  * input_formats
  * choices
  * read_only
  * write_only
  * required
  * default
  * initial
  * allow_blank
  * allow_null
1. Let's add a serializer field validation for title
  * If title is "NO", then throw a ValidationError

#### Mission K - SerializerMethodField
1. Create a SerializerMethodField in TodoSerializer that returns "This Todo rocks!"

#### Mission L - Paginations
* Add paginate_by, paginate_size arguments to ListAPIView

#### Mission M - Authentication and Permissions
* SessionAuthentication & TokenAutentication setup to Django settings.py
* Use AllowAny permission in ListAPIView
* Use IsAuthenticated permission in CreateAPIView

#### Lab Mission - Restaurant Menu
Your assignment is to build an API application that deals with the restaurant menu. The application will be consist of MenuItem, Ingredient, and Review models. The API application will list, show a single item, and create a new item for each model.

1. Create a new Django app called restaurant_menu
1. Create new Django models for restaurant_menu app: MenuItem, Ingredient, and Review models.
1. Use the best judgement on coming up fields for each model.
  1. The followings must be included:
    1. Ingredient model would have a foreign key to MenuItem model (1-to-m)
    1. MenuItem model would have a foreign key to Review model (1-to-m)
1. Add restaurant_menu Django app to settings.py
1. Create DB migrations and apply them
1. Create each ModelAdmin class for your models and register them
1. Go to Django Admin page and create some dummy items!
1. Create serializer classes for each model
  * For foreign key relationships, use nested serializer techniques
1. Create List API Views for each model
  * Demonstrate ListAPIView in barebone APIView and generic ListAPIView
1. Create Detail API Views for each model
  * Demonstrate DetailAPIView in barebone APIView and generic RetrieveAPIView
1. Create Create API View for each model
  * Demonstrate CreateAPIView in barebone APIView and generic CreateAPIView
1. Bonus: Create Update API Views for each model
  * Demonstrate UpdateAPIView in EITHER barebone APIView or generic RetrieveUpdateAPIView
1. Bonus: Create Delete API Views for each model
  * Demonstrate DeleteAPIView in EITHER barebone APIView or generic RetrieveDestroyAPIView
1. Bonus: Add Pagination to one of your ListAPIView
1. Bonus: Add Token Authentication and let one of your List API View to be allowed for all request while one of your Create API View needs authentication.
