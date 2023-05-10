
class BaseModel:
    n_obj = 0

    def __init__(self):
        BaseModel.n_obj += 1
        self.id = BaseModel.n_obj
