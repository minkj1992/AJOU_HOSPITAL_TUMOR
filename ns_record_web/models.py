from django.db import models
from multiselectfield import MultiSelectField

from ns_record_web.choices import *
class NsCommonModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    extra_comment = models.TextField(null=True, verbose_name='Extra Comment', blank=True)

    class Meta:
        abstract = True


# Step1
class Patient(NsCommonModel):
    patient_id = models.CharField(max_length=255, verbose_name='Patient ID', primary_key=True)
    admission_date = models.DateField(verbose_name='Admission Date')
    DOCTOR_CHOICES = (
        ('김세혁', '김세혁'), ('유남규', '유남규'), ('노태훈', '노태훈'), ('박정언', '박정언'), ('안영환', '안영환'), ('윤수한', '윤수한'), ('임용철', '임용철'),
        ('정경원', '정경원'), ('조진모', '조진모'), ('최미선', '최미선'), ('최현용', '최현용'))

    doctor = models.CharField(max_length=255, choices=DOCTOR_CHOICES)
    name = models.CharField(max_length=255)
    GENDER_CHOICES = (
        ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')
    )
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    birthday = models.DateField(verbose_name='Date of Birth (DOB)')
    contact = models.CharField(max_length=255, verbose_name='Contact Information', blank=True)
    address = models.CharField(max_length=255, blank=True)

    EDUCATION_CHOICES = (
        ('Lack of schooling', 'Lack of schooling'),
        ('Elementary school graduation', 'Elementary school graduation'),
        ('Middle school graduation', 'Middle school graduation'),
        ('High school graduation', 'High school graduation'),
        ('University graduation', 'University graduation'),
        ('Master more', 'Master more'),
        ('Other', 'Other')
    )
    education = models.CharField(max_length=255, verbose_name='Education Status', choices=EDUCATION_CHOICES,
                                 default=EDUCATION_CHOICES[-1][0])
    education_detail = models.TextField(blank=True)
    EMPLOYMENT_CHOICES = (
        ('Inoccupation', 'Inoccupation'), ('Office Job', 'Office Job'),
        ('Specialized Job', 'Specialized Job'),
        ('Technical Post', 'Technical Post'),
        ('Driver', 'Driver'),
        ('Service Industry', 'Service Industry'),
        ('Student', 'Student'),
        ('Simple Work', 'Simple Work'),
        ('Self-employed', 'Self-employed'),
        ('Farmer Etc.', 'Farmer Etc.'),
        ('Police Officer', 'Police Officer'),
        ('Soldier', 'Soldier'),
        ('Other', 'Other')
    )
    employment = models.CharField(max_length=255, verbose_name='Employment (Job)', choices=EMPLOYMENT_CHOICES,
                                  default=EMPLOYMENT_CHOICES[-1][0])
    employment_detail = models.TextField(blank=True)
    INSURANCE_CHOICES = (
        ('Health insurance', 'Health insurance'),
        ('Car insurance', 'Car insurance'),
        ('Workers compensation', 'Workers compensation'),
        ('Medicaid', 'Medicaid'),
        ('Other', 'Other')
    )
    insurance = models.CharField(max_length=255, choices=INSURANCE_CHOICES, default=INSURANCE_CHOICES[-1][0])
    insurance_detail = models.TextField(blank=True)
    NATION_CHOICES = (
        ('KOREAN', 'KOREAN'),
        ('CHINA', 'CHINA'),
        ('ASIAN', 'ASIAN'),
        ('EUROPE', 'EUROPE'),
        ('AMERICA', 'AMERICA'),
        ('Other', 'Other')
    )
    nationality = models.CharField(max_length=255, choices=NATION_CHOICES, default=NATION_CHOICES[-1][0])
    nationality_detail = models.TextField(blank=True)

    RACE_CHOICES = (
        ('South Asian (Indian subcontient)', 'South Asian (Indian subcontient)'),
        ('Far Eastern Asian', 'Far Eastern Asian'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Middle Eastern', 'Middle Eastern'),
        ('Hispanic or Latino', 'Hispanic or Latino'),
        ('Other', 'Other')
    )
    race = models.CharField(max_length=255, choices=RACE_CHOICES, default=RACE_CHOICES[-1][0])
    race_detail = models.TextField(blank=True)

    INCOME_CHOICES = (('Unknown', 'Unknown'),
                      ('High 10%(up 4 million won/month)', 'High 10%(up 4 million won/month)'),
                      ('10-30%(3 million won/month)', '10-30%(3 million won/month)'),
                      ('30~70%(2 million won/month)', '30~70%(2 million won/month)'),
                      ('70~90%(1 million won/month)', '70~90%(1 million won/month)'),
                      ('Low 90%(under 1 million won/month)', 'Low 90%(under 1 million won/month)'),
                      ('Other', 'Other')
                      )
    income = models.CharField(max_length=255, choices=INCOME_CHOICES, default=INCOME_CHOICES[-1][0])
    income_detail = models.TextField(blank=True)

    MARRIAGE_CHOICES = (
        ('Never married', 'Never married'),
        ('Married', 'Married'),
        ('Domestic partnership', 'Domestic partnership'),
        ('Divorced', 'Divorced'),
        ('Separated', 'Separated'),
        ('Widowed', 'Widowed'),
        ('Other', 'Other')
    )
    marriage = models.CharField(max_length=255, choices=MARRIAGE_CHOICES, default=MARRIAGE_CHOICES[-1][0])
    marriage_detail = models.TextField(blank=True)

    RESIDENCE_CHOICES = (
        ('Alone', 'Alone'),
        ('Familty (Child)', 'Familty (Child)'),
        ('Spouse', 'Spouse'),
        ('Other', 'Other')
    )
    residence = models.CharField(max_length=255, choices=RESIDENCE_CHOICES, default=RESIDENCE_CHOICES[-1][0])
    residence_detail = models.TextField(blank=True)

    HANDED_CHOICES = (
        ('Righthanded', 'Righthanded'),
        ('Lefthanded', 'Lefthanded'),
        ('Both', 'Both'),
        ('Unknown', 'Unknown')
    )
    handedness = models.CharField(max_length=255, choices=HANDED_CHOICES, default=HANDED_CHOICES[-1][0])
    RELIGION_CHOICES = (
        ('None', 'None'),
        ('Catholic', 'Catholic'),
        ('Christian', 'Christian'),
        ('Buddhism', 'Buddhism'),
        ('Other', 'Other')
    )
    religion = models.CharField(max_length=255, choices=RELIGION_CHOICES, default=RELIGION_CHOICES[-1][0])
    religion_detail = models.TextField(blank=True)

    class Meta:
        ordering = ('-admission_date', 'pk')

    def __str__(self):
        return f'{self.name}/{self.pk}/{self.gender}/{self.birthday}'


class NsDataModel(NsCommonModel):
    NONE_STATUS = 1
    EXIST_STATUS = 2
    NON_EXIST_STATUS = 3
    STATUS_CHOICES = (
        (NONE_STATUS, 'None'),
        (EXIST_STATUS, 'Exist'),
        (NON_EXIST_STATUS, 'Non-Exist'),
    )
    check = models.IntegerField(choices=STATUS_CHOICES, default='1', verbose_name='History')
    confirm = models.BooleanField(default=False, verbose_name='Confirm')

    class Meta:
        abstract = True


# Step2
class Trauma(NsDataModel):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, verbose_name='Patient ID')
    injury_and_arrival_date_range = models.CharField(max_length=127,
                                                     verbose_name='Date & Time of Injury and Arrival')
    differ = models.CharField(max_length=255, blank=True,
                              verbose_name='Time interval between injury and arrival')
    TYPE_CHOICES = (
        ('None', 'None'),
        ('Direct to ER', 'Direct to ER'),
        ('Direct to T-bay', 'Direct to T-bay'),
        ('Transfer to ER', 'Transfer to ER'),
        ('Transfer to T-bay', 'Transfer to T-bay'),
        ('OPD', 'OPD'),
        ('Other', 'Other')
    )
    type_admission = models.CharField(max_length=255, choices=TYPE_CHOICES, blank=True,
                                      verbose_name='Type of Admission')
    type_admission_detail = models.TextField(blank=True, verbose_name='Type Admission Detail')

    TRANSFER_CHOICES = (
        ('None', 'None'),
        ('119 Ambulance', '119 Ambulance'),
        ('Private Ambulance', 'Private Ambulance'),
        ('Air Ambulance', 'Air Ambulance'),
        ('Another Car', 'Another Car'),
        ('Walk', 'Walk'),
        ('Other', 'Other')
    )

    transfer_method = models.CharField(max_length=255, choices=TRANSFER_CHOICES, blank=True,
                                       verbose_name='Transfer Method')
    transfer_method_detail = models.TextField(null=True, blank=True, verbose_name='Transfer Method Detail')

    PRE_ADMISSION_CHOICES = (
        ('None', 'None'),
        ('O2', 'O2'),
        ('Intubation', 'Intubation'),
        ('C-spine brace', 'C-spine brace'),
        ('Air way', 'Air way'),
        ('CPR', 'CPR'),
        ('Other', 'Other')
    )
    pre_admission = MultiSelectField(max_length=255, choices=PRE_ADMISSION_CHOICES, blank=True,
                                     verbose_name='Pre-admission treat')
    pre_admission_detail = models.TextField(null=True, blank=True, verbose_name='Pre-admission Detail')
    TYPE_OF_INJURY_CHOICES = (
        ('None', 'None'),
        ('Closed', 'Closed'),
        ('Blast', 'Blast'),
        ('Crush', 'Crush'),
        ('Penetrating', 'Penetrating'),
        ('Other', 'Other')
    )
    type_of_injury = MultiSelectField(max_length=255, choices=TYPE_OF_INJURY_CHOICES, null=True, blank=True,
                                      verbose_name='Type of Injury')
    type_of_injury_detail = models.TextField(null=True, blank=True, verbose_name='Type of Injury Detail')

    PLACE_OF_INJURY_CHOICES = (
        ('None', 'None'),
        ('Street/Highway', 'Street/Highway'),
        ('Home', 'Home'),
        ('Work/School', 'Work/School'),
        ('Recreational', 'Recreational'),
        ('Military', 'Military'),
        ('Unknown', 'Unknown'),
        ('Other', 'Other'),
    )
    place_of_injury = MultiSelectField(max_length=255, choices=PLACE_OF_INJURY_CHOICES, blank=True,
                                       verbose_name='Place of Injury')
    place_of_injury_detail = models.TextField(null=True, blank=True, verbose_name='Place of Injury Detail')

    DRUG_INTOXICATION_CHOICES = (
        ('None', 'None'),
        ('Alcohol', 'Alcohol'),
        ('Sedatives', 'Sedatives'),
        ('Sleep phils', 'Sleep phils'),
        ('Other', 'Other')
    )
    drug_intoxication = models.CharField(max_length=255, choices=DRUG_INTOXICATION_CHOICES, blank=True,
                                         verbose_name='Drug Intoxication')
    drug_intoxication_detail = models.TextField(blank=True, verbose_name='Drug Intoxication Detail')
    CAUSE_OF_INJURY_CHOICES = (
        ('Driver TA', 'Driver TA'),
        ('Passenger TA', 'Passenger TA'),
        ('Pedestrian TA', 'Pedestrian TA'),
        ('Bicycle', 'Bicycle'),
        ('Motorcycle', 'Motorcycle'),
        ('Other Vehicle', 'Other Vehicle'),
        ('Fall from height', 'Fall from height'),
        ('Slip down', 'Slip down'),
        ('Sports', 'Sports'),
        ('Violence', 'Violence'),
        ('Work related', 'Work related'),
        ('Other', 'Other')
    )
    cause_of_injury = models.CharField(max_length=255, choices=CAUSE_OF_INJURY_CHOICES, blank=True,
                                       verbose_name='Cause of Injury')
    cause_of_injury_detail = models.TextField(blank=True, verbose_name='Cause of Injury Detail')

    LOC_CHOICES = (
        (None, 'Unknown'), ('No', 'No'), ('Y', 'Yes'), ('Suspected', 'Suspected')
    )
    loc = models.CharField(max_length=255, blank=True, choices=LOC_CHOICES, verbose_name='LOC')
    loc_detail = models.CharField(max_length=255, null=True, blank=True, verbose_name='LOC Time(min)')

    def __str__(self):
        return str(self.patient)


