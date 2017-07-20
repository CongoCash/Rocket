class: center, middle

# Django-REST-Framework

Silin Na, Software Engineer @ [Tivix](http://www.tivix.com)
---

class: center, middle

# What is API? - Application Programming Interface
---

class: center, middle

**A software service/resource available for other software to interact with.**

With APIs, we can make our software can talk to another software in order to achieve something relying on that program, or send/retrieve processed data either directions.
---

class: middle

### Facebook, Instagram, Parse, Google Maps, Stripe, Square, Dropbox, and other big companies all provide APIs.
Facebook - http://graph.facebook.com/n1207n/picture?type=large

Twitter - https://dev.twitter.com/rest/tools/console

Stripe - https://stripe.com/docs/api

Just Google “Company Name here” REST API for more!

Almost every mobile application uses it in order to get data from DB or data services!
---

class: middle

# An Example

https://graph.facebook.com/n1207n

```javascript
{
  id: "100000023295821",
  first_name: "Silin",
  gender: "male",
  last_name: "Na",
  locale: "en_US",
  name: "Silin Na",
  username: "n1207n"
}
```

* That's ME in Facebook API!

* We will get to why this data looks like this.

* Reminds you of a Python dictionary?

---

class: middle

### Why do they provide APIs?

* We can create a software that is easy and scalable to support multiple platforms. Ex) iOS, Android, Single Page App

* This is known as Software or Platform as a Service (SaaS, PaaS).

* It is to promote third-party application with their content, and influence back to their software.

* The company can maintain developer friendship and demonstrate their technical skills.
---

class: middle

### Why is this important?
* Lots of lots of people have more devices to access.

* Web is not the only platform people use anymore.

* To support mobile and other platforms quickly with data at ease, we need a set of APIs to power these platforms to be fully interactive.

* It is a trend that many software use other software as services to power their features. People use AWS for server hosting and DevOps. I use Slack for the main communication channel, integrated with Pivotal, Github, CircleCI, and Basecamp.
---

class: center, middle

# What is RESTful? - Representational State Transfer
---

class: center, middle

By default, HTTP is stateless. Web browser or anything that can load data from Internet is purely a delivery guy.
---

class: center, middle

### RESTful API

It is an idea that we should give some “meanings” or application logic bound to each HTTP url.
---

class: middle

## Examples
GET request to http://myawesomeapp.com/api/fruits/
  * Shows a list of fruit data

GET request to http://myawesomeapp.com/api/fruits/:fruit_id/
  * Shows one fruit data

POST request to http://myawesomeapp.com/api/fruits/create/
  * Creates fruit data

POST request to http://myawesomeapp.com/api/fruits/:fruit_id/edit
  * Updates one fruit data

POST request to http://myawesomeapp.com/api/fruits/:fruit_id/delete
  * Deletes one fruit data
---

class: middle

## Another example would be binding one url with multiple HTTP protocols

http://myawesomeapp.com/api/fruits/
  * GET request shows a list of fruit data

  * POST request creates a fruit data

http://myawesomeapp.com/api/fruits/:fruit_id/
  * GET request displays one fruit detail data

  * PATCH request updates one fruit data partially

  * PUT request updates one fruit data fully

  * DELETE or (maybe POST) request deletes one fruit data
---

class: middle

# Another Example - this time with some query params

https://graph.facebook.com/n1207n?fields=id%2Cname%2Cpicture

```javascript
{
  id: "100000023295821",
  name: "Silin Na",
  picture: {
    data: {
    is_silhouette: false,
    url: "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xaf1/v/t1.0-1/c0.2.50.50/p50x50/10330286_789163247761111_4936213709121362523_n.jpg?oh=0366e6fe0825b725fc87b1e3f272ca57&oe=555FBAAD&__gda__=1428283390_971426114562b625ece8eabe00d56b2d"
    }
  }
}
```

---

class: center, middle

# JSON - JavaScript Object Notation

A modern way to store the data in universal format.
---

class: middle

###Anyone familiar with XML?

```xml
<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>
```

It is a once-glorified-markup-language from 90’s. It was used to send data in universal format between software/platforms. It is still being used widely today.

Android Studio and Xcode use XML to visualize Graphic Interfaces or store internal core data. However for sending/retrieving data, this is easily getting complicated.

#### Therefore, many people didn't like XML a lot because it can look really complicated.

---

class: middle

**JSON is the data format we want to use today because of its simplicity if you were to work for a company or a project today.**

```javascript
[
    {
        "title": "And Now for Something Completely Different",
        "year": 1971
    },
    {
        "title": "Monty Python and the Holy Grail",
        "year": 1975
    }
]
```

---

# Chrome plugin to validate and view JSON output

* Get JSONView plugin on Chrome

* https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc?hl=en

---

class: center, middle

# DRF - Django-REST-Framework
A magical framework provided by Tom Christie to make a Django API application.
---

class: middle

You can have a web application as your main user platform, while you can provide backend support for Mobile, Single Page Application, and other platforms quickly.

We want our web application to expose these data from DB directly to our mobile devices and let mobile devices interact and make updates back to our web application.

With Django-REST-Framework, your website now can become a multi-platform application from just another web application.
---

class: middle

# What are we going to accomplish?

First, you will be building yet another Django web application in order to use DRF.

You will learn the followings:
* How to write APIs with Django-REST-Framework 3.x

* How to handle different HTTP requests in Django-REST-Framework

* How to prepare the data from DB to JSON-friendly format (Serialization)

* How to enforce authentication and permissions for your APIs

Ultimately, you will be prepared to be a full-stack developer as you will be learning AngularJS to implement Single Page App that is powered by Django RESTful APIs.
