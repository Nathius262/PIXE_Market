from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self, email=None, phone=None, password=None):
        if not email:
            if not phone:
                raise ValueError("Users must have an email address or a phone number")

        if not phone:
            if not email:
                raise ValueError("Users mut have either an phone number or email address")                

        if not password:
            raise ValueError("Users must secure accout with password")

        if email and phone:
            user = self.model(
                email=self.normalize_email(email),
                phone=phone,
            )
        elif email:
            user = self.model(
                email=self.normalize_email(email),
            )
        elif phone:
            user = self.model(
                phone=phone,
            )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email=None, phone=None, password=None):
        user = self.create_user(
            email=email,
            phone=phone,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user