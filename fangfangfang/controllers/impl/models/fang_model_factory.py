from fangfangfang.models.model import Model
from fangfangfang.controllers.impl.models.homoglyph_fang_model\
    import HomoglyphFangModel


class FangModelFactory(object):

    _model_class_mappings = {
        Model.HOMOGLYPH: HomoglyphFangModel
    }
    _default_model = HomoglyphFangModel

    @classmethod
    def create_model(cls, model: str):
        model_class = cls._default_model if model is None\
            else cls._model_class_mappings[model]
        return model_class()
