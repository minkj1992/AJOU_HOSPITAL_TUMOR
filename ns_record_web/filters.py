import django_filters

from .models import Patient, Trauma, Combine, History, GCS, Diagnosis, Injury, Monitor, Surgery, NonSurgicalTreatment, \
    Treatment, Assessment


class PatientFilter(django_filters.FilterSet):
    admission_date = django_filters.DateFilter()
    admission_date__gt = django_filters.DateFilter(field_name='admission_date', lookup_expr='gt')
    admission_date__lt = django_filters.DateFilter(field_name='admission_date', lookup_expr='lt')

    # Trauma
    type_admission = django_filters.ChoiceFilter(label='Type of Admission', field_name='trauma__type_admission',
                                                 choices=Trauma.TYPE_CHOICES)
    transfer_method = django_filters.ChoiceFilter(label='Pre-admission treat', field_name='trauma__pre_admission',
                                                  choices=Trauma.TRANSFER_CHOICES)
    pre_admission = django_filters.ChoiceFilter(label='Transfer Method', field_name='trauma__transfer_method',
                                                choices=Trauma.PRE_ADMISSION_CHOICES)
    type_of_injury = django_filters.ChoiceFilter(label='Type of Injury', field_name='trauma__type_of_injury',
                                                 choices=Trauma.TYPE_OF_INJURY_CHOICES)
    place_of_injury = django_filters.ChoiceFilter(label='Place of Injury', field_name='trauma__place_of_injury',
                                                  choices=Trauma.TYPE_OF_INJURY_CHOICES)
    drug_intoxication = django_filters.ChoiceFilter(label='Drug Intoxication', field_name='trauma__drug_intoxication',
                                                    choices=Trauma.DRUG_INTOXICATION_CHOICES)
    cause_of_injury = django_filters.ChoiceFilter(label='Cause of Injury', field_name='trauma__cause_of_injury',
                                                  choices=Trauma.CAUSE_OF_INJURY_CHOICES)
    loc = django_filters.ChoiceFilter(label='Drug Intoxication', field_name='trauma__loc',
                                      choices=Trauma.LOC_CHOICES)

    # Combine
    other_major_operation = django_filters.CharFilter(label='Drug Intoxication',
                                                      field_name='combine__other_major_operation')
    other_major_office = django_filters.MultipleChoiceFilter(label='Drug Intoxication',
                                                             field_name='combine__other_major_office',
                                                             choices=Combine.OPR_CHOICES)
    non_tbi_surgery_date = django_filters.DateFilter(label='Drug Intoxication',
                                                     field_name='combine__other_major_office')

    # History
    psychiatric = django_filters.MultipleChoiceFilter(label='Psychiatric',
                                                      field_name='history__other_major_office',
                                                      choices=History.PSYCHIATRIC_CHOICES)

    cardiovascular = django_filters.MultipleChoiceFilter(label='Cardiovascular',
                                                         field_name='history__cardiovascular',
                                                         choices=History.CARDIOVASCULAR_CHOICES)
    endocrine = django_filters.MultipleChoiceFilter(label='Endocrine',
                                                    field_name='history__endocrine',
                                                    choices=History.ENDO_CHOICES)
    spinal = django_filters.MultipleChoiceFilter(label='spinal',
                                                 field_name='history__spinal',
                                                 choices=History.SPINAL_CHOICES)
    neurologic = django_filters.MultipleChoiceFilter(label='Neurologic',
                                                     field_name='history__neurologic',
                                                     choices=History.NEU_CHOICES)
    oncologic = django_filters.MultipleChoiceFilter(label='Oncologic',
                                                    field_name='history__oncologic',
                                                    choices=History.ONCOLOGIC_CHOICES)
    gi = django_filters.MultipleChoiceFilter(label='GI',
                                             field_name='history__gi',
                                             choices=History.GI_CHOICES)
    hepatic = django_filters.MultipleChoiceFilter(label='Hepatic',
                                                  field_name='history__hepatic',
                                                  choices=History.HEP_CHOICES)
    hematologic = django_filters.MultipleChoiceFilter(label='Hematologic',
                                                      field_name='history__hematologic',
                                                      choices=History.HEM_CHOICES)
    pulmonologic = django_filters.MultipleChoiceFilter(label='Pulmonologic',
                                                       field_name='history__pulmonologic',
                                                       choices=History.PULMONOLOGIC_CHOICES)
    renal = django_filters.MultipleChoiceFilter(label='Renal',
                                                field_name='history__renal',
                                                choices=History.RENAL_CHOICES)
    ent = django_filters.MultipleChoiceFilter(label='Ent',
                                              field_name='history__ent',
                                              choices=History.ENT_CHOICES)
    musculoskeletal = django_filters.MultipleChoiceFilter(label='Musculoskeletal',
                                                          field_name='history__musculoskeletal',
                                                          choices=History.MUSCULOSKELETAL_CHOICES)
    developmental = django_filters.MultipleChoiceFilter(label='Developmental',
                                                        field_name='history__developmental',
                                                        choices=History.DEV_CHOICES)
    anticoagulants = django_filters.MultipleChoiceFilter(label='Anticoagulants',
                                                         field_name='history__anticoagulants',
                                                         choices=History.ANTICOAGULANTS_CHOICES)
    platelet = django_filters.MultipleChoiceFilter(label='Platelet',
                                                   field_name='history__platelet',
                                                   choices=History.PLATELET_CHOICES)

    # GCS
    arr_date = django_filters.DateTimeFilter(label='Date & Time of GCS',
                                             field_name='gcs__arr_date')
    arr_status = django_filters.ChoiceFilter(label='Arrival Mental Status', field_name='gcs__arr_status',
                                             choices=GCS.ARR_STAT_CHOICES)
    arr_sbp = django_filters.CharFilter(label='Arrival SBP', field_name='gcs__arr_sbp')
    arr_dbp = django_filters.CharFilter(label='Arrival DBP', field_name='gcs__arr_dbp')
    arr_hr = django_filters.CharFilter(label='Arrival HR', field_name='gcs__arr_hr')
    arr_rr = django_filters.CharFilter(label='Arrival RR(회/min)', field_name='gcs__arr_rr')
    arr_eye = django_filters.ChoiceFilter(label='Arrival DBP', field_name='gcs__arr_eye', choices=GCS.GEYE_CHOICES)
    arr_verbal = django_filters.ChoiceFilter(label='Arrival GCS Best Verbal Response', field_name='gcs__arr_verbal',
                                             choices=GCS.GVERBAL_CHOICES)
    arr_motor = django_filters.ChoiceFilter(label='Arrival GCS Motor', field_name='gcs__arr_motor',
                                            choices=GCS.GMOTOR_CHOICES)
    arr_total = django_filters.CharFilter(label='Arrival GCS Total', field_name='gcs__arr_total')
    arr_sum = django_filters.CharFilter(label='Arrival Sum', field_name='gcs__arr_sum')
    arr_rts = django_filters.CharFilter(label='Arrival RTS', field_name='gcs__arr_rts')
    arr_rtupper = django_filters.ChoiceFilter(label='Arrival Rt.Upper', field_name='gcs__arr_rtupper',
                                              choices=GCS.GEYE_CHOICES)
    arr_ltupper = django_filters.ChoiceFilter(label='Arrival Lt.Upper', field_name='gcs__arr_ltupper',
                                              choices=GCS.GEYE_CHOICES)
    arr_rtlower = django_filters.ChoiceFilter(label='Arrival Rt.Lower', field_name='gcs__arr_rtlower',
                                              choices=GCS.GEYE_CHOICES)
    arr_ltlower = django_filters.ChoiceFilter(label='Arrival DBP', field_name='gcs__arr_ltlower',
                                              choices=GCS.GEYE_CHOICES)
    arr_pp_right = django_filters.MultipleChoiceFilter(label='Arrival Pupils Right', field_name='gcs__arr_pp_right',
                                                       choices=GCS.PPLR_CHOICES)
    arr_pp_left = django_filters.MultipleChoiceFilter(label='Arrival Pupils Left', field_name='gcs__arr_pp_left',
                                                      choices=GCS.PPLR_CHOICES)
    arr_pp_rtsize = django_filters.ChoiceFilter(label='Arrival Pupils Right Size', field_name='gcs__arr_pp_rtsize',
                                                choices=GCS.PPSIZE_CHOICES)
    arr_pp_ltsize = django_filters.ChoiceFilter(label='Arrival Pupils Left Size', field_name='gcs__arr_pp_ltsize',
                                                choices=GCS.PPSIZE_CHOICES)
    arr_pp_rtshape = django_filters.ChoiceFilter(label='Arrival Pupils Right Shape', field_name='gcs__arr_pp_rtshape',
                                                 choices=GCS.PPSIZE_CHOICES)
    arr_pp_ltshape = django_filters.ChoiceFilter(label='Arrival Pupils Left Shape', field_name='gcs__arr_pp_ltshape',
                                                 choices=GCS.PPSIZE_CHOICES)
    arr_pp_rtprompt = django_filters.ChoiceFilter(label='Arrival Pupils Right Prompt',
                                                  field_name='gcs__arr_pp_rtprompt',
                                                  choices=GCS.PPPROM_CHOICES)
    arr_pp_ltprompt = django_filters.ChoiceFilter(label='Arrival Pupils Left Prompt', field_name='gcs__arr_pp_ltprompt',
                                                  choices=GCS.PPPROM_CHOICES)
    arr_coa_correction = django_filters.ChoiceFilter(label='Arrival Correction of coagulopathy',
                                                     field_name='gcs__arr_coa_correction',
                                                     choices=GCS.COCOA_CHOICES)
    arr_coa_blood = django_filters.ChoiceFilter(label='Arrival Blood Transfusion',
                                                field_name='gcs__arr_coa_blood',
                                                choices=GCS.COCOA_CHOICES)
    wor_date = django_filters.DateTimeFilter(label='Worst Date & Time of GCS',
                                             field_name='gcs__wor_date')
    wor_status = django_filters.ChoiceFilter(choices=GCS.WORSTAT_CHOICES,
                                             field_name='gcs__wor_status',
                                             label='Worst Mental Status')
    wor_sbp = django_filters.CharFilter(label='Worst SBP', field_name='gcs__wor_sbp')
    wor_dbp = django_filters.CharFilter(label='Worst DBP', field_name='gcs__wor_dbp')
    wor_hr = django_filters.CharFilter(label='Worst HR', field_name='gcs__wor_hr')
    wor_rr = django_filters.CharFilter(label='Worst RR(회/min)', field_name='gcs__wor_rr')
    wor_eye = django_filters.ChoiceFilter(choices=GCS.GEYE_CHOICES,
                                          label='Worst GCS Eyes Opening', field_name='gcs__wor_eye')
    wor_verbal = django_filters.ChoiceFilter(choices=GCS.GVERBAL_CHOICES,
                                             label='Worst GCS Best Verbal Response', field_name='gcs__wor_verbal')
    wor_motor = django_filters.ChoiceFilter(choices=GCS.GMOTOR_CHOICES,
                                            label='Worst GCS Motor', field_name='gcs__wor_motor')
    wor_total = django_filters.CharFilter(label='Worst GCS Total', field_name='gcs__wor_total')
    wor_sum = django_filters.CharFilter(label='Worst Sum', field_name='gcs__wor_sum')
    wor_rts = django_filters.CharFilter(label='Worst RTS', field_name='gcs__wor_rts')
    wor_rtupper = django_filters.ChoiceFilter(choices=GCS.MOTOR_CHOICES,
                                              label='Worst Rt.Upper', field_name='gcs__wor_rtupper')
    wor_ltupper = django_filters.ChoiceFilter(choices=GCS.MOTOR_CHOICES,
                                              label='Worst Lt.Upper', field_name='gcs__wor_ltupper')
    wor_rtlower = django_filters.ChoiceFilter(choices=GCS.MOTOR_CHOICES,
                                              label='Worst Rt.Lower', field_name='gcs__wor_rtlower')
    wor_ltlower = django_filters.ChoiceFilter(choices=GCS.MOTOR_CHOICES,
                                              label='Worst Lt.Lower', field_name='gcs__wor_ltlower')
    wor_pp_right = django_filters.MultipleChoiceFilter(choices=GCS.PPLR_CHOICES,
                                                       label='Worst Pupils Right', field_name='gcs__wor_pp_right')
    wor_pp_left = django_filters.MultipleChoiceFilter(choices=GCS.PPLR_CHOICES,
                                                      label='Worst Pupils Left', field_name='gcs__wor_pp_left')
    wor_pp_rtsize = django_filters.ChoiceFilter(choices=GCS.PPSIZE_CHOICES,
                                                label='Worst Pupils Right Size', field_name='gcs__wor_pp_rtsize')
    wor_pp_ltsize = django_filters.ChoiceFilter(choices=GCS.PPSIZE_CHOICES,
                                                label='Worst Pupils Left Size', field_name='gcs__wor_pp_ltsize')
    wor_pp_rtshape = django_filters.ChoiceFilter(choices=GCS.PPSHAPE_CHOICES,
                                                 label='Worst Pupils Right Shape', field_name='gcs__wor_pp_rtshape')
    wor_pp_ltshape = django_filters.ChoiceFilter(choices=GCS.PPSHAPE_CHOICES,
                                                 label='Worst Pupils Left Shape', field_name='gcs__wor_pp_ltshape')
    wor_pp_rtprompt = django_filters.ChoiceFilter(choices=GCS.PPPROM_CHOICES, field_name='gcs__wor_pp_rtprompt',
                                                  label='Worst Pupils Right Prompt')
    wor_pp_ltprompt = django_filters.ChoiceFilter(choices=GCS.PPPROM_CHOICES, field_name='gcs__wor_pp_ltprompt',
                                                  label='Worst Pupils Left Prompt')
    wor_coa_correction = django_filters.ChoiceFilter(choices=GCS.COCOA_CHOICES, field_name='gcs__wor_coa_correction',
                                                     label='Worst Correction of coagulopathy')
    wor_coa_blood = django_filters.ChoiceFilter(choices=GCS.BLCOA_CHOICES, field_name='gcs__wor_coa_blood',
                                                label='Worst Blood Transfusion')
    wounds = django_filters.CharFilter(label='External Wounds', field_name='gcs__wounds')

    # Diagnosis
    diagnosis = django_filters.CharFilter(field_name='diagnosis__diagnosis', label='Diagnosis')
    primary_code = django_filters.CharFilter(field_name='diagnosis__primary_code', label='Primary diagnosis Code')
    primary_name = django_filters.CharFilter(field_name='diagnosis__primary_name', label='Primary diagnosis Name')
    skull = django_filters.MultipleChoiceFilter(field_name='diagnosis__skull', choices=Diagnosis.SKULL_CHOICES,
                                                label='Skull Injury')
    injury_position = django_filters.MultipleChoiceFilter(field_name='diagnosis__injury_position',
                                                          choices=Diagnosis.INJURY_POSITION_CHOICES,
                                                          label='Injury Position')
    position = django_filters.MultipleChoiceFilter(field_name='diagnosis__position', choices=Diagnosis.POSITION_CHOICES,
                                                   label='Position')
    hemorrhage = django_filters.MultipleChoiceFilter(field_name='diagnosis__hemorrhage',
                                                     choices=Diagnosis.HEMORRHAGE_CHOICES,
                                                     label='Hemorrhage Injury')
    hemorrhage_injury_position = django_filters.MultipleChoiceFilter(field_name='diagnosis__hemorrhage_injury_position',
                                                                     choices=Diagnosis.HEMORRHAGE_INJURY_POSITION_CHOICES,
                                                                     label='Injury Position')
    hemorrhage_position = django_filters.MultipleChoiceFilter(field_name='diagnosis__hemorrhage_position',
                                                              choices=Diagnosis.POSIT_CHOICES,
                                                              label='Hemorrhage Position')
    diffuse = django_filters.MultipleChoiceFilter(field_name='diagnosis__diffuse', choices=Diagnosis.DIFFUSE_CHOICES,
                                                  label='Diffuse Injury')
    vascular = django_filters.ChoiceFilter(field_name='diagnosis__vascular', choices=Diagnosis.VASCULAR_CHOICES,
                                           label='Vascular Injury')
    penetrating = django_filters.ChoiceFilter(field_name='diagnosis__penetrating',
                                              choices=Diagnosis.PENETRATING_CHOICES,
                                              label='Penetrating')
    fore = django_filters.ChoiceFilter(field_name='diagnosis__fore', choices=Diagnosis.FORE_CHOICES,
                                       label='Foreign body')

    # Injury
    head_neck = django_filters.ChoiceFilter(field_name='injury__head_neck', label='Head, Neck',
                                            choices=Injury.AIS_CHOICES)
    face = django_filters.ChoiceFilter(field_name='injury__face', label='Face', choices=Injury.AIS_CHOICES)
    chest = django_filters.ChoiceFilter(field_name='injury__chest', label='Chest', choices=Injury.AIS_CHOICES)
    abdomen = django_filters.ChoiceFilter(field_name='injury__abdomen', label='Abdomen', choices=Injury.AIS_CHOICES)
    extremity = django_filters.ChoiceFilter(field_name='injury__extremity', label='Extremity',
                                            choices=Injury.AIS_CHOICES)
    external = django_filters.ChoiceFilter(field_name='injury__external', label='External', choices=Injury.AIS_CHOICES)
    iss_score = django_filters.ChoiceFilter(field_name='injury__iss_score', label='ISS Score')
    marshall_score = django_filters.ChoiceFilter(field_name='injury__marshall_score', choices=Injury.MARS_CHOICES,
                                                 label='Marshall Score')

    # Monitor
    icp_timing = django_filters.ChoiceFilter(field_name='monitor__icp_timing', choices=Monitor.TIMING_ICP_CHOICES,
                                             label='Timing of ICP monitoring')
    icp_type = django_filters.ChoiceFilter(field_name='monitor__icp_type', choices=Monitor.TYPE_ICP_CHOICES,
                                           label='Type of ICP monitoring')
    icp_start_date = django_filters.DateFilter(field_name='monitor__icp_start_date',
                                               label='Start date of ICP monitoring')
    icp_end_date = django_filters.DateFilter(field_name='monitor__icp_end_date', label='End date of ICP monitoring')
    icp_location = django_filters.ChoiceFilter(field_name='monitor__icp_location', choices=Monitor.LOC_ICP_CHOICES,
                                               label='Location of ICP monitoring')
    icp_reason = django_filters.MultipleChoiceFilter(field_name='monitor__icp_reason',
                                                     choices=Monitor.REASON_ICP_CHOICES,
                                                     label='Reason for ICP')
    evd_timing = django_filters.ChoiceFilter(field_name='monitor__evd_timing', choices=Monitor.TIMING_EVD_CHOICES,
                                             label='Timing of EVD')
    evd_start_date = django_filters.DateFilter(field_name='monitor__evd_start_date', label='Start date of EVD')
    evd_end_date = django_filters.DateFilter(field_name='monitor__evd_end_date', label='End date of EVD')
    evd_location = django_filters.ChoiceFilter(field_name='monitor__evd_location', choices=Monitor.LOC_EVD_CHOICES,
                                               label='Location of EVD')
    evd_reason = django_filters.MultipleChoiceFilter(field_name='monitor__evd_reason',
                                                     choices=Monitor.REASON_EVD_CHOICES,
                                                     label='Reason for EVD')
    jb_timing = django_filters.ChoiceFilter(field_name='monitor__jb_timing', choices=Monitor.TIMING_JB_CHOICES,
                                            label='Timing of Jugular bulb')
    jb_start_date = django_filters.DateFilter(field_name='monitor__jb_start_date', label='Start date of Jugular bulb')
    jb_end_date = django_filters.DateFilter(field_name='monitor__jb_end_date', label='End date of Jugular bulb')
    jb_location = django_filters.ChoiceFilter(field_name='monitor__jb_location', choices=Monitor.LOC_JB_CHOICES,
                                              label='Location of Jugular bulb')
    jb_reason = django_filters.MultipleChoiceFilter(field_name='monitor__jb_reason', choices=Monitor.REASON_JB_CHOICES,
                                                    label='Reason for JB')
    bis_timing = django_filters.ChoiceFilter(field_name='monitor__bis_timing', choices=Monitor.TIMING_BIS_CHOICES,
                                             label='Timing of BIS')
    bis_start_date = django_filters.DateFilter(field_name='monitor__bis_start_date', label='Start date of BIS')
    bis_end_date = django_filters.DateFilter(field_name='monitor__bis_end_date', label='End date of BIS')
    bis_location = django_filters.ChoiceFilter(field_name='monitor__bis_location', choices=Monitor.LOC_BIS_CHOICES,
                                               label='Location of BIS')
    bis_reason = django_filters.MultipleChoiceFilter(field_name='monitor__bis_reason',
                                                     choices=Monitor.REASON_BIS_CHOICES,
                                                     label='Reason for Bis')

    # Surgery
    surgery_no = django_filters.NumberFilter(field_name='surgery__surgery_no', label='No of Surgery')
    aim = django_filters.MultipleChoiceFilter(field_name='surgery__aim', choices=Surgery.AIM_CHOICES,
                                              label='Aim of Surgery')
    typeof = django_filters.MultipleChoiceFilter(field_name='surgery__typeof', choices=Surgery.TYPE_CHOICES,
                                                 label='Type of Surgery')
    direction = django_filters.ChoiceFilter(field_name='surgery__direction', choices=Surgery.DIRECT_CHOICES,
                                            label='Direction of Surgery')
    intraevd = django_filters.ChoiceFilter(field_name='surgery__intraevd', choices=Surgery.INTRAEVD_CHOICES,
                                           label='Intraoperative EVD')
    intrasono = django_filters.ChoiceFilter(field_name='surgery__intrasono', choices=Surgery.INTRASONO_CHOICES,
                                            label='Intraoperative Sonography')
    surgery_name = django_filters.CharFilter(field_name='surgery__surgery_name', label='Name of Surgery')
    surgery_result = django_filters.CharFilter(field_name='surgery__surgery_result', label='Result of Surgery')
    orroom_date = django_filters.DateTimeFilter(field_name='surgery__orroom_date',
                                                label='Date & time of tranfer to OR room')
    surgery_start_date = django_filters.DateTimeFilter(field_name='surgery__surgery_start_date',
                                                       label='Start time of Surgery')
    surgery_end_date = django_filters.DateTimeFilter(field_name='surgery__surgery_end_date',
                                                     label='End time of Surgery')
    blood_loss = django_filters.CharFilter(field_name='surgery__blood_loss', label='Blood loss')
    ffp = django_filters.CharFilter(field_name='surgery__ffp', label='Transfusion(FFP)')
    prbc = django_filters.CharFilter(field_name='surgery__prbc', label='Transfusion(PRBC)')
    plt = django_filters.CharFilter(field_name='surgery__plt', label='Transfusion(PLT)')
    duroplasty = django_filters.ChoiceFilter(field_name='surgery__duroplasty', choices=Surgery.DURO_CHOICES,
                                             label='Duroplasty')

    # NonSurgicalTreatment
    sedation = django_filters.MultipleChoiceFilter(field_name='nonsurgicaltreatment__sedation',
                                                   choices=NonSurgicalTreatment.SEDA_CHOICES, label='Sedation Drug')
    hypothermia = django_filters.MultipleChoiceFilter(field_name='nonsurgicaltreatment__hypothermia',
                                                      choices=NonSurgicalTreatment.HYPO_CHOICES, label='Hypothermia')
    hyperosmolar = django_filters.MultipleChoiceFilter(field_name='nonsurgicaltreatment__hyperosmolar',
                                                       choices=NonSurgicalTreatment.HYPE_CHOICES,
                                                       label='Hyperosmolar Detail')
    crrt = django_filters.ChoiceFilter(field_name='nonsurgicaltreatment__crrt',
                                       choices=NonSurgicalTreatment.BOOL_CHOICES,
                                       label='CRRT')
    nogas = django_filters.ChoiceFilter(field_name='nonsurgicaltreatment__nogas',
                                        choices=NonSurgicalTreatment.BOOL_CHOICES, label='NO Gas')

    # Treatment
    neuro = django_filters.MultipleChoiceFilter(field_name='treatment__neuro', choices=Treatment.NEU_CHOICES,
                                                label='Neurological')
    cardio = django_filters.MultipleChoiceFilter(field_name='treatment__cardio', choices=Treatment.CAR_CHOICES,
                                                 label='Cardiovascular')
    hematopoetic = django_filters.MultipleChoiceFilter(field_name='treatment__hematopoetic',
                                                       choices=Treatment.HEMA_CHOICES, label='Hematopoetic')
    pulmonary = django_filters.MultipleChoiceFilter(field_name='treatment__pulmonary', choices=Treatment.PUL_CHOICES,
                                                    label='Pulmonary')
    giab = django_filters.MultipleChoiceFilter(field_name='treatment__giab', choices=Treatment.GIAB_CHOICES,
                                               label='GI/Abdomen')
    wound = django_filters.MultipleChoiceFilter(field_name='treatment__wound', choices=Treatment.WOUND_CHOICES,
                                                label='Wound')
    lab = django_filters.MultipleChoiceFilter(field_name='treatment__lab', choices=Treatment.LAB_CHOICES,
                                              label='Lab Abnomarlities')
    infection = django_filters.MultipleChoiceFilter(field_name='treatment__infection', choices=Treatment.INFE_CHOICES,
                                                    label='Infection other than pneumonia / Wound')
    othercomp = django_filters.MultipleChoiceFilter(field_name='treatment__othercomp', choices=Treatment.OTHER_CHOICES,
                                                    label='Other Complications')
    discharge_type = django_filters.ChoiceFilter(field_name='treatment__discharge_type', choices=Treatment.DIS_CHOICES,
                                                 label='Type of Discharge')
    causedeath = django_filters.ChoiceFilter(field_name='treatment__causedeath', choices=Treatment.DEATH_CHOICES,
                                             label='Cause of death')
    discharge_date = django_filters.DateFilter(field_name='treatment__discharge_date', label='Date of Discharge')

    # Assessment
    resultno = django_filters.NumberFilter(field_name='assessment__resultno', label='resultno')
    date = django_filters.DateFilter(field_name='assessment__date', label='Date')
    gcs_eye = django_filters.ChoiceFilter(field_name='assessment__gcs_eye', choices=Assessment.GEYE_CHOICES,
                                          label='GCS Eyes Opening')
    gcs_verbal = django_filters.ChoiceFilter(field_name='assessment__gcs_verbal', choices=Assessment.GVERBAL_CHOICES,
                                             label='GCS Best Verbal Response')
    gcs_motor = django_filters.ChoiceFilter(field_name='assessment__gcs_motor', choices=Assessment.GMOTOR_CHOICES,
                                            label='GCS Motor')
    gcs_total = django_filters.CharFilter(field_name='assessment__gcs_total', label='GCS Total')
    gcs_sum = django_filters.CharFilter(field_name='assessment__gcs_sum', label='GCS Sum')
    mmse = django_filters.CharFilter(field_name='assessment__mmse', label='MMSE')
    gose = django_filters.ChoiceFilter(field_name='assessment__gose', choices=Assessment.GOSE_CHOICES, label='GOSE')
    bathel = django_filters.CharFilter(field_name='assessment__bathel', label='Bathel Index')
    drs = django_filters.CharFilter(field_name='assessment__drs', label='DRS')
    mrs = django_filters.ChoiceFilter(field_name='assessment__mrs', choices=Assessment.MRS_CHOICES, label='MRS')

    class Meta:
        model = Patient
        fields = (
            'name', 'doctor', 'gender', 'birthday', 'contact', 'address', 'education', 'employment', 'insurance',
            'nationality', 'race', 'income', 'marriage', 'residence', 'handedness', 'religion')


class OverallFilter(django_filters.FilterSet):
    yearno = django_filters.CharFilter()

