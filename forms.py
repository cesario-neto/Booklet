from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField
from wtforms.validators import DataRequired
from product_choices import name_choice


class ProductForm(FlaskForm):
    name = SelectField(label='Produto', choices=name_choice,
                       validators=[DataRequired()])
    price = IntegerField(label='Preço', validators=[DataRequired()])
    quantity = IntegerField(label='Quantidade', validators=[DataRequired()])
