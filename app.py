from flask import Flask, render_template, request, redirect, url_for
from booklet import Booklet
from forms import ProductForm
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config.from_pyfile('config.py')
csrf = CSRFProtect(app)
booklet = Booklet()


@app.route('/')
def booklet_view():
    form = ProductForm()
    return render_template('booklet.html', form=form)


@app.route('/booklet/create_order', methods=['POST'])
def create_order():
    form = ProductForm(request.form)

    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        quantity = form.quantity.data
        type_of_sale = form.type_of_sale.data

        dictionary = {
            'product': name,
            'price': price,
            'quantity': quantity,
            'type_of_sale': type_of_sale
        }

        booklet.add_order(dictionary)

    return redirect(url_for('booklet_view'))


if __name__ == '__main__':
    app.run(debug=True, port=8080)
