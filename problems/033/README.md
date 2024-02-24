# Password Validator

## Overview
The Password Validator module (`password_validator.py`) is designed to ensure that passwords meet a specific set of security requirements. It includes a class `PasswordRequirements` which defines the criteria a valid password must meet, and a function `validate_password` which checks whether a given password satisfies these criteria.

## Objective
Your task is to implement the `password_validator` module with a `PasswordRequirements` class and a `validate_password` function according to the requirements detailed below.

## Requirements
Your `PasswordValidator` module should meet the following requirements:

- The `PasswordRequirements` class should define the following password requirements:
  - `minimum_length`: The minimum number of characters the password must contain.
  - `maximum_length`: The maximum number of characters the password must contain.
  - `requires_numbers`: Whether the password requires at least one numeric character.
  - `requires_uppercase`: Whether the password requires at least one uppercase letter.
  - `requires_special_characters`: Whether the password requires at least one special character (e.g., `!@#$%^&*()`).

- The `validate_password` function should:
  - Take a single `password` string as an argument.
  - Use an instance of `PasswordRequirements` to check if the provided `password` meets all the defined requirements.
  - Return a dictionary with:
    - A boolean value for the key `is_valid` indicating whether the password is valid.
    - A list of strings under the key `messages` that contains messages for each requirement not met.

## Instructions
1. Create a file named `password_validator.py`.
2. Implement the `PasswordRequirements` class with an appropriate constructor and a method to validate passwords.
3. Implement the `validate_password` function that utilizes the `PasswordRequirements` class.
4. Include a test block (within `if __name__ == "__main__":`) that:
   - Creates an instance of `PasswordRequirements` with the following settings:
     - Minimum length: 8 characters
     - Maximum length: 16 characters
     - Requires at least one number
     - Requires at least one uppercase letter
     - Requires at least one special character
   - Tests the `validate_password` function with a sample password
   - Prints the validation result including a list of validation messages.

## Notes
- Ensure your code adheres to the Python style guide (PEP 8).
- Your code should be well-documented with comments explaining the functionality.
- You may use Python's built-in modules and packages as required.

Good luck with your implementation!