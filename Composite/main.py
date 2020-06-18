from Composite.package import Package
from Composite.product import Product


def build_some_pack():
    pack = Package("001")
    pack.add(Product("002"))

    pack_in = Package("003")
    pack_in.add(Product("004"))

    pack.add(pack_in)
    pack.add(Product("005"))
    pack.add(Product("006"))
    return pack


if __name__ == '__main__':
    pack_1 = build_some_pack()

    print(pack_1.find_by_tracking_id("001"))
    print(pack_1.find_by_tracking_id("003"))
    print(pack_1.find_by_tracking_id("004"))
    print(pack_1.find_by_tracking_id("040"))