# Step3
class Combine(NsDataModel):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, verbose_name='Patient ID')
    other_major_operation = models.CharField(max_length=255, null=True, blank=True,
                                             verbose_name='Other Major Operation')
    other_major_operation_detail = models.TextField(null=True, blank=True, verbose_name='Other Major Operation Detail')
    OPR_CHOICES = (
        ('None', 'None'),
        ('OS', 'OS'),
        ('TS', 'TS'),
        ('PS', 'PS'),
        ('ENT', 'ENT'),
        ('OPTH', 'OPTH'),
        ('CS', 'CS'),
        ('OMS', 'OMS'),
        ('URO', 'URO'),
        ('NS', 'NS'),
        ('Other', 'Other'),
    )
    other_major_office = MultiSelectField(max_length=255, null=True, choices=OPR_CHOICES, blank=True,
                                          verbose_name='Other Major Office')
    non_tbi_surgery_date = models.DateField(max_length=255, null=True, blank=True,
                                            verbose_name='Date of Non TBI Surgery')

    def __str__(self):
        return str(self.patient)


# Step4
class History(NsDataModel):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, verbose_name='Patient ID')
    PSYCHIATRIC_CHOICES = (
        ('No', 'No'),
        ('Anxirety', 'Anxirety'),
        ('Depression', 'Depression'),
        ('Sleep disorder', 'Sleep disorder'),
        ('Bipolar Disorder', 'Bipolar Disorder'),
        ('SPR', 'SPR'),
        ('PTS', 'PTS'),
        ('Other', 'Other')
    )
    psychiatric = MultiSelectField(max_length=255, choices=PSYCHIATRIC_CHOICES, null=True, blank=True,
                                   verbose_name='Psychiatric')
    psychiatric_detail = models.TextField(null=True, blank=True, verbose_name='Psychiatric Detail')
    CARDIOVASCULAR_CHOICES = (
        ('No', 'No'),
        ('HTN', 'HTN'),
        ('Arrhythmia', 'Arrhythmia'),
        ('IHD', 'IHD'),
        ('MI', 'MI'),
        ('VHD', 'VHD'),
        ('CHF', 'CHF'),
        ('Thromboembolic', 'Thromboembolic'),
        ('Other', 'Other')
    )
    cardiovascular = MultiSelectField(max_length=255, choices=CARDIOVASCULAR_CHOICES, null=True, blank=True,
                                      verbose_name='Cardiovascular')
    cardiovascular_detail = models.TextField(null=True, blank=True, verbose_name='Cardiovascular Detail')
    ENDO_CHOICES = (
        ('No', 'No'),
        ('Hyperlipidemia', 'Hyperlipidemia'),
        ('Thyroid disorder', 'Thyroid disorder'),
        ('DM type 1', 'DM type 1'),
        ('DM type 2', 'DM type 2'),
        ('BPH', 'BPH'),
        ('Hystrectomy', 'Hystrectomy'),
        ('Other', 'Other')
    )
    endocrine = MultiSelectField(max_length=255, choices=ENDO_CHOICES, null=True, blank=True, verbose_name='Endocrine')
    endocrine_detail = models.TextField(null=True, blank=True, verbose_name='Endocrine Detail')

    SPINAL_CHOICES = (
        ('No', 'No'),
        ('SCI', 'SCI'),
        ('Spinal dz', 'Spinal dz'),
        ('Other', 'Other')
    )
    spinal = MultiSelectField(max_length=255, choices=SPINAL_CHOICES, null=True, blank=True, verbose_name='Spinal')
    spinal_detail = models.TextField(null=True, blank=True, verbose_name='Spinal Detial')
    NEU_CHOICES = (
        ('No', 'No'),
        ('TIA', 'TIA'),
        ('Sz', 'Sz'),
        ('Epilepsy', 'Epilepsy'),
        ('HA-non migrain', 'HA-non migrain'),
        ('HA-migrain', 'HA-migrain'),
        ('CVA', 'CVA'),
        ('Vascular abnormality', 'Vascular abnormality'),
        ('MS', 'MS'),
        ('Degeneration', 'Degeneration'),
        ('Encephlaopathy', 'Encephlaopathy'),
        ('Brain tumor', 'Brain tumor'),
        ('Nerve sheath tumor', 'Nerve sheath tumor'),
        ('Other', 'Other')
    )
    neurologic = MultiSelectField(max_length=255, choices=NEU_CHOICES, null=True, blank=True, verbose_name='Neurologic')
    neurologic_detail = models.TextField(null=True, blank=True, verbose_name='Neurologic Detail')

    ONCOLOGIC_CHOICES = (
        ('No', 'No'),
        ('Leukemia', 'Leukemia'),
        ('Lymphoma', 'Lymphoma'),
        ('Myeloma', 'Myeloma'),
        ('Breast', 'Breast'),
        ('Oropharyngeal', 'Oropharyngeal'),
        ('Bone', 'Bone'),
        ('Thyroid', 'Thyroid'),
        ('Prostate', 'Prostate'),
        ('Lung', 'Lung'),
        ('GI', 'GI'),
        ('Liver', 'Liver'),
        ('Pancrease', 'Pancrease'),
        ('Kidney', 'Kidney'),
        ('Gonad', 'Gonad'),
        ('Skin', 'Skin'),
        ('Other', 'Other')
    )
    oncologic = MultiSelectField(max_length=255, choices=ONCOLOGIC_CHOICES, null=True, blank=True,
                                 verbose_name='Oncologic')
    oncologic_detail = models.TextField(null=True, blank=True, verbose_name='Oncologic Detail')
    GI_CHOICES = (
        ('No', 'No'),
        ('GERD', 'GERD'),
        ('GI bleeding', 'GI bleeding'),
        ('IBS', 'IBS'),
        ('Diarrhear', 'Diarrhear'),
        ('GI surguries', 'GI surguries'),
        ('Appendicitis', 'Appendicitis'),
        ('Other', 'Other')
    )
    gi = MultiSelectField(max_length=255, choices=GI_CHOICES, null=True, blank=True, verbose_name='GI')
    gi_detail = models.TextField(null=True, blank=True, verbose_name='GI Detail')
    HEP_CHOICES = (
        ('No', 'No'),
        ('Insufficiency', 'Insufficiency'),
        ('Hepatitis', 'Hepatitis'),
        ('LC', 'LC'),
        ('Transplant', 'Transplant'),
        ('Other', 'Other')
    )
    hepatic = MultiSelectField(max_length=255, choices=HEP_CHOICES, null=True, blank=True, verbose_name='Hepatic')
    hepatic_detail = models.TextField(null=True, blank=True, verbose_name='')
    HEM_CHOICES = (
        ('No', 'No'),
        ('Anemia', 'Anemia'),
        ('HIV positive', 'HIV positive'),
        ('Coagulopathy', 'Coagulopathy'),
        ('Other', 'Other')
    )
    hematologic = MultiSelectField(max_length=255, choices=HEM_CHOICES, null=True, blank=True,
                                   verbose_name='Hematologic')
    hematologic_detail = models.TextField(null=True, blank=True, verbose_name='Hematologic Detail')
    PULMONOLOGIC_CHOICES = (
        ('No', 'No'),
        ('COPD', 'COPD'),
        ('Asthma', 'Asthma'),
        ('Pneumonia', 'Pneumonia'),
        ('Pleural effusion', 'Pleural effusion'),
        ('TB', 'TB'),
        ('Emphysema', 'Emphysema'),
        ('Bronchitis', 'Bronchitis'),
        ('Respiratory failure', 'Respiratory failure'),
        ('Sleep apnea', 'Sleep apnea'),
        ('Pulmonary insufficiency', 'Pulmonary insufficiency'),
        ('Other', 'Other')
    )
    pulmonologic = MultiSelectField(max_length=255, choices=PULMONOLOGIC_CHOICES, null=True, blank=True,
                                    verbose_name='Pulmonologic')
    pulmonologic_detail = models.TextField(null=True, blank=True, verbose_name='Pulmonologic Detail')

    RENAL_CHOICES = (
        ('No', 'No'),
        ('Renal insufficiency', 'Renal insufficiency'),
        ('UTI', 'UTI'),
        ('Kidney stone', 'Kidney stone'),
        ('Mlnfection', 'Mlnfection'),
        ('KT', 'KT'),
        ('Other', 'Other')
    )
    renal = MultiSelectField(max_length=255, choices=RENAL_CHOICES, null=True, blank=True, verbose_name='Renal')
    renal_detail = models.TextField(null=True, blank=True, verbose_name='Reanl Detail')
    ENT_CHOICES = (
        ('No', 'No'),
        ('Lack of olfaction', 'Lack of olfaction'),
        ('Tinitus', 'Tinitus'),
        ('Sinusitis', 'Sinusitis'),
        ('Vision abnormality', 'Vision abnormality'),
        ('Hearing deficit', 'Hearing deficit'),
        ('Throat', 'Throat'),
        ('Other', 'Other')
    )
    ent = MultiSelectField(max_length=255, choices=ENT_CHOICES, null=True, blank=True, verbose_name='ENT')
    ent_detail = models.TextField(null=True, blank=True, verbose_name='ENT Detail')
    MUSCULOSKELETAL_CHOICES = (
        ('No', 'No'),
        ('Arthritis', 'Arthritis'),
        ('Osteoporosis', 'Osteoporosis'),
        ('Fibromyalgia', 'Fibromyalgia'),
        ('Hernia', 'Hernia'),
        ('Previous Fxe surgeries', 'Previous Fxe surgeries'),
        ('Low back pain', 'Low back pain'),
        ('Degenerative joint dz', 'Degenerative joint dz'),
        ('Other', 'Other')
    )
    musculoskeletal = MultiSelectField(max_length=255, choices=MUSCULOSKELETAL_CHOICES, null=True, blank=True,
                                       verbose_name='Musculoskeletal')
    musculoskeletal_detail = models.TextField(null=True, blank=True, verbose_name='Musculoskeletal Detail')
    DEV_CHOICES = (
        ('No', 'No'),
        ('Leanign Dz', 'Leanign Dz'),
        ('ADHD', 'ADHD'),
        ('ADD', 'ADD'),
        ('Developmental delay', 'Developmental delay'),
        ('Dyslexia', 'Dyslexia'),
        ('Other', 'Other')
    )
    developmental = MultiSelectField(max_length=255, choices=DEV_CHOICES, null=True, blank=True,
                                     verbose_name='Developmental')
    developmental_detail = models.TextField(null=True, blank=True, verbose_name='Developmental Detail')
    ANTICOAGULANTS_CHOICES = (('None', 'None'),
                              ('Coumarin derivative (Coumadin, Warfarin)', 'Coumarin derivative (Coumadin, Warfarin)'),
                              ('Heparin', 'Heparin'),
                              ('Low-molecular weight heparin', 'Low-molecular weight heparin'),
                              ('Inhibitor of factor Xa (eg.Rivaroxaban)', 'Inhibitor of factor Xa (eg.Rivaroxaban)'),
                              ('Direct thrombin Inhibitor (eg. dabigatran, argatroban, melagatran)',
                               'Direct thrombin Inhibitor (eg. dabigatran, argatroban, melagatran)'),
                              ('Antithrombin protein therapeutics (Atryn)', 'Antithrombin protein therapeutics (Atryn)')
                              )
    anticoagulants = MultiSelectField(max_length=255, choices=ANTICOAGULANTS_CHOICES, null=True, blank=True,
                                      verbose_name='Anticoagulants Detail')
    PLATELET_CHOICES = (
        ('None', 'None'),
        ('Aspirin', 'Aspirin'),
        ('ADP receptor inhibitors', 'ADP receptor inhibitors'),
        ('Clopidogrel (Plavix)', 'Clopidogrel (Plavix)'),
        ('Ticlopidine (Ticlid)', 'Ticlopidine (Ticlid)'),
        ('Parasugrel (Effient)', 'Parasugrel (Effient)'),
        ('Adenosine re-uptake inhibitor (eg. Persantin, Dipyridamole)',
         'Adenosine re-uptake inhibitor (eg. Persantin, Dipyridamole)'),
        ('Glycoprotein IIB/IIIA inhibitors (eg. Aggrastat)', 'Glycoprotein IIB/IIIA inhibitors (eg. Aggrastat)'),
    )
    platelet = MultiSelectField(max_length=255, choices=PLATELET_CHOICES, null=True, blank=True,
                                verbose_name='Platelet aggregation inhibitors')

    def __str__(self):
        return str(self.patient)


