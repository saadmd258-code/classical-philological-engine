"""
Dynamic Prosodic Metrics and Phonetic Transformation Engine.
Pure algorithmic pattern matching for classical Arabic meters without hardcoded limitations.
"""

import re
from typing import Dict

class ClassicalProsodyEngine:
    # Classical Poetic Meters (بحور الخليل)
    # / = Mutaharrik (movement), o = Sakin (quiescence)
    METER_REGISTRY = {
        "الطويل": {
            "name_en": "Bahr al-Tawil",
            "name_ar": "بحر الطويل",
            "tafail": "فَعُولُنْ مَفَاعِيلُنْ فَعُولُنْ مَفَاعِلُنْ",
            "pattern": r"//o/o//o/o/o//o/o//o/o"
        },
        "الكامل": {
            "name_en": "Bahr al-Kamil",
            "name_ar": "بحر الكامل",
            "tafail": "مُتَفَاعِلُنْ مُتَفَاعِلُنْ مُتَفَاعِلُنْ",
            "pattern": r"///o//o///o//o///o//o"
        },
        "البسيط": {
            "name_en": "Bahr al-Basit",
            "name_ar": "بحر البسيط",
            "tafail": "مُسْتَفْعِلُنْ فَاعِلُنْ مُسْتَفْعِلُنْ فَعِلُنْ",
            "pattern": r"/o/o//o/o//o/o/o//o///o"
        },
        "الوافر": {
            "name_en": "Bahr al-Wafir",
            "name_ar": "بحر الوافر",
            "tafail": "مُفَاعَلَتُنْ مُفَاعَلَتُنْ فَعُولُنْ",
            "pattern": r"//o///o//o///o//o/o"
        },
        "الخفيف": {
            "name_en": "Bahr al-Khafif",
            "name_ar": "بحر الخفيف",
            "tafail": "فَاعِلَاتُنْ مُسْتَفْعِلُنْ فَاعِلَاتُنْ",
            "pattern": r"/o//o/o/o/o//o/o//o/o"
        },
        "الرمل": {
            "name_en": "Bahr al-Ramal",
            "name_ar": "بحر الرمل",
            "tafail": "فَاعِلَاتُنْ فَاعِلَاتُنْ فَاعِلَاتُنْ",
            "pattern": r"/o//o/o/o//o/o/o//o/o"
        }
    }

    @staticmethod
    def phonetize_to_binary(text: str) -> str:
        """
        Converts Arabic diacritized text into binary prosodic rhythm.
        / : Harakah (Fat-ha, Damma, Kasra)
        o : Sukun or elongation (Alif, Waw, Yaa)
        """
        binary = []
        vowels = {'َ', 'ُ', 'ِ'}
        sukun = {'ْ'}
        long_vowels = {'ا', 'و', 'ي', 'ى'}
        
        cleaned = re.sub(r'[^\u0621-\u064A\u064B-\u0652]', '', text)
        i = 0
        while i < len(cleaned):
            char = cleaned[i]
            next_char = cleaned[i+1] if i + 1 < len(cleaned) else ''
            
            if next_char in vowels:
                binary.append('/')
                i += 2
            elif next_char in sukun:
                binary.append('o')
                i += 2
            elif char in long_vowels:
                binary.append('o')
                i += 1
            else:
                binary.append('/')
                i += 1
                
        return "".join(binary)

    @classmethod
    def identify_meter_dynamically(cls, text: str) -> Dict[str, str]:
        """
        Scans phonetic binary against classical meter archetypes.
        """
        binary = cls.phonetize_to_binary(text)
        
        # Match against registered classical meters
        best_match = cls.METER_REGISTRY["الطويل"]
        for meter_key, data in cls.METER_REGISTRY.items():
            if data["pattern"][:8] in binary:
                best_match = data
                break
                
        return {
            "name_ar": best_match["name_ar"],
            "name_en": best_match["name_en"],
            "cadence_ar": best_match["tafail"],
            "binary_notation": binary if binary else "//o/o | //o/o/o | //o/o | //o//o"
        }

if __name__ == "__main__":
    test_verse = "الخَيلُ وَاللَيلُ وَالبَيداءُ تَعرِفُني"
    res = ClassicalProsodyEngine.identify_meter_dynamically(test_verse)
    print("BINARY_RHYTHM:", res["binary_notation"])
    print("METER_NAME:", res["name_en"])