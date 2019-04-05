DOCTOR_CHOICES = (
    ('1', ('김세혁')), ('2', ('노태훈')), ('3', ('others'))
)
SURGERY_CHOICES = (
    ('1', ('Operated case')), ('2', ('Non-Operated'))
)
SEX_CHOICES = (
    ('1', 'Female'), ('2', 'Male')
)
PATIENT_TYPE_CHOICES = (
    (1, 'new visitor'), (2, 'transferred from other hospital after treatment')
)
DISEASE_TYPE_CHOICES = (
    (1, "newly diagnosed"), (2, "remnant"), (3, "recurrent")
)
AXIS_CHOICES = (
    (1, 'extraaxial'), (2, 'intraaxial')
)
TENT_CHOICES = (
    (1, 'supratentorial'), (2, 'infratentorial'), (3, 'both')
)
CLASS_CHOICES = (
    ('1', 'Neuroepithelial tumors'), ('2', 'Sellar region tumors'), ('3', 'meningiomas'),
    ('4', 'Schwannomas'), ('5', 'others')
)
CC_CHOICES = (
    ('1', 'mass effect'), ('2', 'seizure'), ('3', 'focal deficit'), ('4', 'others')
)
NUESIGN_CHOICES = (
    ('1', 'IICP'), ('2', 'mental change'), ('3', 'cranial nerve palsy'), ('4', 'motor weakness'),
    ('5', 'cerebellar sign'), ('6', 'others'), ('7', 'mixed')
)
MENTAL_CHOICES = (
    (1, 'alert'), (2, 'confusion'), (3, 'lethargic'), (4, 'drowsy'), (5, 'stupor or worse')
)
KPS_CHOICES = (
    (100, '정상'), (90, '정상, minor Sx'), (80, '힘들지만 정상 생활 가능'), (70, 'self care 가능'),
    (60, '때때로 assist 요함'), (50, '자주 돌보아 주어야 함'), (40, '불구'), (30, '장해가 심한 불구'),
    (20, '매우 위중함'), (10, '사망 직전')
)

CTLESNO_CHOICES = (
    (1, "single"), (2, "multiple")
)
CTSITE_CHOICES = (
    (1, 'right'), (2, 'left'), (3, 'both'), (4, 'midline(including brainstem)')
)
CTHYDR_CHOICES = (
    (1, 'no'), (2, 'yes')
)
CTHEMO_CHOICES = (
    (1, 'no'), (2, 'yes')
)
CTCALC_CHOICES = (
    (1, 'no'), (2, 'yes')
)
THALLIUM_CHOICES = (
    (1, 'no uptake'), (2, 'uptake')
)
MIBI_CHOICES = (
    (1, 'no uptake'), (2, 'partial uptake'), (3, 'uptake')
)
PETRI_CHOICES = (
    (1, '18FDG'), (2, '1methionine'), (3, 'others')
)
PET_CHOICES = (
    (1, 'no uptake'), (2, 'partial uptake'), (3, 'uptake')
)
ANGIOCOM_CHOICES = (
    (1, 'no'), (2, 'yes')
)