# Step5
class GCS(NsDataModel):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, verbose_name='Patient ID')
    arr_date = models.DateTimeField(null=True, blank=True, verbose_name='Date & Time of GCS')
    ARR_STAT_CHOICES = (
        ('Alert', 'Alert'), ('Drowsy', 'Drowsy'), ('Stupor', 'Stupor'), ('Semicoma', 'Semicoma'), ('Coma', 'Coma')
    )
    arr_status = models.CharField(max_length=255, null=True, blank=True, choices=ARR_STAT_CHOICES,
                                  verbose_name='Arrival Mental Status')
    arr_sbp = models.CharField(max_length=255, null=True, blank=True, verbose_name='Arrival SBP')
    arr_dbp = models.CharField(max_length=255, null=True, blank=True, verbose_name='Arrival DBP')
    arr_hr = models.CharField(max_length=255, null=True, blank=True, verbose_name='Arrival HR')
    arr_rr = models.CharField(max_length=255, null=True, blank=True, verbose_name='Arrival RR(회/min)')
    GEYE_CHOICES = (
        ('1', '1-No Response'),
        ('2', '2-To Pain'),
        ('3', '3-To Verbal Command'),
        ('4', '4-Spontaneously'),
        ('S', 'S-Untestable (Swollen)'),
    )
    arr_eye = models.CharField(max_length=255, choices=GEYE_CHOICES, null=True, blank=True,
                               verbose_name='Arrival GCS Eyes Opening')
    GVERBAL_CHOICES = (
        ('1', '1-No Response'),
        ('2', '2-Incomprehensible Sounds'),
        ('3', '3-Inappropriate Words'),
        ('4', '4-Disoriented & Converses'),
        ('5', '5-Oriented & Converses'),
        ('T', 'T-Untestable (Artificial Airway)'),
    )
    arr_verbal = models.CharField(max_length=255, choices=GVERBAL_CHOICES, null=True, blank=True,
                                  verbose_name='Arrival GCS Best Verbal Response')
    GMOTOR_CHOICES = (
        ('1', '1-No Response'),
        ('2', '2-Extension'),
        ('3', '3-Flexion Abnormal'),
        ('4', '4-Flexion Withdrawal'),
        ('5', '5-Localizes to Pain'),
        ('6', '6-Obeys Commands'),
        ('P', 'P-Untestable (Paralyzed)'),
    )
    arr_motor = models.CharField(max_length=255, choices=GMOTOR_CHOICES, null=True, blank=True,
                                 verbose_name='Arrival GCS Motor')
    arr_total = models.CharField(max_length=255, null=True, blank=True, verbose_name='Arrival GCS Total')
    arr_sum = models.CharField(max_length=255, null=True, blank=True, verbose_name='Arrival Sum')
    arr_rts = models.CharField(max_length=255, null=True, blank=True, verbose_name='Arrival RTS')
    MOTOR_CHOICES = (
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('U', 'U')
    )
    arr_rtupper = models.CharField(max_length=255, choices=MOTOR_CHOICES, null=True, blank=True,
                                   verbose_name='Arrival Rt.Upper')
    arr_ltupper = models.CharField(max_length=255, choices=MOTOR_CHOICES, null=True, blank=True,
                                   verbose_name='Arrival Lt.Upper')
    arr_rtlower = models.CharField(max_length=255, choices=MOTOR_CHOICES, null=True, blank=True,
                                   verbose_name='Arrival Rt.Lower')
    arr_ltlower = models.CharField(max_length=255, choices=MOTOR_CHOICES, null=True, blank=True,
                                   verbose_name='Arrival Lt.Lower')
    PPLR_CHOICES = (
        ('Untestable', 'Untestable'),
        ('Unknown', 'Unknown')
    )
    arr_pp_right = MultiSelectField(max_length=255, choices=PPLR_CHOICES, null=True, blank=True,
                                    verbose_name='Arrival Pupils Right')
    arr_pp_left = MultiSelectField(max_length=255, choices=PPLR_CHOICES, null=True, blank=True,
                                   verbose_name='Arrival Pupils Left')
    PPSIZE_CHOICES = (
        ('Unknown', 'Unknown'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),
        ('8', '8')
    )
    arr_pp_rtsize = models.CharField(max_length=255, choices=PPSIZE_CHOICES, null=True, blank=True,
                                     verbose_name='Arrival Pupils Right Size')
    arr_pp_ltsize = models.CharField(max_length=255, choices=PPSIZE_CHOICES, null=True, blank=True,
                                     verbose_name='Arrival Pupils Left Size')
    PPSHAPE_CHOICES = (
        ('Round', 'Round'),
        ('Oval', 'Oval'),
        ('Unknown', 'Unknown')
    )
    arr_pp_rtshape = models.CharField(max_length=255, choices=PPSHAPE_CHOICES, null=True, blank=True,
                                      verbose_name='Arrival Pupils Right Shape')
    arr_pp_ltshape = models.CharField(max_length=255, choices=PPSHAPE_CHOICES, null=True, blank=True,
                                      verbose_name='Arrival Pupils Left Shape')
    PPPROM_CHOICES = (
        ('Brisk', 'Brisk'),
        ('Sluggish', 'Sluggish'),
        ('Nonreactive', 'Nonreactive'),
        ('Untestable', 'Untestable'),
        ('Unknown', 'Unknown')
    )
    arr_pp_rtprompt = models.CharField(max_length=255, null=True, choices=PPPROM_CHOICES, blank=True,
                                       verbose_name='Arrival Pupils Right Prompt')
    arr_pp_ltprompt = models.CharField(max_length=255, null=True, choices=PPPROM_CHOICES, blank=True,
                                       verbose_name='Arrival Pupils Left Prompt')
    COCOA_CHOICES = ((None, 'Unknown'), ('Yes', 'Yes'), ('No', 'No'))
    arr_coa_correction = models.CharField(max_length=255, choices=COCOA_CHOICES, null=True, blank=True,
                                          verbose_name='Arrival Correction of coagulopathy')
    BLCOA_CHOICES = ((None, 'Unknown'), ('Yes', 'Yes'), ('No', 'No'))
    arr_coa_blood = models.CharField(max_length=255, choices=BLCOA_CHOICES, null=True, blank=True,
                                     verbose_name='Arrival Blood Transfusion')
    wor_date = models.DateTimeField(max_length=255, null=True, blank=True, verbose_name='Worst Date & Time of GCS')
    WORSTAT_CHOICES = (
        ('Alert', 'Alert'), ('Drowsy', 'Drowsy'), ('Stupor', 'Stupor'), ('Semicoma', 'Semicoma'), ('Coma', 'Coma')
    )
    wor_status = models.CharField(max_length=255, choices=WORSTAT_CHOICES, null=True, blank=True,
                                  verbose_name='Worst Mental Status')
    wor_sbp = models.CharField(max_length=255, null=True, blank=True, verbose_name='Worst SBP')
    wor_dbp = models.CharField(max_length=255, null=True, blank=True, verbose_name='Worst DBP')
    wor_hr = models.CharField(max_length=255, null=True, blank=True, verbose_name='Worst HR')
    wor_rr = models.CharField(max_length=255, null=True, blank=True, verbose_name='Worst RR(회/min)')
    wor_eye = models.CharField(max_length=255, choices=GEYE_CHOICES, null=True, blank=True,
                               verbose_name='Worst GCS Eyes Opening')
    wor_verbal = models.CharField(max_length=255, null=True, choices=GVERBAL_CHOICES, blank=True,
                                  verbose_name='Worst GCS Best Verbal Response')
    wor_motor = models.CharField(max_length=255, null=True, choices=GMOTOR_CHOICES, blank=True,
                                 verbose_name='Worst GCS Motor')
    wor_total = models.CharField(max_length=255, null=True, blank=True, verbose_name='Worst GCS Total')
    wor_sum = models.CharField(max_length=255, null=True, blank=True, verbose_name='Worst Sum')
    wor_rts = models.CharField(max_length=255, null=True, blank=True, verbose_name='Worst RTS')
    wor_rtupper = models.CharField(max_length=255, choices=MOTOR_CHOICES, null=True, blank=True,
                                   verbose_name='Worst Rt.Upper')
    wor_ltupper = models.CharField(max_length=255, choices=MOTOR_CHOICES, null=True, blank=True,
                                   verbose_name='Worst Lt.Upper')
    wor_rtlower = models.CharField(max_length=255, choices=MOTOR_CHOICES, null=True, blank=True,
                                   verbose_name='Worst Rt.Lower')
    wor_ltlower = models.CharField(max_length=255, choices=MOTOR_CHOICES, null=True, blank=True,
                                   verbose_name='Worst Lt.Lower')
    wor_pp_right = MultiSelectField(max_length=255, choices=PPLR_CHOICES, null=True, blank=True,
                                    verbose_name='Worst Pupils Right')
    wor_pp_left = MultiSelectField(max_length=255, choices=PPLR_CHOICES, null=True, blank=True,
                                   verbose_name='Worst Pupils Left')
    wor_pp_rtsize = models.CharField(max_length=255, choices=PPSIZE_CHOICES, null=True, blank=True,
                                     verbose_name='Worst Pupils Right Size')
    wor_pp_ltsize = models.CharField(max_length=255, choices=PPSIZE_CHOICES, null=True, blank=True,
                                     verbose_name='Worst Pupils Left Size')
    wor_pp_rtshape = models.CharField(max_length=255, choices=PPSHAPE_CHOICES, null=True, blank=True,
                                      verbose_name='Worst Pupils Right Shape')
    wor_pp_ltshape = models.CharField(max_length=255, choices=PPSHAPE_CHOICES, null=True, blank=True,
                                      verbose_name='Worst Pupils Left Shape')
    wor_pp_rtprompt = models.CharField(max_length=255, null=True, choices=PPPROM_CHOICES, blank=True,
                                       verbose_name='Worst Pupils Right Prompt')
    wor_pp_ltprompt = models.CharField(max_length=255, null=True, choices=PPPROM_CHOICES, blank=True,
                                       verbose_name='Worst Pupils Left Prompt')
    wor_coa_correction = models.CharField(max_length=255, choices=COCOA_CHOICES, null=True, blank=True,
                                          verbose_name='Worst Correction of coagulopathy')
    wor_coa_blood = models.CharField(max_length=255, choices=BLCOA_CHOICES, null=True, blank=True,
                                     verbose_name='Worst Blood Transfusion')
    wounds = models.TextField(null=True, blank=True, verbose_name='External Wounds')

    def __str__(self):
        return str(self.patient)


