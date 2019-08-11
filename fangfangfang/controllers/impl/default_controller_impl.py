from fangfangfang.str_utils import replace_all
from fangfangfang.models.defang_request import DefangRequest
from fangfangfang.models.refang_request import RefangRequest
from fangfangfang.models.defang_response import DefangResponse
from fangfangfang.models.refang_response import RefangResponse
from fangfangfang.controllers.impl.models.fang_model_factory\
    import FangModelFactory
import iocextract
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'custom_regex.txt'), 'r') as f:
    custom_regex = f.read().splitlines()


def defang(body: DefangRequest):
    """Identifies indicators of compromise and defangs them. Urls, emails,
    and custom regex rules defined in custom_regex.txt are used to search for
    indicators of compromise.

    Keyword arguments:
    body -- the defang request body
    """
    fang_model = FangModelFactory.create_model(body.model)
    defanged_contents = []
    for text in body.contents:
        iocs = list(iocextract.extract_urls(text))\
               + list(iocextract.extract_emails(text))\
               + list(iocextract.extract_custom_iocs(text, custom_regex))
        substitutions = {}

        for ioc in iocs:
            substitutions[ioc] = fang_model.defang(ioc)
        defanged_contents.append(replace_all(text, substitutions))
    return DefangResponse(defanged_contents)


def refang(body: RefangRequest):
    """Refangs pieces of text.

    Keyword arguments:
    body -- the refang request body
    """
    fang_model = FangModelFactory.create_model(body.model)
    refanged_contents = []
    for text in body.contents:
        refanged_contents.append(fang_model.refang(text))
    return RefangResponse(refanged_contents)
