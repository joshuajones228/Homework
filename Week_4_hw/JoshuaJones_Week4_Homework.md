## **1.** What does one need to do to use a module?
A. You have to import it. The best way is to import the module and use the convention shorthand for it. 

> I.E. `import pandas as pd` 

You can also search for modules and packages you need [here](https://pypi.org/)

## **2.** Name a Module (not the DateTime Nodule) we looked at and write a line or 2 of code as an example using this module.
Let's use the example from above.

> `import pandas as pd`

>`df = (your_csv_here.csv, args)`
>`df.columns #this will show the columns in your dataframe`

## **3.** What is a benefit of using Exception handling?
Exception handling is great because it allows your code to still execute in spite of errors. 

An good example is the `ZeroDivisionError` in python, that will throw an error when you try to divide by 0, but will not break your code for the user.

## **4.** What are the 4 components used for Python Exception Handling?
they are: 
- try 
- except
- else 
- finally

## **5.** NumPy arrays are like what Python data type?
They're like lists except they can only be 1 type of data.
## **6.** What is one of the main benefits of using NumPy arrays.
They're way faster than lists.
## **7.** What is one of the main requirements about the 'dtype' of NumPy arrays? 
it has to be set by user.
## **8.** Of the 10 uses of NumPy, name 2.
mathematical operations, logical operations
## **9.** Name one of the other libraries we'll use with NumPy?
pandas
## **10.** What is the shape of NumPy arrays?
The shape is effectively the number of elements in each dimension `np.array = [1,2,3]`, for example this is a 1 dimension array with 3 elements, or (3,).
## **11.** What is a Tensor?
An array with 3+ dimensions. So once we get out of the 2d world, we are there
## **12.** Name a reason why it's better using NumPy for Data Analysis than using a Python List?
NumPy is built in C and is way faster than lists.
## **13.** When creating an "empty" array, where do the elements come from?
They are whatever values are at the present memory location

&#x2600;&#x2600;&#x2600;&#x1F680;&#x1F680;&#x1F680;