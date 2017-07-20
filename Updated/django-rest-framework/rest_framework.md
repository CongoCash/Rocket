class: center, middle

# Django-REST-Framework

Silin Na, Software Engineer @ [Tivix](http://www.tivix.com)
---

class: center, middle

# Django-REST-Framework (DRF) core concepts
---

class: middle

There are 3 main concepts in DRF:

API View, Serializer, and Response
---

class: middle

### Here is how it works:

1. Django receives a HTTP request and routes it to the API View by the URL.

1. API View gets the HTTP request.

1. API View runs the Python codes we wrote to do whatever the API should be doing.

1. Then the API View returns a Response object with the results.

That simple.

---

class: middle

### Do we need to do anything for result data?

We may need to convert data from/to JSON format if any of below happens:
* We want to send data from DB (Model object or Queryset)

* The request has data for API to process.

The reason is that Django does not understand JSON as the REST client does not understand Django Model.

Therefore, we need a middle man to convert data: Serializer.

---

class: middle

### How do we create API endpoint with API View?

Do you know how to write Django views? Then you know how to write API already!

Preparing or submitting data for the API view? Using Serializer is just like using Django forms!

DRF provides both Function-based views and Class-based views for creating API monuments.

---

class: middle

### Function-based VS Class-based

For this course, we will be using Class-based view approaches.

* Object-oriented programming to code clean.

* Inheritance to feature nested logic.

* Method Resolution Order allows the request to be processed in the organized order.

---

class: center, middle

# APIView class

Let's write an API with the barebone API class.

---

class: middle

### API View example

```
class TodoListAPIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        queryset = Todo.objects.all()

        serializer = TodoSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
```

We have an API view that lists Todo items, by using the barebone APIView class. APIView class has a method for each HTTP request method
* GET

* POST

* PUT

* PATCH

* DELETE

---

class: middle

### API View example

```
class TodoListAPIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
*       queryset = Todo.objects.all()

*       serializer = TodoSerializer(queryset, many=True)

*       return Response(serializer.data, status=status.HTTP_200_OK)
```

What this view does is just displaying a list of Todo items as JSON.

1. Therefore, it loads Todo Model items first.

1. In order to convert Todo Django objects into JSON, we use TodoSerializer class to do so.

1. Lastly, TodoListAPIView returns Response object which takes the serializer's data and HTTP status code.

---

### API View example

As of result, TodoListAPIView class returns something like this:

```javascript
[
    {
        "id": 1,
        "user": {
            "id": 1,
            "username": "admin",
            "first_name": "",
            "last_name": "",
            "email": "",
            "date_joined": "2015-01-30T22:37:16.585677Z",
            "is_active": true
        },
        "title": "Test",
        "content": "",
        "created_at": "2015-01-30T22:38:54.330401Z",
        "updated_at": "2015-01-30T22:38:54.330430Z"
    }
]
```
---

class: middle

### API View example

#### What about POST request?

```
def post(self, request, format=None, *args, **kwargs):
    serializer = TodoSerializer(data=request.data)

    # OR
    # serializer = TodoSerializer(data=request.POST)

    if serializer.is_valid():
        # Serializer save method returns the instance object
        # In this case, this will return Todo object!
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

Just add another method for HTTP request type.

If you want to create PATCH request, then what method do you need to add?

---

class: center, middle

# Generic APIView classes

Easier way to create API for your Django model.

---

class: middle

### Generic APIView classes

So far, we know how to write API logic for each HTTP request.

```
def get(self, request, format=None, *args, **kwargs):
    queryset = Todo.objects.all()

    serializer = TodoSerializer(queryset, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

def post(self, request, format=None, *args, **kwargs):
    serializer = TodoSerializer(data=request.data)

    # OR
    # serializer = TodoSerializer(data=request.POST)

    if serializer.is_valid():
        # Serializer save method returns the instance object
        # In this case, this will return Todo object!
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

---

class: middle

### Generic APIView classes

Mostly, we'll be interacting with Django model all the time for our APIs.

Does that mean I have to repeat same thing for every API view with my Models?

```
def get(self, request, format=None, *args, **kwargs):
*   queryset = Todo.objects.all()

*   serializer = TodoSerializer(queryset, many=True)

*   return Response(serializer.data, status=status.HTTP_200_OK)

def post(self, request, format=None, *args, **kwargs):
*   serializer = TodoSerializer(data=request.data)

    # OR
    # serializer = TodoSerializer(data=request.POST)

    if serializer.is_valid():
        # Serializer save method returns the instance object
        # In this case, this will return Todo object!
        serializer.save()

*       return Response(serializer.data, status=status.HTTP_201_CREATED)

*   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

---

class: middle

### Generic APIView classes

.center[![Better Way](http://cdn.meme.am/instances/500x/58689093.jpg)]

---

class: middle

### Generic APIView classes

There is a set of pre-made API Views that do each certain action with your Django model by Django-REST-Framework.

All you need to do are:
* Specify your Django model

* Specify your Serializer class

Pre-baked API logic and actions are already built in these API View classes.

If you need fine tunings on the Generic API View, you can override methods to implement customized logic or validations.

---

### Generic APIView classes

Each class denotes an action on your Django Model.

* CreateAPIView

* ListAPIView

* RetrieveAPIView

* DestroyAPIView

* UpdateAPIView

* ListCreateAPIView

* RetrieveUpdateAPIView

* RetrieveDestroyAPIView

* RetrieveUpdateDestroyAPIView


---

class: middle

### Generic APIView classes

.center[![OH YEAH](http://cdn.meme.am/instances/500x/58689184.jpg)]

---

### Generic APIView classes

#### ListAPIView

This generic API View simply lists your Model items.

All it needs are:
* Your model

* Your queryset

Done!

```
class TodoGenericListAPIView(ListAPIView):
    model = Todo
    serializer_class = TodoSerializer
    # queryset = Todo.objects.all()

    def get_queryset(self):
        return Todo.objects.all()
```
---

### Generic APIView classes

#### CreateAPIView

This generic API View simply create a new item of your Model.

All it needs are:
* Your model

* Your serializer

```
class TodoGenericCreateAPIView(CreateAPIView):
    model = Todo
    serializer_class = TodoSerializer
```

If you need some custom validation or behavior on creation, you can add create method to override, add your logic, and mimic the result behavior.

```
def create(self, request, *args, **kwargs):
        ...

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
---

### Generic APIView classes

#### RetrieveUpdateDestroyAPIView

This generic API View can show/update/delete one single Model object.

All it needs are:
* Your model

* Your serializer

* A keyword argument from url pattern to be used in ORM query

```
url(r'^generics/(?P<id>\d+)/$', TodoGenericRetrieveUpdateDestroyAPIView.as_view(), name="todo-generic-single"),
```

```
class TodoGenericRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    model = Todo
    serializer_class = TodoSerializer
    lookup_field = 'id'
    # queryset = Todo.objects.all()

    def get_queryset(self):
        return Todo.objects.all()
```

---

### Generic APIView classes

#### RetrieveUpdateDestroyAPIView

```
def get(self, request, *args, **kwargs):
    # Do your things here ...

    return self.get(request, *args, **kwargs)

def patch(self, request, *args, **kwargs):
    # Do your things here ...

    return self.update(request, *args, **kwargs)

def delete(self, request, *args, **kwargs):
    # Do your things here ...

    return self.destroy(request, *args, **kwargs)
```

Again, if you need some custom validation or behavior, you can add methods to override, add your logic, and mimic the result behavior.

---

class: center, middle

# Request

Work order for API.

---

class: middle

### Request

Any API View class method will have request passed in.

This is the same request object that you used in Normal Django views.

```
*def post(self, request, format=None, *args, **kwargs):
    serializer = TodoSerializer(data=request.data)

    # OR
    # serializer = TodoSerializer(data=request.POST)

    if serializer.is_valid():
        # Serializer save method returns the instance object
        # In this case, this will return Todo object!
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

---

class: middle

### Request

Normally, you can access request.user, request.POST, request.GET, and request.FILES in your logic.

In REST-Framework's Request, it has more information; here are some:
* request.data

* request.query_params

* request.auth

---

class: middle

### Request

request.data - HTTP request data passed to API
  * POST, PUT, and PATCH data can be accessed

Ex) I send a POST request with this JSON
```javascript
{"title": "YOYOYO", "user_id": 1}
```

I can access title and user_id from request.data.

```
request.data['title'] # YOYOYO
request.data['user_id'] # 1
```

---

class: middle

### Request

request.query_params - HTTP GET request data passed to API
  * Recommended over request.GET

Ex) I send a GET request with parameters:
```javascript
"http://myawesomeapp.com/api/list/?name='Silin'&location='SF'"
```

I can access title and user_id from request.query_params.

```
request.query_params['name'] # Silin
request.query_params['location'] # SF
```

---

class: middle

### Request

request.auth - Authentication indicator

If the API request is not authenticated, this will be None. Otherwise, it would return Authentication object.
* Session
* Token

If the API request is authenticated by Token, you can access Token object by request.auth.token

---

class: center, middle

# API Browser

Convenient way to test Django APIs.

---

class: middle

### API Browser

Django-REST-Framework provides a nice Web interface to test our APIs!

Just try to visit our API view urls on the [browser](http://localhost:8000/api/todo/).

---

class: middle

### API Browser

API Browser will run Todo List API View and gives us the result automatically.

<img src="images/api_browser_1.png" width="100%"/>

---

class: middle

### API Browser

API Browser will run Todo Create API View and provides us the nice HTML POST form too!

<img src="images/api_browser_2.png" width="100%" height="575px"/>

---

class: middle

### API Browser

See? I just created a new Todo object in Django.

<img src="images/api_browser_3.png" width="100%"/>

---

class: center, middle

# Intro to Serializer

A middle man between Django and JSON.

---

### Intro to Serializer

#### Do we need a serializer in order to build API?

That is not always true. Response object can return a Python dictionary too. In fact, the serializer converts Django object into a Python dictionary.

```
class TodoListAPIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        queryset = Todo.objects.all()

        # serializer = TodoSerializer(queryset, many=True)

        # return Response(serializer.data, status=status.HTTP_200_OK)

        data = {"message": "Hello there!!"}

        return Response(data, status=status.HTTP_200_OK)

```

The client will receive the below response:

```javascript
{"message": "Hello there!!"}
```

---

### Intro to Serializer

#### When should we return a Python dictionary or Serializer data?

This really depends on the scenario. You need to decide what is appropriate to return.

If the API needs to return database data, you need to use Serializer data to return back.
* Listing database items

* Creating/Retrieving/Updating/Deleting one database item

---

### Intro to Serializer

#### When should we return a Python dictionary or Serializer data?

If the API is doing any of below actions, then I would recommend a Python dictionary to return.

1. Data processing and a need to return success/failure message

1. A need to return more than one Serializer data or some complex Python data

####Tip

*If you think API View should display the serializer data as the outcome of data processing,*

*Feel free to do so!*

---

### Intro to Serializer

#### Let's write a serializer class!

Writing a serializer feels just like Django Form class.

The below is an example of ModelSerializer. It looks really same as Django's ModelForm class!

```
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
```

---

### Intro to Serializer

#### Let's write a serializer class!

In order to use ModelSerializer, we need a Django model. Here is a Todo model for the example:

```
class Todo(models.Model):

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    title = models.CharField("Title", max_length=100)
    content = models.TextField("Content", null=True, blank=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)

    user = models.ForeignKey(User)

    def __str__(self):
        return "%s by %s User" % (self.title, self.user)
```

With our TodoSerializer class, Todo Queryset will be converted to ...

---

### Intro to Serializer

Serializer class will convert Todo Queryset to below JSON list. Dead simple. Super powerful.

```javascript
[
    {
        "id": 1,
        "title": "Test",
        "content": "",
        "created_at": "2015-01-30T22:38:54.330401Z",
        "updated_at": "2015-01-30T22:38:54.330430Z",
        "user": 1
    },
    {
        "id": 2,
        "title": "Grocery shopping",
        "content": "Need to buy some milk and bread",
        "created_at": "2015-01-30T22:40:44.738452Z",
        "updated_at": "2015-01-30T22:40:44.738480Z",
        "user": 1
    },
    {
        "id": 3,
        "title": "Test for tomorrow",
        "content": "Finals week is coming!!",
        "created_at": "2015-01-30T22:47:54.596758Z",
        "updated_at": "2015-01-30T22:47:54.596784Z",
        "user": 1
    }
]
```

---

### Intro to Serializer

Remember that Todo model has a foreign key to User?

By default, any related fields, such as foreign key, one-to-one, and many-to-many fields will be shown as primary key value.

```python
{
    "id": 1,
    "title": "Test",
    "content": "",
    "created_at": "2015-01-30T22:38:54.330401Z",
    "updated_at": "2015-01-30T22:38:54.330430Z",
*   "user": 1
}
```

What if we want to show the fields for related fields instead of primary key value? Can we do that?

---

class: center, middle

# Nested serializer

Make your serializer to carry multiple Django data at once.

---

### Nested serializer

It is possible to use a serializer in another serializer as a field. Let's create a Serializer for User model.

```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'is_active')
```

Also, notice that UserSerializer has fields attribute in Meta class. Again, this is same as Django Form's fields!

---

### Nested serializer

Back to our TodoSerializer class. We override user field with UserSerializer. Therefore, we are nesting the serializer!

```python
class TodoSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Todo
```

Now the user field will be **converted with UserSerializer data**, instead of returning its primary key value.

---

### Nested serializer

Now we're seeing User data inside Todo serialized data!

```javascript
[
    {
        "id": 1,
*       "user": {
*           "id": 1,
*           "username": "admin",
*           "first_name": "",
*           "last_name": "",
*           "email": "",
*           "date_joined": "2015-01-30T22:37:16.585677Z",
*           "is_active": true
*       },
        "title": "Test",
        "content": "",
        "created_at": "2015-01-30T22:38:54.330401Z",
        "updated_at": "2015-01-30T22:38:54.330430Z"
    }
]
```

---

class: center, middle

# Uh oh

Houston, we have a problem.

---

### Nested serializer problem

There is now a problem with our Todo Create API. Here is what we see from API Browser.

<img src="images/api_browser_4.png" width="100%" height="500px"/>

---

### Nested serializer problem

**Serializing user field also works on other HTTP requests such as POST on this example.**

This is problematic for the following reasons:
* If we have lots of models and serializers, making a POST API request will be very cumbersome.

* This now has a dependency. In order to create Todo, now we have to create User. What if we want to use existing User?

* We can create and get User from the separate API. Then we could supply User ID in order to create Todo. Would it be better?

**This beats Separation of Concerns.**

---

class: center, middle

# How do we solve this?

---

### Nested serializer solution

We can limit Serializer class to be only used in read or write actions.

```
user = UserSerializer(read_only=True)
```

With this setup, user field will only be displayed in GET request. This will remove the User object dependency.

---

### Nested serializer solution

<img src="images/api_browser_5.png" width="100%" height="500px"/>

---

### Nested serializer solution

We just turned off UserSerializer for write actions, but user is still required for Todo model.

```
*user = models.ForeignKey(User)
```

What should we do?

We need to manually give User object when creating Todo object.

---

### Nested serializer solution

#### OK, where should we code this validation?

We can do this in Serializer level or API View level. I'll choose API View level to get this validation.

We need to override create method for TodoCreateAPIView in order to add this custom validation.

```
def create(self, request, *args, **kwargs):
    # Put our validation, then return Response object accordingly here!
```

---

### Nested serializer solution

#### How are we going to do that?

Let's expect the POST request to have a User ID.
* We can access POST request data from request.data, remember?

Then, we need to send an error HTTP response for below scenarios:
* The request does not have user_id.
* The request gives us the User ID that does not exist in DB.

If the request has the valid User ID:
1. then let's load User object.
1. then create a serializer with request.data
1. then manually pass User object to the serializer.save() method.

```
user = get_object_or_404(User, id=self.request.data.pop('user_id'))

*serializer.save(user=user)
```

---

class: center, middle

# Response

A shipping package that the client receives from API.

---

class: middle

### Response

Just like Django views need to return HttpResponse, API Views need to return the Rest Framework's Response.

```
class TodoListAPIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        queryset = Todo.objects.all()

        # serializer = TodoSerializer(queryset, many=True)

        # return Response(serializer.data, status=status.HTTP_200_OK)

        data = {"message": "Hello there!!"}

*        return Response(data, status=status.HTTP_200_OK) <---- This guy

```

---

class: middle

### Response

When you create a Response, you can give the following parameters:
* data

* status

* template_name

* headers

* content_type


For the most part, you'll be using **data and status** a lot.

```
return Response({"data": "Very simple!"}, status=status.HTTP_200_OK)
```

---

class: center, middle

# Response status

A shipping package label.

---

class: middle

### Response status

When you create a Response, it is very important that you need to set an appropriate HTTP response status code.

If the API returns perfectly fine data with HTTP error status, **then the client will misintepret the response, and will throw the good data or execute error handling codes!**

The reason is that HTTP is a protocol; **a set of rules that all devices connected to Internet must follow**. They play by the rules, so let us respect the rules here as well.

---

class: middle

### Response status

If your API view handled the data according to correct logic, please return HTTP 200 OK status.

```
return Response({"data": "I'm good, dude!! :D"}, status=status.HTTP_200_OK)
```

**Please do not send a wrong HTTP response status with valid data.**

```
return Response({"data": "I'm good, dude!! :D", "anotherData": "Really I'm cool, OK?"}, status=status.HTTP_403_FORBIDDEN)
```

---

class: middle

### Response status

If the API sends a wrong response status, the client will still receive the data no matter what.

**However, the response will be received as the error response, thus the client will behave accordingly!**

```javascript
{"anotherData":"Really I'm cool, OK?","data":"I'm good, dude!! :D"}
```

> [01/Feb/2015 06:14:33] "GET /api/todo/wrongResponse/ HTTP/1.1" 403 67

---

class: middle

### Response status

#### What are the status codes we should use?

Django-REST-Framework has a list of constant values for each HTTP status. Here are some examples.

```
from rest_framework import status

status.HTTP_200_OK
status.HTTP_201_CREATED
status.HTTP_204_NO_CONTENT
status.HTTP_205_RESET_CONTENT
status.HTTP_206_PARTIAL_CONTENT

status.HTTP_301_MOVED_PERMANENTLY
status.HTTP_302_FOUND

status.HTTP_400_BAD_REQUEST
status.HTTP_401_UNAUTHORIZED
status.HTTP_403_FORBIDDEN
status.HTTP_404_NOT_FOUND
status.HTTP_405_METHOD_NOT_ALLOWED
```

---

class: middle

### Response status

#### What status code should I use?

Here is my guideline regarding setting successful HTTP response status.
* Displaying contents, return 200 OK.

* Creating something in DB, return 201 Created.
  * *New user sign up, new Todo item, and so on ;)*

* Updating something *partially in DB, return 206 Partial Content.
  * *The client mainly expects this for PATCH request.*

* Updating something *fully in DB, return 205 Reset Content.
  * *The client mainly expects this for PUT request.*

* Deleting something in DB, return 204 No Content.
  * *The client mainly expects this for DELETE request.*

---

class: middle

### Response status

#### What status code should I use?

Here is my guideline regarding setting bad HTTP response status.
* Having data or processing errors or failed validation, return 400 Bad Request.

* Receiving unauthorized request, return 401 Unauthorized.

* Recieving a valid request without a permission to access, return 403 Forbidden.

* Unable to do the job because of the non-existing requested data in application, return 404 Not Found.

---

class: center, middle

# Pagination

Pizza cutter.

---

### Pagination

Let's say we have thousands of things to do; Suppose we created 2,000 Todo objects in our Django API application.

If the Todo List API sends all of 2,000 Todo data at once, the client will get the massive list of data. Meanwhile, Django needs to create the massive list too.

Therefore, it would be slower for both Django and our client to process JSON data.

It takes a long time to make a huge pizza and it takes a longer time to eat that pizza at once!

We need to be less greedy on the quantity of data we're sending. Therefore, we should divide the data in chunks by Pagination.

---

### Pagination

The ListAPIView generic view provides us the pagination by default. We can use paginate_by, max_paginate_by, and paginate_by_param arguments.

```
class TodoGenericListAPIView(ListAPIView):
    model = Todo
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, )
    paginate_by = 1
    max_paginate_by = 10
    paginate_by_param = 'size'