# Step6
class Diagnosis(NsDataModel):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, verbose_name='Patient ID')
    diagnosis = models.TextField(null=True, blank=True, verbose_name='Diagnosis')
    primary_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='Primary diagnosis Code')
    primary_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Primary diagnosis Name')
    SKULL_CHOICES = (
        ('None', 'None'),
        ('Linear Fx', 'Linear Fx'),
        ('Depressed Fx', 'Depressed Fx'),
        ('Basal Skull fracture', 'Basal Skull fracture'),
        ('Diastic Fx', 'Diastic Fx'),
        ('Frontal sinus Fx', 'Frontal sinus Fx'),
        ('Temporal bone fracture', 'Temporal bone fracture'),
        ('FCCD', 'FCCD'),
        ('Pneumocephalus', 'Pneumocephalus'),
        ('CSF leakage', 'CSF leakage')
    )
    skull = MultiSelectField(max_length=255, choices=SKULL_CHOICES, null=True, blank=True, verbose_name='Skull Injury')
    INJURY_POSITION_CHOICES = (
        ('None', 'None'),
        ('Right', 'Right'),
        ('Left', 'Left'),
        ('Bilateral', 'Bilateral')
    )
    injury_position = MultiSelectField(max_length=255, choices=INJURY_POSITION_CHOICES, null=True, blank=True,
                                       verbose_name='Injury Position')
    POSITION_CHOICES = (
        ('None', 'None'),
        ('Frontal', 'Frontal'),
        ('Temporal', 'Temporal'),
        ('Parietal', 'Parietal'),
        ('Occipital', 'Occipital'),
        ('Cerebellum', 'Cerebellum'),
        ('Other', 'Other')
    )
    position = MultiSelectField(max_length=255, choices=POSITION_CHOICES, null=True, blank=True,
                                verbose_name='Position')
    position_detail = models.TextField(null=True, blank=True, verbose_name='Position Detail')
    HEMORRHAGE_CHOICES = (
        ('None', 'None'),
        ('SDH', 'SDH'),
        ('EDH', 'EDH'),
        ('ICH', 'ICH'),
        ('Contusion', 'Contusion')
    )
    hemorrhage = MultiSelectField(max_length=255, choices=HEMORRHAGE_CHOICES, null=True, blank=True,
                                  verbose_name='Hemorrhage Injury')

    HEMORRHAGE_INJURY_POSITION_CHOICES = (
        ('None', 'None'),
        ('Right', 'Right'),
        ('Left', 'Left'),
        ('Bilateral', 'Bilateral')
    )
    hemorrhage_injury_position = MultiSelectField(max_length=255, choices=HEMORRHAGE_INJURY_POSITION_CHOICES, null=True,
                                                  blank=True,
                                                  verbose_name='Injury Position')
    POSIT_CHOICES = (
        ('None', 'None'),
        ('Frontal', 'Frontal'),
        ('Temporal', 'Temporal'),
        ('Parietal', 'Parietal'),
        ('Occipital', 'Occipital'),
        ('Cerebellum', 'Cerebellum'),
        ('Other', 'Other')
    )
    hemorrhage_position = MultiSelectField(max_length=255, choices=POSIT_CHOICES, null=True, blank=True,
                                           verbose_name='Hemorrhage Position')
    hemorrhage_position_detail = models.TextField(null=True, blank=True, verbose_name='Hemorrhage Position Detail')
    DIFFUSE_CHOICES = (
        ('None', 'None'),
        ('SAH', 'SAH'),
        ('IVH', 'IVH'),
        ('DAI', 'DAI')
    )
    diffuse = MultiSelectField(max_length=255, choices=DIFFUSE_CHOICES, null=True, blank=True,
                               verbose_name='Diffuse Injury')
    VASCULAR_CHOICES = (
        ('Absent', 'Absent'),
        ('Exist', 'Exist')
    )
    vascular = models.CharField(max_length=255, choices=VASCULAR_CHOICES, null=True, blank=True,
                                verbose_name='Vascular Injury')
    vascular_detail = models.TextField(null=True, blank=True, verbose_name='Vascular Injury Detail')

    PENETRATING_CHOICES = (
        ('Absent', 'Absent'),
        ('Penetrating Only', 'Penetrating Only'),
        ('Foreign body', 'Foreign body')
    )
    penetrating = models.CharField(max_length=255, choices=PENETRATING_CHOICES, null=True, blank=True,
                                   verbose_name='Penetrating')
    penetrating_detail = models.TextField(null=True, blank=True, verbose_name='Penetrating Detail')
    FORE_CHOICES = (
        ('Absent', 'Absent'),
        ('Penetrating Only', 'Penetrating Only')
    )
    fore = models.CharField(max_length=255, choices=FORE_CHOICES, null=True, blank=True, verbose_name='Foreign body')
    fore_detail = models.TextField(null=True, blank=True, verbose_name='Foreign Body Detail')

    def __str__(self):
        return str(self.patient)


# Step7
class Injury(NsDataModel):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, verbose_name='Patient ID')
    AIS_CHOICES = (
        (0, 'No Injury'),
        (1, 'Minor'),
        (2, 'Moderate'),
        (3, 'Serious'),
        (4, 'Severe'),
        (5, 'Critical'),
        (6, 'Unsurvivable'),

    )
    head_neck = models.IntegerField(verbose_name='Head, Neck', choices=AIS_CHOICES, default=AIS_CHOICES[0][0])
    face = models.IntegerField(verbose_name='Face', choices=AIS_CHOICES, default=AIS_CHOICES[0][0])
    chest = models.IntegerField(verbose_name='Chest', choices=AIS_CHOICES, default=AIS_CHOICES[0][0])
    abdomen = models.IntegerField(verbose_name='Abdomen', choices=AIS_CHOICES, default=AIS_CHOICES[0][0])
    extremity = models.IntegerField(verbose_name='Extremity', choices=AIS_CHOICES, default=AIS_CHOICES[0][0])
    external = models.IntegerField(verbose_name='External', choices=AIS_CHOICES, default=AIS_CHOICES[0][0])
    iss_score = models.IntegerField(verbose_name='ISS Score', default=0)

    MARS_CHOICES = (
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
        ('V', 'V'),
        ('VI', 'VI')
    )
    marshall_score = models.CharField(max_length=255, choices=MARS_CHOICES, null=True, blank=True,
                                      verbose_name='Marshall Score')
    def __str__(self):
        return str(self.patient)



# Step8
class Monitor(NsDataModel):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, verbose_name='Patient ID')
    TIMING_ICP_CHOICES = (
        ('Init', 'Init'),
        ('After Operation', 'After Operation'),
        ('Init + After Operation', 'Init + After Operation')
    )
    icp_timing = models.CharField(max_length=255, choices=TIMING_ICP_CHOICES, null=True, blank=True,
                                  verbose_name='Timing of ICP monitoring')
    TYPE_ICP_CHOICES = (
        ('Parenchymal', 'Parenchymal'),
        ('Subdural', 'Subdural'),
        ('EVD', 'EVD')
    )
    icp_type = models.CharField(max_length=255, choices=TYPE_ICP_CHOICES, null=True, blank=True,
                                verbose_name='Type of ICP monitoring')
    icp_start_date = models.DateField(max_length=255, null=True, blank=True,
                                      verbose_name='Start date of ICP monitoring')
    icp_end_date = models.DateField(max_length=255, null=True, blank=True, verbose_name='End date of ICP monitoring')
    LOC_ICP_CHOICES = (
        ('Rt Kocher', 'Rt Kocher'),
        ('Lt Kocher', 'Lt Kocher'),
        ('Subdural', 'Subdural')
    )
    icp_location = models.CharField(max_length=255, choices=LOC_ICP_CHOICES, null=True, blank=True,
                                    verbose_name='Location of ICP monitoring')
    REASON_ICP_CHOICES = (
        ('None', 'None'),
        ('Monitor/catheter failure', 'Monitor/catheter failure'),
        ('Patient considered unsalvageable', 'Patient considered unsalvageable'),
        ('Patient died', 'Patient died'),
        ('Clinically no longer required', 'Clinically no longer required'),
        ('Other', 'Other')
    )
    icp_reason = MultiSelectField(max_length=255, choices=REASON_ICP_CHOICES, null=True, blank=True,
                                  verbose_name='Reason for ICP')
    icp_reason_detail = models.TextField(null=True, blank=True, verbose_name='Reason for ICP Detail')
    TIMING_EVD_CHOICES = (
        ('Init', 'Init'),
        ('After Operation', 'After Operation'),
        ('Init + After Operation', 'Init + After Operation')
    )
    evd_timing = models.CharField(max_length=255, choices=TIMING_EVD_CHOICES, null=True, blank=True,
                                  verbose_name='Timing of EVD')
    evd_start_date = models.DateField(max_length=255, null=True, blank=True, verbose_name='Start date of EVD')
    evd_end_date = models.DateField(max_length=255, null=True, blank=True, verbose_name='End date of EVD')
    LOC_EVD_CHOICES = (
        ('Rt Kocher', 'Rt Kocher'),
        ('Lt Kocher', 'Lt Kocher'),
        ('Subdural', 'Subdural')
    )
    evd_location = models.CharField(max_length=255, choices=LOC_EVD_CHOICES, null=True, blank=True,
                                    verbose_name='Location of EVD')
    REASON_EVD_CHOICES = (
        ('None', 'None'),
        ('Monitor/catheter failure', 'Monitor/catheter failure'),
        ('Patient considered unsalvageable', 'Patient considered unsalvageable'),
        ('Patient died', 'Patient died'),
        ('Clinically no longer required', 'Clinically no longer required'),
        ('Other', 'Other')
    )
    evd_reason = MultiSelectField(max_length=255, choices=REASON_EVD_CHOICES, null=True, blank=True,
                                  verbose_name='Reason for EVD')
    evd_reason_detail = models.TextField(null=True, blank=True, verbose_name='Reason for EVD Detail')
    TIMING_JB_CHOICES = (
        ('Init', 'Init'),
        ('After Operation', 'After Operation'),
        ('Init + After Operation', 'Init + After Operation')
    )
    jb_timing = models.CharField(max_length=255, choices=TIMING_JB_CHOICES, null=True, blank=True,
                                 verbose_name='Timing of Jugular bulb')
    jb_start_date = models.DateField(max_length=255, null=True, blank=True, verbose_name='Start date of Jugular bulb')
    jb_end_date = models.DateField(max_length=255, null=True, blank=True, verbose_name='End date of Jugular bulb')
    LOC_JB_CHOICES = (
        ('Right', 'Right'),
        ('Left', 'Left')
    )
    jb_location = models.CharField(max_length=255, choices=LOC_JB_CHOICES, null=True, blank=True,
                                   verbose_name='Location of Jugular bulb')
    REASON_JB_CHOICES = (
        ('None', 'None'),
        ('Monitor/catheter failure', 'Monitor/catheter failure'),
        ('Patient considered unsalvageable', 'Patient considered unsalvageable'),
        ('Patient died', 'Patient died'),
        ('Clinically no longer required', 'Clinically no longer required'),
        ('Other', 'Other')
    )
    jb_reason = MultiSelectField(max_length=255, choices=REASON_JB_CHOICES, null=True, blank=True,
                                 verbose_name='Reason for JB')
    jb_reason_detail = models.TextField(null=True, blank=True, verbose_name='Reason for JB Detail')
    TIMING_BIS_CHOICES = (
        ('Init', 'Init'),
        ('After Operation', 'After Operation'),
        ('Init + After Operation', 'Init + After Operation')
    )
    bis_timing = models.CharField(max_length=255, choices=TIMING_BIS_CHOICES, null=True, blank=True,
                                  verbose_name='Timing of BIS')
    bis_start_date = models.DateField(max_length=255, null=True, blank=True, verbose_name='Start date of BIS')
    bis_end_date = models.DateField(max_length=255, null=True, blank=True, verbose_name='End date of BIS')
    LOC_BIS_CHOICES = (
        ('None', 'None'),
        ('Forhead', 'Forhead')
    )
    bis_location = models.CharField(max_length=255, choices=LOC_BIS_CHOICES, null=True, blank=True,
                                    verbose_name='Location of BIS')
    REASON_BIS_CHOICES = (
        ('None', 'None'),
        ('Monitor/catheter failure', 'Monitor/catheter failure'),
        ('Patient considered unsalvageable', 'Patient considered unsalvageable'),
        ('Patient died', 'Patient died'),
        ('Clinically no longer required', 'Clinically no longer required'),
        ('Other', 'Other')
    )
    bis_reason = MultiSelectField(max_length=255, choices=REASON_BIS_CHOICES, null=True, blank=True,
                                  verbose_name='Reason for Bis')
    bis_reason_detail = models.TextField(null=True, blank=True, verbose_name='Reason for Bis Detail')

    def __str__(self):
        return str(self.patient)


