from product_model import Product
from extension import db

def setup():
    added_product = ""
    stock_update = ""
    ret = ""
    check = Product.query.filter(Product.name == 'tata').first()
    if (check):
        check.stock += 8
        stock_update += "tata + 8\n"
    else:
        test = Product(name="tata", stock=8, description="Produit de test, achetez-y ;) ", prix=10)
        db.session.add(test)
        added_product += "tata + 8\n"

    check = Product.query.filter(Product.name == 'Drakauf').first()
    if (check):
        check.stock += 0
        stock_update += "Drakauf + 0\n"
    else:
        test = Product(name="Drakauf", stock=0, description="Ceci est un Pokemon Particulier", image="https://avatars0.githubusercontent.com/u/34242501?s=460&v=4", prix=1000000000)
        db.session.add(test)
        added_product += "Drakauf + 0\n"

    check = Product.query.filter(Product.name == 'A').first()
    if (check):
        check.stock += 10000
        stock_update += "A + 10000\n"
    else:
        test = Product(name="A", stock=0, description="Ceci est une Lettre", image="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/LetterA.svg/1200px-LetterA.svg.png", prix=1, promo = "2 Achete 1 Offer")
        db.session.add(test)
        added_product += "A + 10000\n"

    check = Product.query.filter(Product.name == 'B').first()
    if (check):
        check.stock += 30
        stock_update += "B + 10000\n"
    else:
        test = Product(name="B", stock=0, description="Ceci est une Lettre", image="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/LetterB.svg/1200px-LetterB.svg.png", prix=1, promo = "2ieme moitie prix")
        db.session.add(test)
        added_product += "B + 30\n"

    if (added_product != ""):
        ret = "The Following products have been added : " + added_product
    if (stock_update != ""):
        ret += "The Following products stock have been updated : " + stock_update
    db.session.commit()
    return(ret)

def add_product(id):
    check = Product.query.filter(Product.id == id).first()
    if (check):
        if (check.stock > 0):
            check.stock -= 1
            db.session.commit()
            return ("Success " + str(check.stock))
        else:
            return ("Error : 2")
    else:
        return ("Error : 1")

def calculate(products):
    ret = {}
    prod = {}
    total_prod = 0
    prom = {}
    total_prom = 0
    error = {}

    for p in products:
        check = Product.query.filter(Product.id == p).first()
        if (check):
            price = check.prix * products[p]
            total_prod += price
            prod[p] = { 'nom': check.name, 'prix': check.prix, 'qt': products[p], 't_prod': price} 
            if check.promo:
                if check.promo == "2 Achete 1 Offer":
                    nb_pprom = products[p] // 3
                    reduction = check.prix * nb_pprom
                    total_prom += reduction
                if check.promo == "2ieme moitie prix":
                    nb_pprom = products[p] // 2
                    reduction = (check.prix / 2) * nb_pprom
                    total_prom += reduction
                prom[p] =  { 'nom': check.name, 'prix': check.prix, 'qt': nb_pprom, 't_prod': reduction} 
        else:
            error = {"Un produit n'existe pas"}
    ret['prod'] = prod
    ret['total_prod'] = total_prod
    ret['prom'] = prom
    ret['total_prom'] = total_prom
    ret['error'] = error
    ret['total'] = total_prod - total_prom
    return ret
