class PasswordRequirements:
    def __init__(self, password:str) -> None:
        self.password = password
    
    def validate(self) -> list:
        pw = self.password
        errors = []
        if len(pw) < 8:
            errors.append("Minimum length: 8 characters")
        if len(pw) > 16:
            errors.append("Maximum length: 16 characters")
        if not self.has_number():
            errors.append("Requires at least one number")
        if not self.has_upper_case():
            errors.append("Requires at least one uppercase letter")
        if not self.has_special_character():
            errors.append("Requires at least one special character (!@#$%^&*())")
        return errors
        
    def has_number(self) -> bool:
        for n in range(10):
            if self.password.count(str(n)) > 0:
                return True
        return False
    
    def has_upper_case(self) -> bool:
        special_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for sc in special_characters:
            if self.password.count(sc) > 0:
                return True
        return False
    
    def has_special_character(self) -> bool:
        special_characters = "!@#$%^&*()"
        for sc in special_characters:
            if self.password.count(sc) > 0:
                return True
        return False

def validate_password(password:str) -> dict:
    password_requirements = PasswordRequirements(password)
    errors = password_requirements.validate()
    return {
        "is_valid": len(errors) == 0,
        "messages": errors
    }
    
if __name__ == "__main__":
    passwords = [
        "1234",
        "abcd",
        "Abcd",
        "abcd!",
        "Abcd!",
        "Abcd123@",
        "1234567890abcdefg",
        "1234567890Abcdef!"
    ]
    
    for password in passwords:
        print(password)
        print(validate_password(password))
