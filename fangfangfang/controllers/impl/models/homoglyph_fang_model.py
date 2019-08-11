from fangfangfang.str_utils import replace_all
from fangfangfang.controllers.impl.models.abstract_fang_model\
    import AbstractSingletonFangModel
import string
import homoglyphs as hg


class HomoglyphFangModel(metaclass=AbstractSingletonFangModel):

    def __init__(self):
        self.ascii_to_homoglyph = {}
        self.homoglyph_to_ascii = {}
        homoglyphs = hg.Homoglyphs()

        for char in string.printable:
            combinations = homoglyphs.get_combinations(char)
            if len(combinations) > 1:
                homoglyph_char = homoglyphs.get_combinations(char)[1]
                self.ascii_to_homoglyph[char] = homoglyph_char
                self.homoglyph_to_ascii[homoglyph_char] = char

    def defang(self, url: str):
        return replace_all(url, self.ascii_to_homoglyph)

    def refang(self, text: str):
        return replace_all(text, self.homoglyph_to_ascii)
