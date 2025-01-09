[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17650028)
# Binary Calculator

This is my take on creating a calculator with multipule implications when it comes to binary calculations.

## How to use:
This calculator is able to add, subtract, multiply and divide. It takes 3 inputs; bin1, bin2 and your 
operator.

    When dividing or subtracting, be sure to put your dividen or minuend as bin1, and your divisor or subtrahend as bin2.

    Your operator is what determines what your trying to do. Use the + for addition, the - for subtraction, the * for multiplication and the / for division.

## Aditional information
NaN:

When dividing, the calculator checks if you are trying to divide by 0, and will return NaN.

Error:

If you input any number or letter other than 1s and 0s in bin1 and bin2, it will return an error, as you did not input valid binary code.

Overflow:

Eight bit binary code has a cap of 255 and cannot go below 0, so if you are trying to solve for something bigger than 255 or in the negative, it will return an overflow message.