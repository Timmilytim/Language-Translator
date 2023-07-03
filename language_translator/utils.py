from enum import Enum


class Language(str, Enum):
    AF = "af"
    AK = "ak"
    AM = "am"
    # AR
    # AS
    # AY
    # AZ
    # BE
    # BG
    # BHO
    # BM
    # BN
    # BS
    # CA
    # CEB
    # CKB
    # CO
    # CS
    # CY
    # DA
    # DE
    # DOI
    # DV
    # EE
    # EL
    EN = "en"
    # EO
    ES = "es"
    # ET
    # EU
    # FA
    # FI
    # FR
    # FY
    # GA
    # GD
    # GL
    # GN
    # GOM
    # GU
    # HA
    # HAW
    # HE
    # HI
    # HMN
    # HR
    # HT
    # HU
    # HY
    # ID
    # IG
    # ILO
    # IS
    # IT
    # IW
    # JA
    # JV
    # JW
    # KA
    # KK
    # KM
    # KN
    # KO
    # KRI
    # KU
    # KY
    # LA
    # LB
    # LG
    # LN
    # LO
    # LT
    # LUS
    # LV
    # MAI
    # MG
    # MI
    # MK
    # ML
    # MN
    # MNI_MTEI
    # MR
    # MS
    # MT
    # MY
    # NE
    # NL
    # NO
    # NSO
    # NY
    # OM
    # OR
    # PA
    # PL
    # PS
    # PT
    # QU
    # RO
    # RU
    # RW
    # SA
    # SD
    # SI
    # SK
    # SL
    # SM
    # SN
    # SO
    # SQ
    # SR
    # ST
    # SU
    # SV
    # SW
    # TA
    # TE
    # TG
    # TH
    # TI
    # TK
    # TL
    # TR
    # TS
    # TT
    # UG
    # UK
    # UR
    # UZ
    # VI
    # XH
    # YI
    # YO
    # ZH
    # ZH_CN
    # ZH_TW
    # ZU


class HTTPMethod(str, Enum):
    GET = "get"
    POST = "post"


class Format(str, Enum):
    HTML = "html"
    TEXT = "text"


class LanguageModel(str, Enum):
    PBMT = "pbmt"
    NMT = "nmt"
