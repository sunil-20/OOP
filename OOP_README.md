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