```

---

### Pagination

Now our Todo List Generic APIView returns the paginated data. We can revisit the API url with GET parameter page to visit other paginated data.

<img src="images/pagination.png" width="100%" height="600px"/>

---

### Pagination

#### Can we use Pagination in a barebone APIView?

Absolutely. We need two things to do this in APIView.
* Django's built-in Paginator

* Django-REST-Framework's PaginatorSerializer class

Let's create a new serializer class

```
from rest_framework import pagination

class TodoPaginatedSerializer(pagination.PaginationSerializer):
    class Meta:
        object_serializer_class = TodoSerializer
```

---

### Pagination

#### Can we use Pagination in a barebone APIView?

Let's go back to view to use TodoPaginatedSerializer and Django's Paginator.

```
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .serializers import TodoSerializer, TodoPaginatedSerializer
```

Pagination works with GET parameter. GET parameter allows us to visit the API with some extra options, thus a bit of flexibility is here.

We can use GET parameter to get the # of page in order to divide our Queryset. When we get the page #, we pass it to Django's built in Paginator.

---

### Pagination

#### Can we use Pagination in a barebone APIView?

```
 # Paginate Queryset by 2 item per each page
paginator = Paginator(queryset, 2)

# Get page # from GET parameter
pageNum = request.query_params.get('page')

