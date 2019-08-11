from fangfangfang.controllers.impl.models.abstract_fang_model\
    import AbstractSingletonFangModel
from fangfangfang.str_utils import replace_all
import string
import homoglyphs as hg


class HomoglyphFangModel(metaclass=AbstractSingletonFangModel):
    """
    This class defangs/refangs using homoglyphs.
    """

    def __init__(self):
        self.ascii_to_homoglyph = {}
        self.homoglyph_to_ascii = {}
        homoglyphs = hg.Homoglyphs()

        # Create translation tables from ascii to homoglyph and vice versa
        character_space = string.ascii_letters + string.digits
        for char in character_space:
            combinations = homoglyphs.get_combinations(char)
            if len(combinations) > 1:
                homoglyph_char = homoglyphs.get_combinations(char)[1]
                # Some unicode characters share the same hash
                # This is to prevent having more keys in self.ascii_to_homoglyph
                # than self.homoglyph_to_ascii
                if homoglyph_char not in self.homoglyph_to_ascii:
                    self.ascii_to_homoglyph[char] = homoglyph_char
                    self.homoglyph_to_ascii[homoglyph_char] = char

    def defang(self, ioc: str):
        return replace_all(ioc, self.ascii_to_homoglyph)

    def refang(self, text: str):
        return replace_all(text, self.homoglyph_to_ascii)
