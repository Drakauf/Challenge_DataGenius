from extension import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200), unique=False, nullable=True)
    image = db.Column(db.String(1000))
    stock = db.Column(db.Integer, default=0)
    promo = db.Column(db.String(300), nullable=True)
    prix = db.Column(db.Integer, default=0)

    def __repr__(self):
        return 'Product #: %i name: %r Description: %s image_url: %s stock: %i Promo %s\n' % (self.id, self.name, self.description, self.image, self.stock, self.promo)