try:
    # Get the paginated queryset
    paginatedQueryset = paginator.page(pageNum)

except PageNotAnInteger:
    # Set the first page by default
    paginatedQueryset = paginator.page(1)

except EmptyPage:
    # If the page number exceeds the number of pages, set the last page
    paginatedQueryset = paginator.page(paginator.pages)

# Pass it to TodoSerializer!
serializer = TodoSerializer(paginatedQueryset, many=True)
```

---

### Pagination

#### What about serializing Python data instead of Serializer?

That is easy too. Just pass the Python list or tuple to Paginator!

---

class: center, middle

# Authentication & Permissions

Boarding pass and ID, please.

---

class: middle

### Authentication & Permissions

Now we know how to make API endpoints. However, some data we're providing may be sensitive or should be only accessed by authenticated users.

Perhaps, we want to block strangers accessing our API otherwise Django application will experience heavy bandwidth issue.

We can perform two different mechanisms: Authentication and Permission.

---

class: middle

### Authentication & Permissions

We can use Authentication on Django-REST-Framework to filter out HTTP requests that are not authenticated. Therefore when the client sends an API request, the client also needs to prove that he is a good guy.

The easy way to do is to use one of HTTP headers: **Authorization**. Thankfully, Django-REST-Framework provides an Authentication using Token.

---

class: middle

### Authentication & Permissions

#### How to use Token Authentication in DRF

Token Authentication has its own Django app. Therefore, we need to add rest_framework.authtoken app to our INSTALLED_APPS in Django settings.

```
INSTALLED_APPS = (
    ...
    'rest_framework',
    'rest_framework.authtoken'
)
```

---

### Authentication & Permissions

#### How to use Token Authentication in DRF

By default, DRF uses Basic & Session Authentication. The reason we can test DRF in API Browser is that we are authenticated via web browser session. We need to add TokenAuthentication class to the dictionary.

```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
*       'rest_framework.authentication.TokenAuthentication',
    )
}
```

---

### Authentication & Permissions

#### How to use Token Authentication in DRF

Now we enabled Token Authentication in DRF. Next step is we need to create Token object for each User object so that we can start using HTTP Authorization.

```
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

