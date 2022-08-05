# AirBnB_clone

# What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

    Create a new object (ex: a new User or a new Place)
    Retrieve an object from a file, a database etc…
    Do operations on objects (count, compute stats, etc…)
    Update attributes of an object
    Destroy an object
 
 # Requirements
 # Python Scripts

    * Allowed editors: vi, vim, emacs
    * All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
    * All your files should end with a new line
    * The first line of all your files should be exactly #!/usr/bin/python3
    * A README.md file, at the root of the folder of the project, is mandatory
    * Your code should use the pycodestyle (version 2.8.*)
    * All your files must be executable
    * The length of your files will be tested using wc
    * All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    * All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    * All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    * A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
    
    
  # Python Unit Tests

    * Allowed editors: vi, vim, emacs
    * All your files should end with a new line
    * All your test files should be inside a folder tests
    * You have to use the unittest module
    * All your test files should be python files (extension: .py)
    * All your test files and folders should start by test_
    * Your file organization in the tests folder should be the same as your project
    e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
    e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
    * All your tests should be executed by using this command: python3 -m unittest discover tests
    * You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
    * All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    * All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    * All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    * We strongly encourage you to work together on test cases, so that you don’t miss any edge case
    
  
# More Info
# Execution

    * Your shell should work like this in interactive mode:
    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit

    (hbnb) 
    (hbnb) 
    (hbnb) quit
    $
    
    But also in non-interactive mode: (like the Shell project in C)
    $ echo "help" | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb) 
    $
    $ cat test_help
    help
    $
    $ cat test_help | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb) 
    $
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

# Tasks


0. README, AUTHORS
      
      Write a README.md:
          
          description of the project
          
          description of the command interpreter:
              
              how to start it
              
              how to use it
              
      
      You should have an AUTHORS file at the root of your repository, listing all   
      
      individuals having contributed content to the repository. For format, reference 
      
      Docker’s AUTHORS page
      
      You should use branches and pull requests on GitHub - it will help you as team 
      
      to organize your work
      
 
1. Be pycodestyle compliant!
    
    Write beautiful code that passes the pycodestyle checks.
    

2. Unittests

All your files, classes, functions must be tested with unit tests

guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$


Unit tests must also pass in non-interactive mode:

guillaume@ubuntu:~/AirBnB$ echo "python3 -m unittest discover tests" | bash
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$



3. BaseModel

Write a class BaseModel that defines all common attributes/methods for other classes:

    - models/base_model.py
    
    - Public instance attributes:
        
        * id: string - assign with an uuid when an instance is created:
            
            you can use uuid.uuid4() to generate unique id but don’t forget to convert 
            
            to a string
            
            the goal is to have unique id for each BaseModel
        * created_at: datetime - assign with the current datetime when an instance is created
        * updated_at: datetime - assign with the current datetime when an instance is 
        
        created and it will be updated every time you change your object
    - __str__: should print: [<class name>] (<self.id>) <self.__dict__>
    
    Public instance methods:
        
        * save(self): updates the public instance attribute updated_at with the 
        
        current datetime
        
        * to_dict(self): returns a dictionary containing all keys/values of __dict__ 
        
        of the instance:
            
            by using self.__dict__, only instance attributes set will be returned
            
            a key __class__ must be added to this dictionary with the class name of 
            
            the object
            
            created_at and updated_at must be converted to string object in ISO 
            
            format:
                
                * format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
                
                * you can use isoformat() of datetime object
            
            - This method will be the first piece of the serialization/deserialization 
            
            process: create a dictionary representation with “simple object type” of 
            
            our BaseModel
     
    guillaume@ubuntu:~/AirBnB$ cat test_base_model.py
    
    #!/usr/bin/python3
    
    from models.base_model import BaseModel

    my_model = BaseModel()
    
    my_model.name = "My First Model"
    
    my_model.my_number = 89
    
    print(my_model)
    
    my_model.save()
    
    print(my_model)
    
    my_model_json = my_model.to_dict()
    
    print(my_model_json)
    
    print("JSON of my_model:")

for key in my_model_json.keys():
    
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

guillaume@ubuntu:~/AirBnB$ ./test_base_model.py

[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First 

Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 

'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 

21, 5, 54, 119427)}

[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First 

Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 

'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 

21, 5, 54, 119427)}

{'my_number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': 

'2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 

'created_at': '2017-09-28T21:05:54.119427'}

JSON of my_model:
    
    my_number: (<class 'int'>) - 89
    
    name: (<class 'str'>) - My First Model
    
    __class__: (<class 'str'>) - BaseModel
    
    updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
    
    id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
    
    created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427

guillaume@ubuntu:~/AirBnB$ 
     

3. BaseModel

mandatory

