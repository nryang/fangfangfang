from fangfangfang.str_utils import replace_all
from fangfangfang.models.defang_request import DefangRequest
from fangfangfang.models.refang_request import RefangRequest
from fangfangfang.models.defang_response import DefangResponse
from fangfangfang.models.refang_response import RefangResponse
from fangfangfang.controllers.impl.models.fang_model_factory\
    import FangModelFactory
import iocextract


def defang(body: DefangRequest):
    fang_model = FangModelFactory.create_model(body.model)
    defanged_contents = []
    for text in body.contents:
        urls = iocextract.extract_urls(text)
        substitutions = {}

        for url in urls:
            substitutions[url] = fang_model.defang(url)
        defanged_contents.append(replace_all(text, substitutions))
    return DefangResponse(defanged_contents)


def refang(body: RefangRequest):
    fang_model = FangModelFactory.create_model(body.model)
    refanged_contents = []
    for text in body.contents:
        refanged_contents.append(fang_model.refang(text))
    return RefangResponse(refanged_contents)