# Step9, 1:N
class Surgery(NsDataModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Patient ID')
    surgery_no = models.IntegerField(null=True, blank=True, verbose_name='No of Surgery')
    AIM_CHOICES = (
        ('None', 'None'),
        ('ICP relief', 'ICP relief'),
        ('Hematoma removal', 'Hematoma removal'),
        ('Foreign body removal', 'Foreign body removal'),
        ('Repair of CSF leak', 'Repair of CSF leak'),
        ('Reconstruction of Skull', 'Reconstruction of Skull'),
        ('Other', 'Other')
    )
    aim = MultiSelectField(max_length=255, choices=AIM_CHOICES, null=True, blank=True, verbose_name='Aim of Surgery')
    aim_detail = models.TextField(null=True, blank=True, verbose_name='Aim of Surgery Detail')
    TYPE_CHOICES = (
        ('None', 'None'),
        ('Craniotomy', 'Craniotomy'),
        ('Craniectomy', 'Craniectomy'),
        ('Lobectomy', 'Lobectomy'),
        ('Drainage catheter', 'Drainage catheter'),
        ('Craniopalsty', 'Craniopalsty'),
        ('Frontal sinus cranialization', 'Frontal sinus cranialization'),
        ('Other', 'Other')
    )
    typeof = MultiSelectField(max_length=255, choices=TYPE_CHOICES, null=True, blank=True,
                              verbose_name='Type of Surgery')
    typeof_detail = models.TextField(null=True, blank=True, verbose_name='Type of Surgery Detail')
    DIRECT_CHOICES = (
        ('Right', 'Right'),
        ('Left', 'Left'),
        ('Bilateral', 'Bilateral'),
        ('Occpital', 'Occpital'),
        ('Posterior fossa', 'Posterior fossa')
    )
    direction = models.CharField(max_length=255, choices=DIRECT_CHOICES, null=True, blank=True,
                                 verbose_name='Direction of Surgery')
    INTRAEVD_CHOICES = (
        (None, 'None'),
        ('Done', 'Done')
    )
    intraevd = models.CharField(max_length=255, choices=INTRAEVD_CHOICES, null=True, blank=True,
                                verbose_name='Intraoperative EVD')
    INTRASONO_CHOICES = (
        (None, 'None'),
        ('Done', 'Done')
    )
    intrasono = models.CharField(max_length=255, choices=INTRASONO_CHOICES, null=True, blank=True,
                                 verbose_name='Intraoperative Sonography')
    surgery_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Name of Surgery')
    surgery_result = models.TextField(null=True, blank=True, verbose_name='Result of Surgery')
    orroom_date = models.DateTimeField(max_length=255, null=True, blank=True,
                                       verbose_name='Date & time of tranfer to OR room')
    surgery_start_date = models.DateTimeField(max_length=255, null=True, blank=True,
                                              verbose_name='Start time of Surgery')
    surgery_end_date = models.DateTimeField(max_length=255, null=True, blank=True, verbose_name='End time of Surgery')
    blood_loss = models.CharField(max_length=255, null=True, blank=True, verbose_name='Blood loss')
    ffp = models.CharField(max_length=255, null=True, blank=True, verbose_name='Transfusion(FFP)')
    prbc = models.CharField(max_length=255, null=True, blank=True, verbose_name='Transfusion(PRBC)')
    plt = models.CharField(max_length=255, null=True, blank=True, verbose_name='Transfusion(PLT)')
    DURO_CHOICES = (
        ('None', 'None'),
        ('Bovie Plenicordium', 'Bovie Plenicordium'),
        ('Synthetic material', 'Synthetic material'),
        ('Autologus tissue', 'Autologus tissue'),
        ('Hemostatic materials', 'Hemostatic materials'),
        ('Other', 'Other')
    )
    duroplasty = models.CharField(max_length=255, choices=DURO_CHOICES, null=True, blank=True,
                                  verbose_name='Duroplasty')
    duroplasty_detail = models.TextField(null=True, blank=True, verbose_name='Duroplasty Detail')

    def __str__(self):
        return str(self.patient)


# Step10
class NonSurgicalTreatment(NsDataModel):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, verbose_name='Patient ID')
    SEDA_CHOICES = (
        ('None', 'None'),
        ('Entobar', 'Entobar'),
        ('Pentothal', 'Pentothal'),
        ('Midazolam + Vecaron', 'Midazolam + Vecaron'),
        ('Midazolam', 'Midazolam'),
        ('Other', 'Other')
    )
    sedation = MultiSelectField(max_length=255, choices=SEDA_CHOICES, null=True, blank=True,
                                verbose_name='Sedation Drug')
    sedation_detail = models.TextField(null=True, blank=True, verbose_name='Sedation Drug Detail')
    HYPO_CHOICES = (
        ('None', 'None'),
        ('Thermia Blanket', 'Thermia Blanket'),
        ('Artic sun', 'Artic sun'),
        ('Cool gard', 'Cool gard'),
        ('Other', 'Other')
    )
    hypothermia = MultiSelectField(max_length=255, choices=HYPO_CHOICES, null=True, blank=True,
                                   verbose_name='Hypothermia')
    hypo_detail = models.TextField(null=True, blank=True, verbose_name='Hypothermia Detail')
    HYPE_CHOICES = (
        ('None', 'None'),
        ('Mannitol', 'Mannitol'),
        ('Hypertonic Saline', 'Hypertonic Saline'),
        ('Other', 'Other')
    )
    hyperosmolar = MultiSelectField(max_length=255, choices=HYPE_CHOICES, null=True, blank=True,
                                    verbose_name='Hyperosmolar Detail')
    hyper_detail = models.TextField(null=True, blank=True, verbose_name='Hyperosmolar Detail')
    BOOL_CHOICES = (
        (None, 'None'),
        ('Yes', 'Yes')
    )
    crrt = models.CharField(max_length=255, choices=BOOL_CHOICES, null=True, blank=True, verbose_name='CRRT')
    nogas = models.CharField(max_length=255, choices=BOOL_CHOICES, null=True, blank=True, verbose_name='NO Gas')

    def __str__(self):
        return str(self.patient)


# Step11
class Treatment(NsDataModel):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, verbose_name='Patient ID')
    NEU_CHOICES = (
        ('No', 'No'),
        ('Rhinorrhea', 'Rhinorrhea'),
        ('Otorrhea', 'Otorrhea'),
        ('Meningitis', 'Meningitis'),
        ('Seizure', 'Seizure'),
        ('Ventriculitis', 'Ventriculitis'),
        ('Stroke', 'Stroke'),
        ('Neurogenic Shock', 'Neurogenic Shock'),
        ('Other CSF Leak', 'Other CSF Leak'),
        ('Other', 'Other')
    )

    neuro = MultiSelectField(max_length=255, choices=NEU_CHOICES, null=True, blank=True, verbose_name='Neurological')
    neuro_detail = models.TextField(null=True, blank=True, verbose_name='Neurological Detail')

    CAR_CHOICES = (
        ('No', 'No'),
        ('Cardiac Arrest', 'Cardiac Arrest'),
        ('CHF', 'CHF'),
        ('DVT', 'DVT'),
        ('Major Arrhythmia', 'Major Arrhythmia'),
        ('MI', 'MI'),
        ('Hypertension Requiring Treatment', 'Hypertension Requiring Treatment'),
        ('Hypotension Requiring Treatment', 'Hypotension Requiring Treatment'),
        ('Other', 'Other')
    )
    cardio = MultiSelectField(max_length=255, choices=CAR_CHOICES, null=True, blank=True, verbose_name='Cardiovascular')
    cardio_detail = models.TextField(null=True, blank=True, verbose_name='Cardiovascular Detail')

    HEMA_CHOICES = (
        ('No', 'No'),
        ('Coagulopathy', 'Coagulopathy'),
        ('DIC', 'DIC'),
        ('Anemia Requiring Treatment', 'Anemia Requiring Treatment'),
        ('Other', 'Other')
    )
    hematopoetic = MultiSelectField(max_length=255, choices=HEMA_CHOICES, null=True, blank=True,
                                    verbose_name='Hematopoetic')
    hematopoetic_detail = models.TextField(null=True, blank=True, verbose_name='Hematopoetic Detail')
    PUL_CHOICES = (
        ('No', 'No'),
        ('ARDS', 'ARDS'),
        ('Fat Embolus', 'Fat Embolus'),
        ('Pulmonary Embolism', 'Pulmonary Embolism'),
        ('Pleural Effusions', 'Pleural Effusions'),
        ('Pneumonia', 'Pneumonia'),
        ('Presumed Pneumonia', 'Presumed Pneumonia'),
        ('Respiratory Failure', 'Respiratory Failure'),
        ('VAP', 'VAP'),
        ('Asthma', 'Asthma'),
        ('Other', 'Other')
    )
    pulmonary = MultiSelectField(max_length=255, choices=PUL_CHOICES, null=True, blank=True, verbose_name='Pulmonary')
    pulmonary_detail = models.TextField(null=True, blank=True, verbose_name='Pulmonary Detail')
    GIAB_CHOICES = (
        ('No', 'No'),
        ('Abdominal Compartment Syndrome', 'Abdominal Compartment Syndrome'),
        ('Bowel Obstruction', 'Bowel Obstruction'),
        ('GI Bleed', 'GI Bleed'),
        ('Hepatic Encephalopathy', 'Hepatic Encephalopathy'),
        ('Hepatic Failure', 'Hepatic Failure'),
        ('Pancreatitis', 'Pancreatitis'),
        ('Renal Failure', 'Renal Failure'),
        ('Other', 'Other')
    )
    giab = MultiSelectField(max_length=255, choices=GIAB_CHOICES, null=True, blank=True, verbose_name='GI/Abdomen')
    giab_detail = models.TextField(null=True, blank=True, verbose_name='GI/Abdomen Detail')

    WOUND_CHOICES = (
        ('No', 'No'),
        ('Abcess', 'Abcess'),
        ('Seroma/hematoma/bleeding', 'Seroma/hematoma/bleeding'),
        ('Wound Dehiscence', 'Wound Dehiscence'),
        ('Wound Infection', 'Wound Infection'),
        ('Pressure Ulcer', 'Pressure Ulcer'),
        ('Other', 'Other')
    )
    wound = MultiSelectField(max_length=255, choices=WOUND_CHOICES, null=True, blank=True, verbose_name='Wound')
    wound_detail = models.TextField(null=True, blank=True, verbose_name='Wound Detail')
    LAB_CHOICES = (
        ('No', 'No'),
        ('Hypoglycemia', 'Hypoglycemia'),
        ('Hyperglycemia', 'Hyperglycemia'),
        ('Hyponatremia', 'Hyponatremia'),
        ('Hypernatremia', 'Hypernatremia'),
        ('Other', 'Other')
    )
    lab = MultiSelectField(max_length=255, choices=LAB_CHOICES, null=True, blank=True, verbose_name='Lab Abnomarlities')
    lab_detail = models.TextField(null=True, blank=True, verbose_name='Lab Abnomarlities Detail')

    INFE_CHOICES = (
        ('No', 'No'),
        ('Bacteremia', 'Bacteremia'),
        ('Fever(Temp>38.5) of unknown origin', 'Fever(Temp>38.5) of unknown origin'),
        ('Presumed Infection', 'Presumed Infection'),
        ('Sepsis', 'Sepsis'),
        ('Septicemia', 'Septicemia'),
        ('UTI', 'UTI'),
        ('Septic Shock', 'Septic Shock'),
        ('Other', 'Other')
    )
    infection = MultiSelectField(max_length=255, choices=INFE_CHOICES, null=True, blank=True,
                                 verbose_name='Infection other than pneumonia / Wound')
    infection_detail = models.TextField(null=True, blank=True,
                                        verbose_name='Infection other than pneumonia / Wound Detail')
    OTHER_CHOICES = (
        ('No', 'No'),
        ('MSOF', 'MSOF'),
        ('Transfusion', 'Transfusion')
    )
    othercomp = MultiSelectField(max_length=255, choices=OTHER_CHOICES, null=True, blank=True,
                                 verbose_name='Other Complications')
    othercomp_detail = models.TextField(null=True, blank=True, verbose_name='Other Complications Detail')
    comp_comment = models.TextField(null=True, blank=True, verbose_name='Extra comment for complication')
    DIS_CHOICES = (
        ('Death', 'Death'),
        ('Home', 'Home'),
        ('Hopeless', 'Hopeless'),
        ('Transfer to Hospital', 'Transfer to Hospital'),
        ('Transfer to other dept', 'Transfer to other dept'),
        ('Other', 'Other')
    )
    discharge_type = models.CharField(max_length=255, choices=DIS_CHOICES, null=True, blank=True,
                                      verbose_name='Type of Discharge')
    DEATH_CHOICES = (
        ('CNS related', 'CNS related'),
        ('Bleeding', 'Bleeding'),
        ('Sepsis/dic', 'Sepsis/dic'),
        ('Cardiac arrest', 'Cardiac arrest'),
        ('Respiratory arrest', 'Respiratory arrest'),
        ('Unknown', 'Unknown')
    )
    causedeath = models.CharField(max_length=255, choices=DEATH_CHOICES, null=True, blank=True,
                                  verbose_name='Cause of death')
    discharge_date = models.DateField(max_length=255, null=True, blank=True, verbose_name='Date of Discharge')

    def __str__(self):
        return str(self.patient)