Write a class BaseModel that defines all common attributes/methods for other classes:

    models/base_model.py
    
    Public instance attributes:
        
        id: string - assign with an uuid when an instance is created:
            
            you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
            
            the goal is to have unique id for each BaseModel
        
        created_at: datetime - assign with the current datetime when an instance is created
        
        updated_at: datetime - assign with the current datetime when an instance is 
        
        created and it will be updated every time you change your object
    
    __str__: should print: [<class name>] (<self.id>) <self.__dict__>
    
    Public instance methods:
        
        save(self): updates the public instance attribute updated_at with the current datetime
        
        to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
            
            by using self.__dict__, only instance attributes set will be returned
            
            a key __class__ must be added to this dictionary with the class name of the object
            
            created_at and updated_at must be converted to string object in ISO format:
                
                format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
                
                you can use isoformat() of datetime object
            
            This method will be the first piece of the serialization/deserialization 
            
            process: create a dictionary representation with “simple object type” of our BaseModel
            
 
guillaume@ubuntu:~/AirBnB$ cat test_base_model.py

#!/usr/bin/python3

from models.base_model import BaseModel

my_model = BaseModel()

my_model.name = "My First Model"

my_model.my_number = 89

print(my_model)

my_model.save()

print(my_model)

my_model_json = my_model.to_dict()

print(my_model_json)

print("JSON of my_model:")

for key in my_model_json.keys():
    
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

guillaume@ubuntu:~/AirBnB$ ./test_base_model.py

[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First 

Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 

'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 

21, 5, 54, 119427)}

[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First 

Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 

'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 

21, 5, 54, 119427)}

{'my_number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': 

'2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 

'created_at': '2017-09-28T21:05:54.119427'}

JSON of my_model:
    
    my_number: (<class 'int'>) - 89
    
    name: (<class 'str'>) - My First Model
    
    __class__: (<class 'str'>) - BaseModel
    
    updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
    
    id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
    
    created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427

guillaume@ubuntu:~/AirBnB$ 



4. Create BaseModel from dictionary
mandatory

Previously we created a method to generate a dictionary representation of an instance (method to_dict()).

Now it’s time to re-create an instance with this dictionary representation.

<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>

Update models/base_model.py:

    __init__(self, *args, **kwargs):
        
        you will use *args, **kwargs arguments for the constructor of a BaseModel. (more information inside the AirBnB clone concept page)
        
        *args won’t be used
        
        if kwargs is not empty:
            
            each key of this dictionary is an attribute name (Note __class__ from 
            
            kwargs is the only one that should not be added as an attribute. See the 
            
            example output, below)
            
            each value of this dictionary is the value of this attribute name
            
            Warning: created_at and updated_at are strings in this dictionary, but 
            
            inside your BaseModel instance is working with datetime object. You have 
            
            to convert these strings into datetime object. Tip: you know the string 
            
            format of these datetime
        
        otherwise:
            
            create id and created_at as you did previously (new instance)


guillaume@ubuntu:~/AirBnB$ cat test_base_model_dict.py

#!/usr/bin/python3

from models.base_model import BaseModel

my_model = BaseModel()

my_model.name = "My_First_Model"

my_model.my_number = 89

print(my_model.id)

print(my_model)

print(type(my_model.created_at))

print("--")

my_model_json = my_model.to_dict()

print(my_model_json)

print("JSON of my_model:")

for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")

my_new_model = BaseModel(**my_model_json)

print(my_new_model.id)

print(my_new_model)

print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py

56d43177-cc5f-4d6c-a0c1-e167f8c27337

[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-

e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 

'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 

'name': 'My_First_Model'}

<class 'datetime.datetime'>
--

{'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': 

'2017-09-28T21:03:54.052298', '__class__': 'BaseModel', 'my_number': 89, 'updated_at': 

'2017-09-28T21:03:54.052302', 'name': 'My_First_Model'}

JSON of my_model:
    
    id: (<class 'str'>) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
    
    created_at: (<class 'str'>) - 2017-09-28T21:03:54.052298
    
    __class__: (<class 'str'>) - BaseModel
    
    my_number: (<class 'int'>) - 89
    
    updated_at: (<class 'str'>) - 2017-09-28T21:03:54.052302
    
    name: (<class 'str'>) - My_First_Model
--

56d43177-cc5f-4d6c-a0c1-e167f8c27337

[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-

e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 

'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 

'name': 'My_First_Model'}

<class 'datetime.datetime'>

--

False
guillaume@ubuntu:~/AirBnB$



5. Store first object

Now we can recreate a BaseModel from another one by using a dictionary representation:

<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>

It’s great but it’s still not persistent: every time you launch the program, you don’t 

restore all objects created before… The first way you will see here is to save these 

objects to a file.

Writing the dictionary representation to a file won’t be relevant:

    Python doesn’t know how to convert a string to a dictionary (easily)
    
    It’s not human readable
    
    Using this file with another program in Python or other language will be hard.

So, you will convert the dictionary representation to a JSON string. JSON is a 

standard representation of a data structure. With this format, humans can read and all 

programming languages have a JSON reader and writer.

Now the flow of serialization-deserialization will be:

<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> 

FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>

Magic right?

Terms:

    
    


    
    


    
   
