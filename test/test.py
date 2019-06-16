class customeSet:
    def __init__(self, rit_manage_id, ref_id):
        self.rit_manage_id = rit_manage_id
        self.ref_id = ref_id

    def __eq__(self, other):
        return self.rit_manage_id == other.rit_manage_id and self.ref_id == other.ref_id

    def __hash__(self):
        return hash(self)