myUser = User.objects.first()

token = Token.objects.create(user=myUser)
```

---

### Authentication & Permissions

#### How to use Token Authentication in DRF

Or we can create Token objects in Django admin as well!

<img src="images/token_in_django_admin.png" width="100%"/>

---

### Authentication & Permissions

#### How to use Token Authentication in DRF

After creating Token object for Django User, you can access Token key in User.auth_token.key
```
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

myUser = User.objects.first()
print myUser.auth_token.key # u'2db003609e55882874cf2fc7a2fc1b70695c7051'

# OR
# token = Token.objects.get(user=myUser)
# print token.key
```

---

### Authentication & Permissions

#### How to use Token Authentication in DRF

Before jumping into how to use our Token. Let us limit TodoListAPIView to prepare.

First, let's limit our TodoListAPIView to only accept authenticated HTTP request by Token. We can use Django-REST-Framework's Permissions to do this easy.

```
from rest_framework.permissions import IsAuthenticated, AllowAny
...


class TodoListAPIView(APIView):
*   permission_classes = (IsAuthenticated, )
```

Now TodoListAPIView will only accept authenticated HTTP requests by Token, Basic, or Session Authentication.

Note that permission_classes is a Python tuple. This means that we can add more than one permission. If multiple permissions are set, then APIView will check each of them, and reject the request if one of them fails.

---

### Authentication & Permissions

#### How to use Token Authentication in DRF

Now we can access Token key for User and limited TodoListAPIView for authenticated requests only. Sweet.

Let's try to call our Todo List API without authentication.

```bash
$ curl -X GET http://localhost:8000/api/todo/

