### OOP
#### *class variable*
* class variables are shared among all instances of the class.
* instance variables unique to each instances e.g. name, pay, email etc.
* class variable should be same for the each instances.
* annual raise >> class variable as all instances(individual employee) have same raise.
#### Class methods and Static methods

In Python, both class methods and static methods are used to define methods that are associated with a class rather than with instances (objects) of the class. However, they have different purposes and behaviors:

**Class Method:**

1. **Decorator:** Class methods are defined using the `@classmethod` decorator.

2. **Access to Class and its Attributes:** Class methods have access to the class itself and its attributes. They can be called on the class itself or on instances of the class.

3. **First Argument is Class:** The first parameter of a class method is typically named `cls`, and it refers to the class itself (similar to `self` for instance methods). This allows class methods to modify or access class-level attributes and call other class methods.

4. **Common Use Cases:** Class methods are often used for tasks that involve class-level operations, such as creating alternative constructors or accessing class-level data.

   Example:
   ```python
   class MyClass:
       class_variable = 10

       @classmethod
       def print_class_variable(cls):
           print(cls.class_variable)

   MyClass.print_class_variable()  # Output: 10
   ```

**Static Method:**

1. **Decorator:** Static methods are defined using the `@staticmethod` decorator.

2. **No Access to Class or Instance:** Unlike class methods, static methods do not have access to the class itself (via `cls`) or its instances (via `self`). They behave like regular functions within the class namespace.

3. **No Implicit First Argument:** Static methods do not have an implicit first argument like `cls` or `self`. They take regular arguments and can be called on the class or instances, but they don't have access to class-level data.

4. **Common Use Cases:** Static methods are used for utility functions that are related to the class but don't depend on class-specific data. They are often used when a method does not need to modify class or instance state.

   Example:
   ```python
   class MathOperations:
       @staticmethod
       def add(a, b):
           return a + b

   result = MathOperations.add(5, 3)  # Calling a static method
   ```

In summary, the main difference between class methods and static methods in Python is their access to class and instance data. Class methods have access to class-level data and are often used for class-level operations, while static methods are more like standalone functions within the class and don't have access to class or instance-specific data. The choice between them depends on the specific requirements of your code and how you intend to use them.

**Access of objects inside a class:**

Objects of one function (or method) in a class can access objects of another function in the same class, provided that those objects are attributes of the class and not local variables within the functions. This is because class attributes are accessible to all methods of the class, and objects created from the class have access to these attributes.

Here's an example to illustrate this concept:

```python
class MyClass:
    def __init__(self):
        self.value = 0  # value is an object attribute

    def increment(self):
        self.value += 1

    def double(self):
        self.value *= 2

# Create an instance of MyClass
obj = MyClass()

# Access and modify the 'value' attribute using different methods
obj.increment()  # Increment 'value' by 1
print(obj.value)  # Output: 1

obj.double()     # Double 'value'
print(obj.value)  # Output: 2
```

In the example above, the `value` attribute is shared between the `increment` and `double` methods. When you create an object (`obj`) from the `MyClass` class, that object has access to the `value` attribute, and both methods can access and modify it.

So, in summary, objects created from a class can access and manipulate attributes that are part of the class, regardless of which method in the class is used to access or modify those attributes.

**Detail on Self argument:** 

 In object-oriented programming, especially in Python, the `self` argument is a reference to the instance of the class that a method is called on. To understand this concept, it's helpful to think of a class as a blueprint for creating objects (instances), and `self` as a way to interact with the specific object that a method is currently operating on.

Here's a more detailed explanation:

1. **Classes and Objects:** In Python, classes are used to define the structure and behavior of objects. An object is an instance of a class, and it can have its own set of attributes (variables) and methods (functions) defined in the class.

2. **Methods and the `self` Argument:** When you define methods within a class, you typically include a special first parameter named `self`. This parameter represents the instance of the class. By convention, it's named `self`, but you could technically use any name, although it's strongly recommended to stick with `self` for clarity.

3. **Instance-Specific Data:** Inside methods, you can access and manipulate instance-specific data (attributes) using `self`. For example, if a class has an attribute `name`, you can access it as `self.name` within a method to refer to the `name` attribute of the specific object.

4. **Different Objects, Same Method:** If you create multiple objects (instances) from the same class, each object will have its own set of attributes and its own copy of the methods. When you call a method on an object, Python automatically passes a reference to that object as the `self` argument for that method.

5. **Accessing Attributes and Methods:** By using `self`, you can access attributes and call methods specific to the instance. This allows you to work with the data and behavior of individual objects, even if they are created from the same class.

Here's an example to illustrate the concept:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Creating two instances of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Calling the introduce method on both instances
person1.introduce()  # Output: "My name is Alice and I am 30 years old."
person2.introduce()  # Output: "My name is Bob and I am 25 years old."
```

In this example, `self` in the `introduce` method refers to the specific instance (`person1` or `person2`) on which the method is called, allowing it to access the unique attributes (`name` and `age`) of that instance.