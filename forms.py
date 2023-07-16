from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, FloatField
from wtforms.validators import DataRequired
from product_choices import name_choice, type_of_sale


class ProductForm(FlaskForm):
    name = SelectField(label='Produto', choices=name_choice,
                       validators=[DataRequired()])
    price = FloatField(label='Preço', validators=[DataRequired()])
    quantity = IntegerField(label='Quantidade', validators=[DataRequired()])
    type_of_sale = SelectField(
        label='Tipo de pagamento', choices=type_of_sale, validators=[DataRequired()])
