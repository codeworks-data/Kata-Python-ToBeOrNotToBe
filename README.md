# Kata-Python-ToBeOrNotToBe
This kata has for objective to define a custom `__eq__`.

## Instructions
Somebody points out to you that the project you are working on duplicates many instances of the `Item` class.

Before finding the source of these duplications, you are asked to modify the `Item` class in order to know if two instances represent the same business object.

# Rules
You have to implement a custom `__eq__` to `Item`.

An `Item` is equals to another if and only if :
- They have the same location
- They have the same name

## Code
In the `src/main` folder, you will find the class `Item` with the missing `__eq__`.

## Test it
You can test your implementation by running the `src/test/ItemTest` class.