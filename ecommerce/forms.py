from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField,IntegerField,SelectField,TextAreaField,FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from ecommerce.models import Category,User

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    phone_number = IntegerField('Phone Number',
                                validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    """def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

    def validate_phone_number(self,phone_number):
        user = User.query.filter_by(phone_number=phone_number.data).first()
        if user :
            raise ValidationError('Already registered with this number.')"""

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    #def isUserAdmin(self,email):
        #pass

class AddCategoryForm(FlaskForm):
    category_name = StringField('Category Name', validators=[DataRequired()])
    submit = SubmitField('Save')

    def validate_category_name(self,category_name):
        category = Category.query.filter_by(category_name = category_name.data).first()
        if category:
            raise ValidationError('Category of this name is already added !. Please try some different names.')


class AddProductForm(FlaskForm):
    category = SelectField('Category', coerce=int)
    product_name = StringField('Product Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = FloatField('Price',validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    quantity = IntegerField('Quantity',validators=[DataRequired()])

class UpdateProductForm(FlaskForm):
    product_name = StringField('Product Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = FloatField('Price',validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    quantity = IntegerField('Quantity',validators=[DataRequired()])