# Step12, 1:N
class Assessment(NsDataModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Patient ID')
    resultno = models.IntegerField(null=True, blank=True)
    date = models.DateField(max_length=255, null=True, blank=True, verbose_name='Date')
    GEYE_CHOICES = (
        ('1', '1-No Response'),
        ('2', '2-To Pain'),
        ('3', '3-To Verbal Command'),
        ('4', '4-Spontaneously'),
        ('S', 'S-Untestable (Swollen)'),
    )
    gcs_eye = models.CharField(max_length=255, choices=GEYE_CHOICES, null=True, blank=True,
                               verbose_name='GCS Eyes Opening')
    GVERBAL_CHOICES = (
        ('1', '1-No Response'),
        ('2', '2-Incomprehensible Sounds'),
        ('3', '3-Inappropriate Words'),
        ('4', '4-Disoriented & Converses'),
        ('5', '5-Oriented & Converses'),
        ('T', 'T-Untestable (Artificial Airway)'),
    )
    gcs_verbal = models.CharField(max_length=255, choices=GVERBAL_CHOICES, null=True, blank=True,
                                  verbose_name='GCS Best Verbal Response')
    GMOTOR_CHOICES = (
        ('1', '1-No Response'),
        ('2', '2-Extension'),
        ('3', '3-Flexion Abnormal'),
        ('4', '4-Flexion Withdrawal'),
        ('5', '5-Localizes to Pain'),
        ('6', '6-Obeys Commands'),
        ('P', 'P-Untestable (Paralyzed)'),
    )
    gcs_motor = models.CharField(max_length=255, choices=GMOTOR_CHOICES, null=True, blank=True,
                                 verbose_name='GCS Motor')
    gcs_total = models.CharField(max_length=255, null=True, blank=True, verbose_name='GCS Total')
    gcs_sum = models.CharField(max_length=255, null=True, blank=True, verbose_name='GCS Sum')
    mmse = models.CharField(max_length=255, null=True, blank=True, verbose_name='MMSE')
    GOSE_CHOICES = (
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')
    )
    gose = models.CharField(max_length=255, choices=GOSE_CHOICES, null=True, blank=True, verbose_name='GOSE')
    bathel = models.CharField(max_length=255, null=True, blank=True, verbose_name='Bathel Index')
    drs = models.CharField(max_length=255, null=True, blank=True, verbose_name='DRS')
    MRS_CHOICES = (
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')
    )
    mrs = models.CharField(max_length=255, choices=MRS_CHOICES, null=True, blank=True, verbose_name='MRS')

    def __str__(self):
        return str(self.patient)

# TUMOR MODELS
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

######################################
class Overall(models.Model):
    # patient_id = models.CharField(max_length=255,verbose_name='Patient ID', primary_key=True)
    year = models.CharField(db_column='Year', max_length=20, blank=True, null=True)  # Field name made lowercase.
    # 등록환자의 일련번호
    ajbtno = models.CharField(db_column='AJBTno', max_length=10, blank=True, null=True)
    doctor = models.CharField(db_column='Doctor', max_length=10, blank=True, null=True,
                              choices=DOCTOR_CHOICES)
    surgery = models.CharField(db_column='Sergery', max_length=10, blank=True, null=True,
                               choices=SURGERY_CHOICES)
    sergno = models.IntegerField(db_column='Sergno', blank=True, null=True)  # Field name made lowercase.
    idno = models.CharField(db_column='Idno', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=10, blank=True, null=True,
                           choices=SEX_CHOICES)  # Field name made lowercase.
    #regage는 계산이 필요한 컬럼
    regage = models.CharField(db_column='regAge', max_length=15, blank=True, null=True)  # Field name made lowercase.
    birthday = models.DateTimeField(db_column='Birthday', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='Phone2', max_length=50, blank=True, null=True)  # Field name made lowercase.

    ptype = models.SmallIntegerField(db_column='Ptype', blank=True, null=True,
                                     choices=PATIENT_TYPE_CHOICES)  # Field name made lowercase.
    distype = models.SmallIntegerField(blank=True, null=True, choices=DISEASE_TYPE_CHOICES)
    axis = models.SmallIntegerField(db_column='Axis', blank=True, null=True,
                                    choices=AXIS_CHOICES)  # Field name made lowercase.
    tent = models.SmallIntegerField(db_column='Tent', blank=True, null=True,
                                    choices=TENT_CHOICES)  # Field name made lowercase.
    class_field = models.CharField(db_column='class', max_length=30, blank=True, null=True,
                                   choices=CLASS_CHOICES)  # Field renamed because it was a Python reserved word.

    cc = models.CharField(db_column='CC', max_length=50, blank=True, null=True,
                          choices=CC_CHOICES)  # Field name made lowercase.
    symptoms = models.TextField(db_column='Symptoms', blank=True, null=True)  # Field name made lowercase.
    neusign = models.CharField(db_column='Neusign', max_length=20, blank=True, null=True,
                               choices=NUESIGN_CHOICES)  # Field name made lowercase.
    signs = models.TextField(db_column='Signs', blank=True, null=True)  # Field name made lowercase.
    mental = models.IntegerField(db_column='Mental', blank=True, null=True, choices=MENTAL_CHOICES)  # Field name made lowercase.
    kps = models.IntegerField(db_column='KPS', blank=True, null=True, choices=KPS_CHOICES) # Field name made lowercase.
    csremark = models.TextField(db_column='Csremark', blank=True, null=True)  # Field name made lowercase.
    qolscore = models.CharField(db_column='QOLscore', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pfhx = models.TextField(db_column='PFHx', blank=True, null=True)  # Field name made lowercase.

    # Radiology (preop Initial CT Findings)

    ictday = models.DateTimeField(db_column='iCTday', blank=True, null=True)  # Field name made lowercase.
    ictlesno = models.SmallIntegerField(db_column='iCTlesno', blank=True, null=True,
                                        choices=CTLESNO_CHOICES)  # Field name made lowercase.
    ictsite = models.SmallIntegerField(db_column='iCTsite', blank=True, null=True,
                                       choices=CTSITE_CHOICES)  # Field name made lowercase.
    icthydr = models.SmallIntegerField(db_column='iCThydr', blank=True, null=True,
                                       choices=CTHYDR_CHOICES)  # Field name made lowercase.
    icthemo = models.SmallIntegerField(db_column='iCThemo', blank=True, null=True,
                                       choices=CTHEMO_CHOICES)  # Field name made lowercase.
    ictcalc = models.SmallIntegerField(db_column='iCTcalc', blank=True, null=True,
                                       choices=CTCALC_CHOICES)  # Field name made lowercase.
    ictsize = models.CharField(db_column='iCTsize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ictfind = models.CharField(db_column='iCTfind', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # Radiology (preop Initial MR Findings)
    imrday = models.DateTimeField(db_column='iMRday', blank=True, null=True)  # Field name made lowercase.
    imrlesno = models.SmallIntegerField(db_column='iMRlesno', blank=True, null=True)  # Field name made lowercase.
    imrsite = models.SmallIntegerField(db_column='iMRsite', blank=True, null=True)  # Field name made lowercase.
    imrhydr = models.SmallIntegerField(db_column='iMRhydr', blank=True, null=True)  # Field name made lowercase.
    imrhemo = models.SmallIntegerField(db_column='iMRhemo', blank=True, null=True)  # Field name made lowercase.
    imrsize = models.CharField(db_column='iMRsize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imrfind = models.CharField(db_column='iMRfind', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # Radiology (preop Initial SPECT Findings)
    spectday = models.DateTimeField(blank=True, null=True)
    thallium = models.SmallIntegerField(blank=True, null=True, choices=THALLIUM_CHOICES)
    mibi = models.SmallIntegerField(db_column='MIBI', blank=True, null=True,
                                    choices=MIBI_CHOICES)  # Field name made lowercase.
    specfind = models.CharField(db_column='Specfind', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    # Radiology (preop Initial PET Findings)
    ipetday = models.DateTimeField(db_column='iPETday', blank=True, null=True)  # Field name made lowercase.
    ipetri = models.IntegerField(db_column='iPETri', blank=True, null=True,
                                 choices=PETRI_CHOICES)  # Field name made lowercase.
    ipet = models.SmallIntegerField(db_column='iPET', blank=True, null=True,
                                    choices=PET_CHOICES)  # Field name made lowercase.
    ipetfind = models.CharField(db_column='iPETfind', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    # Radiology (preop Initial Angiography Findings)
    angioday = models.DateTimeField(db_column='Angioday', blank=True, null=True)  # Field name made lowercase.
    angiocom = models.SmallIntegerField(db_column='Angiocom', blank=True, null=True,
                                        choices=ANGIOCOM_CHOICES)  # Field name made lowercase.
    angiofin = models.CharField(db_column='Angiofin', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    othraday = models.DateTimeField(db_column='Othraday', blank=True, null=True)  # Field name made lowercase.
    othrad = models.CharField(db_column='Othrad', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f'{self.name}/{self.pk}/{self.sex}/{self.birthday}'

    class Meta:
        managed = True
        db_table = 'Overall'

# 1:1 Tumor : Overall
class TumorSurgery(models.Model):
    # Tumor surgery
    patient = models.OneToOneField(Overall,null=True, on_delete=models.CASCADE, verbose_name='Patient ID')
    op = models.SmallIntegerField(db_column='Op', blank=True, null=True)  # Field name made lowercase.
    oprema = models.CharField(db_column='Oprema', max_length=200, blank=True, null=True)  # Field name made lowercase.
    specimen = models.CharField(db_column='Phone2', max_length=50, blank=True, null=True)
    # from csf
    csfop = models.SmallIntegerField(db_column='CSFop', blank=True, null=True)  # Field name made lowercase.


# N:1 Sub:Tumor
class SubSurgery(models.Model):
# surgery class
# pk = auto inc
# fk = Tumor (idno/surgery)
    surgery = models.ForeignKey(TumorSurgery, on_delete=models.CASCADE, verbose_name='Surgery ID')
    opdate = models.DateTimeField(db_column='Opdate', blank=True, null=True)  # Field name made lowercase.
    opname = models.TextField(db_column='Opname', blank=True, null=True)  # Field name made lowercase.
    optype = models.SmallIntegerField(db_column='Optype', blank=True, null=True)  # Field name made lowercase.
    oprema = models.TextField(db_column='Oprema', blank=True, null=True)  # Field name made lowercase.
    opresu = models.TextField(db_column='Opresu', blank=True, null=True)  # Field name made lowercase.
    # choice 넣어주어야한다.
    opcx = models.SmallIntegerField(db_column='opCx', blank=True, null=True)  # Field name made lowercase.
    cxday = models.DateTimeField(db_column='Cxday', blank=True, null=True)  # Field name made lowercase.
    cxrema = models.TextField(db_column='Cxrema', blank=True, null=True)  # Field name made lowercase.
    cxresu = models.SmallIntegerField(db_column='Cxresu', blank=True, null=True)  # Field name made lowercase.
    cxfinal = models.CharField(db_column='Cxfinal', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    # Surgery for CSF disorder
    csfday = models.DateTimeField(db_column='CSFday', blank=True, null=True)  # Field name made lowercase.
    csftype = models.TextField(db_column='CSFtype', blank=True, null=True)  # Field name made lowercase.
    csfcx = models.SmallIntegerField(db_column='CSFcx', blank=True, null=True)  # Field name made lowercase.
    csfcxre = models.CharField(db_column='CSFcxre', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    csfresu = models.CharField(db_column='CSFresu', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.

# 1:1 Adju : Overall
class AdjuvantTherapy(models.Model):
    patient = models.OneToOneField(Overall,null=True, on_delete=models.CASCADE, verbose_name='Patient ID')

    # Radiation therapy
    rtx = models.SmallIntegerField(db_column='RTx', blank=True, null=True)  # Field name made lowercase.
    rtstart = models.DateTimeField(db_column='RTstart', blank=True, null=True)  # Field name made lowercase.
    rtend = models.DateTimeField(db_column='RTend', blank=True, null=True)  # Field name made lowercase.
    rtxdose = models.CharField(db_column='RTxdose', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rtxrema = models.TextField(db_column='Rtxrema', blank=True, null=True)  # Field name made lowercase.
    rtcx = models.CharField(db_column='RTcx', max_length=50, blank=True, null=True)  # Field name made lowercase.

    # Radio surgery
    rs = models.SmallIntegerField(db_column='RS', blank=True, null=True)  # Field name made lowercase.
    rsdate = models.DateTimeField(db_column='RSdate', blank=True, null=True)  # Field name made lowercase.
    rsmax = models.CharField(db_column='RSmax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rsmar = models.IntegerField(db_column='RSmar', blank=True, null=True)  # Field name made lowercase.
    rsrema = models.CharField(db_column='RSrema', max_length=50, blank=True, null=True)  # Field name made lowercase.


    # Threarpeutic trial
    othertx = models.SmallIntegerField(db_column='Othertx', blank=True, null=True)  # Field name made lowercase.
    othtxtyp = models.CharField(db_column='Othtxtyp', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    othtxday = models.DateTimeField(db_column='Othtxday', blank=True, null=True)  # Field name made lowercase.
    othtxtm = models.TextField(db_column='Othtxtm', blank=True, null=True)  # Field name made lowercase.
    othtxre = models.TextField(db_column='Othtxre', blank=True, null=True)  # Field name made lowercase.
    othtxcx = models.CharField(db_column='Othtxcx', max_length=50, blank=True, null=True)  # Field name made lowercase.

# Chemotherapy
#  N:1 Chemo : Adjuvant therapy
class Chemotherapy(models.Model):
    therapy = models.ForeignKey(AdjuvantTherapy, on_delete=models.CASCADE, verbose_name='Adjuvant Therapy ID')

    ctx = models.SmallIntegerField(db_column='CTx', blank=True, null=True)  # Field name made lowercase.

    ctxregi = models.CharField(db_column='CTxregi', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    ctxno = models.CharField(db_column='CTxno', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctxday = models.DateTimeField(db_column='CTxday', blank=True, null=True)  # Field name made lowercase.
    ctxtm = models.DateTimeField(db_column='CTxtm', blank=True, null=True)  # Field name made lowercase.
    ctx1rema = models.TextField(db_column='CTxrema', blank=True, null=True)  # Field name made lowercase.

# 누구와 관계?
#  우선 overall와 1:N
class Followup(models.Model):
    fuid = models.CharField(db_column='FUid', max_length=50, primary_key=True)  # Field name made lowercase.
    patient = models.ForeignKey(Overall,null=True, on_delete=models.CASCADE, verbose_name='Patient ID')
    idno = models.CharField(db_column='Idno', max_length=50)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    # Clinical Fu
    cfuday = models.DateTimeField(db_column='CFUday', blank=True, null=True)  # Field name made lowercase.
    cfucli = models.TextField(db_column='CFUcli', blank=True, null=True)  # Field name made lowercase.
    cfukps = models.SmallIntegerField(db_column='CFUKPS', blank=True, null=True)  # Field name made lowercase.
    cfuqol = models.SmallIntegerField(db_column='CFUQOL', blank=True, null=True)  # Field name made lowercase.
    # Radiological Fu
    rfuday = models.DateTimeField(db_column='RFUday', blank=True, null=True)  # Field name made lowercase.
    rfutyp = models.SmallIntegerField(db_column='RFUtyp', blank=True, null=True)  # Field name made lowercase.
    rfures = models.SmallIntegerField(db_column='RFUres', blank=True, null=True)  # Field name made lowercase.
    rfurad = models.TextField(db_column='RFUrad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Followup'

# followup와  1:n 관계?  or orverall(1:N)?
#  Followup와 M:N 관계?
#  우선은 overall 1:N
class Recurrence(models.Model):
    patient = models.ForeignKey(Overall, on_delete=models.CASCADE, verbose_name='Patient ID')
    # 이런 녀석을 어떻게 만들어야 할까. 중복 되지 않지만 bool 사용되는 녀석(재발 여부 확인)
    recur = models.SmallIntegerField(db_column='Recur', blank=True, null=True)  # Field name made lowercase.
    recurtm = models.DateTimeField(db_column='Recurtm', blank=True, null=True)  # Field name made lowercase.
    recurpt = models.CharField(db_column='Recurpt', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recurre = models.TextField(db_column='Recurre', blank=True, null=True)  # Field name made lowercase.
    recurtx = models.TextField(db_column='Recurtx', blank=True, null=True)  # Field name made lowercase.

# Followup 1:1 관계 ?
#  우선은 Overall 와 1:1로 작성
class Results(models.Model):
    # Clinical result
    patient = models.OneToOneField(Overall,null=True, on_delete=models.CASCADE, verbose_name='Patient ID')

    lcfuday = models.DateTimeField(db_column='LCFUday', blank=True, null=True)  # Field name made lowercase.
    liferesu = models.SmallIntegerField(db_column='Liferesu', blank=True, null=True)  # Field name made lowercase.
    lcfucli = models.TextField(db_column='LCFUcli', blank=True, null=True)  # Field name made lowercase.
    lcfukps = models.SmallIntegerField(db_column='LCFUKPS', blank=True, null=True)  # Field name made lowercase.
    lcfuqol = models.SmallIntegerField(db_column='LCFUQOL', blank=True, null=True)  # Field name made lowercase.
    outcome = models.SmallIntegerField(db_column='Outcome', blank=True, null=True)  # Field name made lowercase.
    cod = models.SmallIntegerField(db_column='Cod', blank=True, null=True)  # Field name made lowercase.
    codrema = models.TextField(db_column='Codrema', blank=True, null=True)  # Field name made lowercase.
    # Radiological result
    lrfuday = models.DateTimeField(db_column='LRFUday', blank=True, null=True)  # Field name made lowercase.
    lrfutyp = models.SmallIntegerField(db_column='LRFUtyp', blank=True, null=True)  # Field name made lowercase.
    lrfures = models.SmallIntegerField(db_column='LRFUres', blank=True, null=True)  # Field name made lowercase.
    lesion = models.SmallIntegerField(db_column='Lesion', blank=True, null=True)  # Field name made lowercase.
    lrfurad = models.TextField(db_column='LRFUrad', blank=True, null=True)  # Field name made lowercase.
    casesum = models.TextField(blank=True, null=True)


######################################
# minkj1992 TODO: db 추가수정 해야한다.
class Netumor(models.Model):
    idno = models.CharField(db_column='Idno', max_length=50, primary_key=True)  # Field name made lowercase.
    netno = models.IntegerField(db_column='Netno', blank=True, null=True)  # Field name made lowercase.
    newho = models.SmallIntegerField(db_column='NEWHO', blank=True, null=True)  # Field name made lowercase.
    nedxchge = models.IntegerField(db_column='NEDxchge', blank=True, null=True)  # Field name made lowercase.
    nedx1 = models.TextField(db_column='NEDx1', blank=True, null=True)  # Field name made lowercase.
    nedx1day = models.DateTimeField(db_column='NEDx1day', blank=True, null=True)  # Field name made lowercase.
    neihc1 = models.CharField(db_column='NEIHC1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nedx2 = models.CharField(db_column='NEDx2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nedx2day = models.DateTimeField(db_column='NEDx2day', blank=True, null=True)  # Field name made lowercase.
    neihc2 = models.CharField(db_column='NEIHC2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nedxrema = models.CharField(db_column='NEdxrema', max_length=100, blank=True, null=True)  # Field name made lowercase.
    neimgtm = models.DateTimeField(db_column='Neimgtm', blank=True, null=True)  # Field name made lowercase.
    neimg = models.SmallIntegerField(blank=True, null=True)
    nelocate = models.CharField(max_length=100, blank=True, null=True)
    netype = models.SmallIntegerField(blank=True, null=True)
    neeloqu = models.SmallIntegerField(blank=True, null=True)
    necyst = models.SmallIntegerField(blank=True, null=True)
    nevent = models.SmallIntegerField(blank=True, null=True)
    necrosis = models.SmallIntegerField(blank=True, null=True)
    nenhance = models.SmallIntegerField(blank=True, null=True)
    nedema = models.SmallIntegerField(blank=True, null=True)
    neremark = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NeTumor'

class Meningtumor(models.Model):
    idno = models.CharField(max_length=50, primary_key=True)
    menino = models.CharField(db_column='Menino', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mepatho = models.TextField(db_column='Mepatho', blank=True, null=True)  # Field name made lowercase.
    meihc = models.CharField(max_length=50, blank=True, null=True)
    meimgtm = models.DateTimeField(db_column='Meimgtm', blank=True, null=True)  # Field name made lowercase.
    mesite = models.SmallIntegerField(db_column='Mesite', blank=True, null=True)  # Field name made lowercase.
    mecyst = models.SmallIntegerField(db_column='Mecyst', blank=True, null=True)  # Field name made lowercase.
    mearach = models.SmallIntegerField(db_column='Mearach', blank=True, null=True)  # Field name made lowercase.
    meedema = models.SmallIntegerField(db_column='Meedema', blank=True, null=True)  # Field name made lowercase.
    mevessel = models.SmallIntegerField(db_column='Mevessel', blank=True, null=True)  # Field name made lowercase.
    mesinus = models.SmallIntegerField(db_column='Mesinus', blank=True, null=True)  # Field name made lowercase.
    meimgre = models.CharField(db_column='Meimgre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    meop1day = models.DateTimeField(db_column='Meop1day', blank=True, null=True)  # Field name made lowercase.
    meop1ara = models.SmallIntegerField(db_column='Meop1ara', blank=True, null=True)  # Field name made lowercase.
    meop1typ = models.SmallIntegerField(db_column='Meop1typ', blank=True, null=True)  # Field name made lowercase.
    meop2day = models.DateTimeField(db_column='Meop2day', blank=True, null=True)  # Field name made lowercase.
    meop2ara = models.SmallIntegerField(db_column='Meop2ara', blank=True, null=True)  # Field name made lowercase.
    meop2typ = models.SmallIntegerField(db_column='Meop2typ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'MeningTumor'

class Others(models.Model):
    idno = models.CharField(max_length=50, primary_key=True)
    otherno = models.IntegerField(db_column='Otherno', blank=True, null=True)  # Field name made lowercase.
    othpatho = models.CharField(db_column='Othpatho', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ihcfind = models.CharField(db_column='Ihcfind', max_length=100, blank=True, null=True)  # Field name made lowercase.
    othrema = models.CharField(db_column='Othrema', max_length=50, blank=True, null=True)  # Field name made lowercase.
    preothtm = models.DateTimeField(db_column='PreOthtm', blank=True, null=True)  # Field name made lowercase.
    preoth = models.CharField(db_column='Preoth', max_length=50, blank=True, null=True)  # Field name made lowercase.
    preothre = models.CharField(db_column='Preothre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oth1tm = models.DateTimeField(db_column='Oth1tm', blank=True, null=True)  # Field name made lowercase.
    oth1 = models.CharField(db_column='Oth1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oth1re = models.CharField(db_column='Oth1re', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oth2tm = models.DateTimeField(db_column='Oth2tm', blank=True, null=True)  # Field name made lowercase.
    oth2 = models.CharField(db_column='Oth2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oth2re = models.CharField(db_column='Oth2re', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oth3tm = models.DateTimeField(db_column='Oth3tm', blank=True, null=True)  # Field name made lowercase.
    oth3 = models.CharField(db_column='Oth3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oth3re = models.CharField(db_column='Oth3re', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oth4tm = models.DateTimeField(db_column='Oth4tm', blank=True, null=True)  # Field name made lowercase.
    oth4 = models.CharField(db_column='Oth4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oth4re = models.CharField(db_column='Oth4re', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oth5tm = models.DateTimeField(db_column='Oth5tm', blank=True, null=True)  # Field name made lowercase.
    oth5 = models.CharField(db_column='Oth5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oth5re = models.CharField(db_column='Oth5re', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oth6tm = models.DateTimeField(db_column='Oth6tm', blank=True, null=True)  # Field name made lowercase.
    oth6 = models.CharField(db_column='Oth6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oth6re = models.CharField(db_column='Oth6re', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oth7tm = models.DateTimeField(db_column='Oth7tm', blank=True, null=True)  # Field name made lowercase.
    oth7 = models.CharField(db_column='Oth7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oth7re = models.CharField(db_column='Oth7re', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oth8tm = models.DateTimeField(db_column='Oth8tm', blank=True, null=True)  # Field name made lowercase.
    oth8 = models.CharField(db_column='Oth8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oth8re = models.CharField(db_column='Oth8re', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oth9tm = models.DateTimeField(db_column='Oth9tm', blank=True, null=True)  # Field name made lowercase.
    oth9 = models.CharField(db_column='Oth9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oth9re = models.CharField(db_column='Oth9re', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oth10tm = models.DateTimeField(db_column='Oth10tm', blank=True, null=True)  # Field name made lowercase.
    oth10 = models.CharField(db_column='Oth10', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oth10re = models.CharField(db_column='Oth10re', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Others'

class Pittumor(models.Model):
    idno = models.CharField(max_length=50, primary_key=True)
    pitno = models.IntegerField(blank=True, null=True)
    endocrin = models.IntegerField(db_column='Endocrin', blank=True, null=True)  # Field name made lowercase.
    function = models.SmallIntegerField(db_column='Function', blank=True, null=True)  # Field name made lowercase.
    pitpatho = models.CharField(db_column='Pitpatho', max_length=100, blank=True, null=True)  # Field name made lowercase.
    seihc = models.CharField(max_length=50, blank=True, null=True)
    pitimgtm = models.DateTimeField(blank=True, null=True)
    hardygr = models.SmallIntegerField(blank=True, null=True)
    hardysta = models.SmallIntegerField(db_column='Hardysta', blank=True, null=True)  # Field name made lowercase.
    pitcyst = models.SmallIntegerField(blank=True, null=True)
    pithemo = models.SmallIntegerField(blank=True, null=True)
    pitneuro = models.SmallIntegerField(blank=True, null=True)
    pitica = models.SmallIntegerField(blank=True, null=True)
    pitimgre = models.CharField(max_length=100, blank=True, null=True)
    vfpretm = models.DateTimeField(db_column='Vfpretm', blank=True, null=True)  # Field name made lowercase.
    vapre = models.CharField(db_column='Vapre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vfpre = models.SmallIntegerField(db_column='Vfpre', blank=True, null=True)  # Field name made lowercase.
    vfprema = models.CharField(db_column='Vfprema', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vf1tm = models.DateTimeField(db_column='Vf1tm', blank=True, null=True)  # Field name made lowercase.
    va1 = models.CharField(db_column='Va1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vf1 = models.SmallIntegerField(db_column='Vf1', blank=True, null=True)  # Field name made lowercase.
    vf1rema = models.CharField(db_column='Vf1rema', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vf2tm = models.DateTimeField(db_column='Vf2tm', blank=True, null=True)  # Field name made lowercase.
    va2 = models.CharField(db_column='Va2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vf2 = models.SmallIntegerField(db_column='Vf2', blank=True, null=True)  # Field name made lowercase.
    vf2rema = models.CharField(db_column='Vf2rema', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vf3tm = models.DateTimeField(db_column='Vf3tm', blank=True, null=True)  # Field name made lowercase.
    va3 = models.CharField(db_column='Va3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vf3 = models.SmallIntegerField(db_column='Vf3', blank=True, null=True)  # Field name made lowercase.
    vf3rema = models.CharField(db_column='Vf3rema', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vf4tm = models.DateTimeField(db_column='Vf4tm', blank=True, null=True)  # Field name made lowercase.
    va4 = models.CharField(db_column='Va4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vf4 = models.SmallIntegerField(db_column='Vf4', blank=True, null=True)  # Field name made lowercase.
    vf4rema = models.CharField(db_column='Vf4rema', max_length=100, blank=True, null=True)  # Field name made lowercase.
    prehormo = models.SmallIntegerField(db_column='Prehormo', blank=True, null=True)  # Field name made lowercase.
    presedi = models.SmallIntegerField(db_column='Presedi', blank=True, null=True)  # Field name made lowercase.
    hspretm = models.DateTimeField(db_column='Hspretm', blank=True, null=True)  # Field name made lowercase.
    hspretyp = models.SmallIntegerField(db_column='Hspretyp', blank=True, null=True)  # Field name made lowercase.
    hsprfind = models.CharField(db_column='Hsprfind', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hs1tm = models.DateTimeField(db_column='Hs1tm', blank=True, null=True)  # Field name made lowercase.
    hs1typ = models.SmallIntegerField(db_column='Hs1typ', blank=True, null=True)  # Field name made lowercase.
    hs1find = models.CharField(db_column='Hs1find', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hs2tm = models.DateTimeField(db_column='Hs2tm', blank=True, null=True)  # Field name made lowercase.
    hs2typ = models.SmallIntegerField(db_column='Hs2typ', blank=True, null=True)  # Field name made lowercase.
    hs2find = models.CharField(db_column='Hs2find', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hs3tm = models.DateTimeField(db_column='Hs3tm', blank=True, null=True)  # Field name made lowercase.
    hs3typ = models.SmallIntegerField(db_column='Hs3typ', blank=True, null=True)  # Field name made lowercase.
    hs3find = models.CharField(db_column='Hs3find', max_length=100, blank=True, null=True)  # Field name made lowercase.
    preprltm = models.DateTimeField(db_column='Preprltm', blank=True, null=True)  # Field name made lowercase.
    preprl = models.CharField(db_column='PrePRL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    preprlre = models.CharField(db_column='prePRLre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prl1tm = models.DateTimeField(db_column='PRL1tm', blank=True, null=True)  # Field name made lowercase.
    prlfu1 = models.CharField(db_column='PRLFU1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prlfu1re = models.CharField(db_column='PRLFU1re', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prl2tm = models.DateTimeField(db_column='PRL2tm', blank=True, null=True)  # Field name made lowercase.
    prlfu2 = models.CharField(db_column='PRLFU2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prlfu2re = models.CharField(db_column='PRLFU2re', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prl3tm = models.DateTimeField(db_column='PRL3tm', blank=True, null=True)  # Field name made lowercase.
    prlfu3 = models.CharField(db_column='PRLFU3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prlfu3re = models.CharField(db_column='PRLFU3re', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prl4tm = models.DateTimeField(db_column='PRL4tm', blank=True, null=True)  # Field name made lowercase.
    prlfu4 = models.CharField(db_column='PRLFU4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prlfu4re = models.CharField(db_column='PRLFU4re', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prl5tm = models.DateTimeField(db_column='PRL5tm', blank=True, null=True)  # Field name made lowercase.
    prlfu5 = models.CharField(db_column='PRLFU5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prlfu5re = models.CharField(db_column='PRLFU5re', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prl6tm = models.DateTimeField(db_column='PRL6tm', blank=True, null=True)  # Field name made lowercase.
    prlfu6 = models.CharField(db_column='PRLFU6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prlfu6re = models.CharField(db_column='PRLFU6re', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prl7tm = models.DateTimeField(db_column='PRL7tm', blank=True, null=True)  # Field name made lowercase.
    prlfu7 = models.CharField(db_column='PRLFU7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prlfu7re = models.CharField(db_column='PRLFU7re', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prl8tm = models.DateTimeField(db_column='PRL8tm', blank=True, null=True)  # Field name made lowercase.
    prlfu8 = models.CharField(db_column='PRLFU8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prlfu8re = models.CharField(db_column='PRLFU8re', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prl9tm = models.DateTimeField(db_column='PRL9tm', blank=True, null=True)  # Field name made lowercase.
    prlfu9 = models.CharField(db_column='PRLFU9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prlfu9re = models.CharField(db_column='PRLFU9re', max_length=50, blank=True, null=True)  # Field name made lowercase.
    preghtm = models.DateTimeField(db_column='preGHtm', blank=True, null=True)  # Field name made lowercase.
    pregh = models.CharField(db_column='preGH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    preigf = models.CharField(db_column='preIGF', max_length=50, blank=True, null=True)  # Field name made lowercase.
    preghre = models.CharField(db_column='preGHre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gh1tm = models.DateTimeField(db_column='GH1tm', blank=True, null=True)  # Field name made lowercase.
    ghfu1 = models.CharField(db_column='GHFU1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    igffu1 = models.CharField(db_column='IGFFU1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ghfu1re = models.CharField(db_column='GHFU1re', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gh2tm = models.DateTimeField(db_column='GH2tm', blank=True, null=True)  # Field name made lowercase.
    ghfu2 = models.CharField(db_column='GHFU2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    igffu2 = models.CharField(db_column='IGFFU2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ghfu2re = models.CharField(db_column='GHFU2re', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gh3tm = models.DateTimeField(db_column='GH3tm', blank=True, null=True)  # Field name made lowercase.
    ghfu3 = models.CharField(db_column='GHFU3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    igffu3 = models.CharField(db_column='IGFFU3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ghfu3re = models.CharField(db_column='GHFU3re', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gh4tm = models.DateTimeField(db_column='GH4tm', blank=True, null=True)  # Field name made lowercase.
    ghfu4 = models.CharField(db_column='GHFU4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    igffu4 = models.CharField(db_column='IGFFU4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ghfu4re = models.CharField(db_column='GHFU4re', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gh5tm = models.DateTimeField(db_column='GH5tm', blank=True, null=True)  # Field name made lowercase.
    ghfu5 = models.CharField(db_column='GHFU5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    igffu5 = models.CharField(db_column='IGFFU5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ghfu5re = models.CharField(db_column='GHFU5re', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gh6tm = models.DateTimeField(db_column='GH6tm', blank=True, null=True)  # Field name made lowercase.
    ghfu6 = models.CharField(db_column='GHFU6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    igffu6 = models.CharField(db_column='IGFFU6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ghfu6re = models.CharField(db_column='GHFU6re', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gh7tm = models.DateTimeField(db_column='GH7tm', blank=True, null=True)  # Field name made lowercase.
    ghfu7 = models.CharField(db_column='GHFU7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    igffu7 = models.CharField(db_column='IGFFU7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ghfu7re = models.CharField(db_column='GHFU7re', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gh8tm = models.DateTimeField(db_column='GH8tm', blank=True, null=True)  # Field name made lowercase.
    ghfu8 = models.CharField(db_column='GHFU8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    igffu8 = models.CharField(db_column='IGFFU8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ghfu8re = models.CharField(db_column='GHFU8re', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gh9tm = models.DateTimeField(db_column='GH9tm', blank=True, null=True)  # Field name made lowercase.
    ghfu9 = models.CharField(db_column='GHFU9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    igffu9 = models.CharField(db_column='IGFFU9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ghfu9re = models.CharField(db_column='GHFU9re', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lpithmtm = models.DateTimeField(db_column='Lpithmtm', blank=True, null=True)  # Field name made lowercase.
    lpith = models.SmallIntegerField(db_column='Lpith', blank=True, null=True)  # Field name made lowercase.
    lpitrem = models.CharField(db_column='Lpitrem', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pitmedi = models.SmallIntegerField(db_column='Pitmedi', blank=True, null=True)  # Field name made lowercase.
    pitdrug = models.CharField(db_column='Pitdrug', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pitmere = models.CharField(db_column='Pitmere', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PitTumor'

class Schtumor(models.Model):
    idno = models.CharField(max_length=50, primary_key=True)
    test = models.IntegerField()
    schtno = models.IntegerField(blank=True, null=True)
    schpatho = models.CharField(max_length=100, blank=True, null=True)
    schihc = models.CharField(db_column='schIhc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    schorig = models.SmallIntegerField(db_column='Schorig', blank=True, null=True)  # Field name made lowercase.
    schimgtm = models.DateTimeField(blank=True, null=True)
    schsize = models.SmallIntegerField(blank=True, null=True)
    schcyst = models.SmallIntegerField(blank=True, null=True)
    samiityp = models.SmallIntegerField(db_column='Samiityp', blank=True, null=True)  # Field name made lowercase.
    nsimgre = models.CharField(max_length=100, blank=True, null=True)
    prehear = models.SmallIntegerField(db_column='Prehear', blank=True, null=True)  # Field name made lowercase.
    preheatm = models.DateTimeField(db_column='Preheatm', blank=True, null=True)  # Field name made lowercase.
    prehl = models.CharField(db_column='Prehl', max_length=50, blank=True, null=True)  # Field name made lowercase.
    presds = models.CharField(db_column='preSDS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    heafu1tm = models.DateTimeField(db_column='heaFU1tm', blank=True, null=True)  # Field name made lowercase.
    hlfu1 = models.IntegerField(db_column='hlFU1', blank=True, null=True)  # Field name made lowercase.
    sdsfu1 = models.CharField(db_column='SDSFU1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    heafu2tm = models.DateTimeField(db_column='heaFU2tm', blank=True, null=True)  # Field name made lowercase.
    hlfu2 = models.IntegerField(db_column='hlFU2', blank=True, null=True)  # Field name made lowercase.
    sdsfu2 = models.CharField(db_column='SDSFU2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    heafu3tm = models.DateTimeField(db_column='heaFU3tm', blank=True, null=True)  # Field name made lowercase.
    hlfu3 = models.IntegerField(db_column='hlFU3', blank=True, null=True)  # Field name made lowercase.
    sdsfu3 = models.CharField(db_column='SDSFU3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prefactm = models.DateTimeField(db_column='Prefactm', blank=True, null=True)  # Field name made lowercase.
    prehb = models.SmallIntegerField(db_column='preHB', blank=True, null=True)  # Field name made lowercase.
    prefacfn = models.CharField(max_length=50, blank=True, null=True)
    facfu1tm = models.DateTimeField(db_column='facFU1tm', blank=True, null=True)  # Field name made lowercase.
    hbfu1 = models.SmallIntegerField(db_column='HBFU1', blank=True, null=True)  # Field name made lowercase.
    facfnfu1 = models.CharField(db_column='FacfnFU1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    facfu2tm = models.DateTimeField(db_column='facFU2tm', blank=True, null=True)  # Field name made lowercase.
    hbfu2 = models.SmallIntegerField(db_column='HBFU2', blank=True, null=True)  # Field name made lowercase.
    facfnfu2 = models.CharField(db_column='FacfnFU2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    facfu3tm = models.DateTimeField(db_column='facFU3tm', blank=True, null=True)  # Field name made lowercase.
    hbfu3 = models.SmallIntegerField(db_column='HBFU3', blank=True, null=True)  # Field name made lowercase.
    facfnfu3 = models.CharField(db_column='FacfnFU3', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'SchTumor'

#minkj1992 TODO: Metastases 추가해주어야 한다.