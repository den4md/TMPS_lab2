from Composite.i_composite import IComposite


class Package(IComposite):

    def __init__(self, tracking_id: str):
        self.children = []
        super(Package, self).__init__(tracking_id)

    def add(self, icomposite: IComposite):
        if (not (icomposite in self.children)) and icomposite != self:
            self.children.append(icomposite)

    def remove(self, icomposite: IComposite):
        self.children.remove(icomposite)

    def find_by_tracking_id(self, tracking_id: str):
        if self._tracking_id == tracking_id:
            return self

        for child in self.children:
            if isinstance(child, IComposite):
                res = child.find_by_tracking_id(tracking_id)
                if res is not None:
                    return res
        return None

    def __str__(self):
        return "Package #" + self._tracking_id