{"detail":"Authentication credentials were not provided."}
```

**Todo List API rejects my request with the message saying "Uh oh, I don't know you, stranger."**

---

### Authentication & Permissions

#### How to use Token Authentication in DRF

Let us show who we are by Token key.

iOS, Android, Web, and other client platforms have their own way to add HTTP header. What is important here is the client needs to add Authorization header with the value of "Token TOKEN_KEY"

In curl command, we can set the HTTP Authorization header like this:
```bash
$ curl -X GET http://localhost:8000/api/todo/ -H "Authorization: Token 2db003609e55882874cf2fc7a2fc1b70695c7051"
```

And, we can now get the data from Todo List API again!

```javascript
[
    {"id":1,"title":"Something","content":"YOYO","user":{"id":1,"username":"admin","first_name":"","last_name":"","email":"","date_joined":"2015-01-30T22:37:16.585677Z","is_active":true},"todo_rocks":"Something Todo item rocks!","created_at":"2015-01-30T22:38:54.330401Z","updated_at":"2015-02-01T08:43:28.930091Z"},

    {"id":2,"title":"Grocery shopping","content":"Need to buy some milk and bread","user":{"id":1,"username":"admin","first_name":"","last_name":"","email":"","date_joined":"2015-01-30T22:37:16.585677Z","is_active":true},"todo_rocks":"Grocery shopping Todo item rocks!","created_at":"2015-01-30T22:40:44.738452Z","updated_at":"2015-01-30T22:40:44.738480Z"},

    {"id":3,"title":"Test for tomorrow","content":"Finals week is coming!!","user":{"id":1,"username":"admin","first_name":"","last_name":"","email":"","date_joined":"2015-01-30T22:37:16.585677Z","is_active":true},"todo_rocks":"Test for tomorrow Todo item rocks!","created_at":"2015-01-30T22:47:54.596758Z","updated_at":"2015-01-30T22:47:54.596784Z"},

    {"id":4,"title":"TEST NOTE","content":"Hi","user":{"id":1,"username":"admin","first_name":"","last_name":"","email":"","date_joined":"2015-01-30T22:37:16.585677Z","is_active":true},"todo_rocks":"TEST NOTE Todo item rocks!","created_at":"2015-01-30T22:59:07.099204Z","updated_at":"2015-01-30T22:59:07.099225Z"},

    {"id":5,"title":"My next life goal","content":"Write a cookbook.","user":{"id":1,"username":"admin","first_name":"","last_name":"","email":"","date_joined":"2015-01-30T22:37:16.585677Z","is_active":true},"todo_rocks":"My next life goal Todo item rocks!","created_at":"2015-02-01T07:19:48.635628Z","updated_at":"2015-02-01T07:19:48.635653Z"},

    {"id":6,"title":"YOYOYO","content":null,"user":{"id":1,"username":"admin","first_name":"","last_name":"","email":"","date_joined":"2015-01-30T22:37:16.585677Z","is_active":true},"todo_rocks":"YOYOYO Todo item rocks!","created_at":"2015-02-01T07:55:01.473052Z","updated_at":"2015-02-01T07:55:01.473236Z"}
]
```

---

class: center, middle

# Closing advices

Things I wanted to learn and where to go from now

---

class: middle

### Closing advices

Make your API Simple. Remember KISS (Keep It Simple, Stupid).

More complex the API is, More work the API has to do, Bigger API response, Longer time the client waits.

Quality API is fast and doing the job right.

Make each API as narrow as possible. Make each API do just one job. The API should not be dependent on each other.

This way, your client will call a series of API requests to achieve something: Modular and Manageable.

---

### Where to go from now

Keep practicing and building more APIs with Django-REST-Framework!

Be challenging by trying advanced features!
* Serializer custom action

* FilterBackend

* Custom API Permissions

* Viewset

* Many more

Study these from [Django-REST-Framework](https://www.django-rest-framework.org)

Check out Django's REST Authentication API View library from Tivix's [Django-REST-Auth](https://github.com/Tivix/django-rest-auth)

---

class: center, middle

## Thank You

Be the cool kids who know how to build APIs and quickly create user platforms! Make Django proud.

---

class: center, middle

# Question Time!
