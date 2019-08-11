from fangfangfang.models.model import Model
from jsonschema import draft4_format_checker


@draft4_format_checker.checks('model')
def is_model(val):
    """Returns true if the value represents a valid model.

    Keyword arguments:
    val -- the model value
    """
    if val is None:
        return True

    model = Model()
    allowed_models = [getattr(model, attr) for attr in dir(model) if
               not callable(getattr(model, attr)) and not attr.startswith('__')]
    return val in allowed_models
