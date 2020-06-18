from Composite.i_composite import IComposite


class Product(IComposite):

    def find_by_tracking_id(self, tracking_id: str):
        if tracking_id == self._tracking_id:
            return self
        else:
            return None

    def __str__(self):
        return "Product #" + self._tracking_id
