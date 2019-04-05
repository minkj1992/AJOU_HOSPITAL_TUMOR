from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div
from crispy_forms.bootstrap import InlineRadios
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)
from django import forms

from .models import Patient, Trauma, Combine, History, GCS, Diagnosis, Injury, Monitor, Surgery, Treatment, Assessment, \
    NonSurgicalTreatment, Overall, Pittumor, Netumor, Meningtumor, Schtumor, Others, Results, Recurrence,Followup, \
    Chemotherapy,AdjuvantTherapy,SubSurgery,TumorSurgery

from ns_record_web.choices import *

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

class PatientForm(forms.ModelForm):
    age = forms.CharField(required=False, disabled=True)

    class Meta:
        model = Patient
        fields = ('patient_id', 'admission_date', 'doctor', 'name', 'gender', 'birthday', 'age', 'contact', 'address',
                  'education', 'education_detail', 'employment', 'employment_detail', 'insurance', 'insurance_detail',
                  'nationality', 'nationality_detail', 'race', 'race_detail', 'income', 'income_detail', 'marriage',
                  'marriage_detail', 'handedness', 'religion', 'religion_detail', 'extra_comment')


class TraumaForm(forms.ModelForm):
    differ = forms.CharField(disabled=True, required=False)

    class Meta:
        model = Trauma
        fields = ('check', 'confirm', 'injury_and_arrival_date_range', 'differ', 'type_admission',
                  'type_admission_detail',
                  'transfer_method', 'transfer_method_detail', 'pre_admission', 'pre_admission_detail',
                  'type_of_injury', 'type_of_injury_detail', 'place_of_injury', 'place_of_injury_detail',
                  'drug_intoxication', 'drug_intoxication_detail', 'cause_of_injury', 'cause_of_injury_detail', 'loc',
                  'loc_detail', 'extra_comment')


class CombineForm(forms.ModelForm):
    class Meta:
        model = Combine
        fields = (
            'check', 'confirm', 'other_major_operation', 'other_major_operation_detail', 'other_major_office',
            'non_tbi_surgery_date', 'extra_comment')


class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = ('check', 'confirm',
                  'psychiatric', 'psychiatric_detail', 'cardiovascular', 'cardiovascular_detail', 'endocrine',
                  'endocrine_detail',
                  'endocrine_detail', 'spinal', 'spinal_detail', 'neurologic', 'neurologic_detail', 'oncologic',
                  'oncologic_detail', 'gi', 'gi_detail',
                  'hepatic', 'hepatic_detail',
                  'hematologic', 'hematologic_detail', 'pulmonologic', 'pulmonologic_detail', 'renal', 'renal_detail',
                  'ent',
                  'ent_detail', 'musculoskeletal', 'musculoskeletal_detail', 'developmental', 'developmental_detail',
                  'anticoagulants',
                  'platelet', 'extra_comment')


class GCSForm(forms.ModelForm):
    class Meta:
        model = GCS
        fields = (
            'check', 'confirm',
            'arr_date', 'arr_status', 'arr_sbp', 'arr_dbp', 'arr_hr', 'arr_rr', 'arr_eye', 'arr_verbal', 'arr_motor',
            'arr_total', 'arr_sum', 'arr_rts', 'arr_rtupper', 'arr_ltupper', 'arr_rtlower', 'arr_ltlower',
            'arr_pp_right', 'arr_pp_rtsize', 'arr_pp_rtshape', 'arr_pp_rtprompt', 'arr_pp_left', 'arr_pp_ltsize',
            'arr_pp_ltshape', 'arr_pp_ltprompt', 'arr_coa_correction', 'arr_coa_blood',
            'wor_date', 'wor_status', 'wor_sbp', 'wor_dbp', 'wor_hr', 'wor_rr', 'wor_eye', 'wor_verbal', 'wor_motor',
            'wor_total', 'wor_sum', 'wor_rts', 'wor_rtupper', 'wor_ltupper', 'wor_rtlower', 'wor_ltlower',
            'wor_pp_right', 'wor_pp_rtsize', 'wor_pp_rtshape', 'wor_pp_rtprompt', 'wor_pp_left', 'wor_pp_ltsize',
            'wor_pp_ltshape', 'wor_pp_ltprompt', 'wor_coa_correction', 'wor_coa_blood', 'wounds', 'extra_comment')


class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = (
            'check', 'confirm', 'diagnosis', 'primary_code', 'primary_name', 'skull', 'injury_position', 'position',
            'position_detail', 'hemorrhage', 'hemorrhage_position', 'hemorrhage_position_detail', 'diffuse', 'vascular',
            'vascular_detail', 'penetrating', 'penetrating_detail', 'fore', 'fore_detail', 'extra_comment')


class InjuryForm(forms.ModelForm):
    class Meta:
        model = Injury
        fields = (
            'check', 'confirm', 'head_neck', 'face', 'chest', 'abdomen', 'extremity', 'external', 'iss_score',
            'marshall_score', 'extra_comment')


class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = (
            'check', 'confirm', 'icp_timing', 'icp_type', 'icp_start_date', 'icp_end_date', 'icp_location',
            'icp_reason',
            'icp_reason_detail', 'evd_timing', 'evd_start_date', 'evd_end_date', 'evd_location', 'jb_timing',
            'jb_start_date', 'jb_end_date', 'jb_location', 'jb_reason', 'jb_reason_detail', 'bis_timing',
            'bis_start_date', 'bis_end_date', 'bis_location', 'bis_reason', 'bis_reason_detail', 'extra_comment')


class SurgeryForm(forms.ModelForm):
    class Meta:
        model = Surgery
        fields = (
            'check', 'confirm', 'surgery_no', 'aim', 'aim_detail', 'typeof', 'typeof_detail', 'direction', 'intraevd',
            'intrasono', 'surgery_name', 'surgery_result', 'orroom_date', 'surgery_start_date', 'surgery_end_date',
            'blood_loss', 'ffp', 'prbc', 'plt', 'duroplasty', 'duroplasty_detail', 'extra_comment')


class NonSurgicalTreatmentForm(forms.ModelForm):
    class Meta:
        model = NonSurgicalTreatment
        fields = (
            'check', 'confirm', 'sedation', 'hypothermia', 'hyperosmolar', 'hyper_detail', 'crrt', 'nogas',
            'extra_comment')


class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = (
            'check', 'confirm', 'neuro', 'neuro_detail', 'cardio', 'cardio_detail', 'hematopoetic',
            'hematopoetic_detail',
            'pulmonary', 'pulmonary_detail', 'giab', 'giab_detail', 'wound', 'wound_detail', 'lab', 'lab_detail',
            'infection', 'infection_detail', 'othercomp', 'othercomp_detail', 'comp_comment',
            'discharge_type', 'causedeath', 'discharge_date', 'extra_comment')


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ('check', 'confirm', 'resultno', 'date', 'gcs_eye', 'gcs_verbal',
                  'gcs_motor', 'gcs_total', 'gcs_sum', 'mmse', 'gose', 'bathel', 'drs', 'mrs', 'extra_comment')


class OverallForm(forms.ModelForm):
    class Meta:
        model = Overall
        fields = '__all__'
        doctor = forms.ChoiceField(choices=DOCTOR_CHOICES, required=True)
        surgery = forms.ChoiceField(choices=SURGERY_CHOICES, required=True)
        sex = forms.ChoiceField(choices=SEX_CHOICES, required=True)
        ptype = forms.ChoiceField(choices=PATIENT_TYPE_CHOICES, required=True)
        distype = forms.ChoiceField(choices=DISEASE_TYPE_CHOICES, required=True)
        axis = forms.ChoiceField(choices=AXIS_CHOICES, required=True)
        tent = forms.ChoiceField(choices=TENT_CHOICES, required=True)
        class_field = forms.ChoiceField(choices=CLASS_CHOICES, required=True)
        cc = forms.ChoiceField(choices=CC_CHOICES, required=True)
        neusign = forms.ChoiceField(choices=NUESIGN_CHOICES, required=True)
        mental = forms.ChoiceField(choices=MENTAL_CHOICES, required=True)
        kps = forms.ChoiceField(choices=KPS_CHOICES, required=True)
        ictlesno = forms.ChoiceField(choices=CTLESNO_CHOICES, required=True)
        ictsite = forms.ChoiceField(choices=CTSITE_CHOICES, required=True)
        icthydr = forms.ChoiceField(choices=CTHYDR_CHOICES, required=True)
        icthemo = forms.ChoiceField(choices=CTHEMO_CHOICES, required=True)
        ictcalc = forms.ChoiceField(choices=CTCALC_CHOICES, required=True)
        thallium = forms.ChoiceField(choices=THALLIUM_CHOICES, required=True)
        mibi = forms.ChoiceField(choices=MIBI_CHOICES, required=True)
        ipetri = forms.ChoiceField(choices=PETRI_CHOICES, required=True)
        ipet = forms.ChoiceField(choices=PET_CHOICES, required=True)
        angiocom = forms.ChoiceField(choices=ANGIOCOM_CHOICES, required=True)

    # https://gist.github.com/linxuedong/e559b437a0b7d4dd6f6cd8a6d1a26e77
    # https: // simpleisbetterthancomplex.com / tutorial / 2018 / 11 / 28 / advanced - form - rendering - with-django - crispy - forms.html

    def __init__(self, *args, **kwargs):
        super(OverallForm, self).__init__(*args, **kwargs)
        # self.fields['doctor'].required = True
        # self.fields['sex'].required = True
        # self.helper.form_id = 'OverallForm'
        # self.helper.form_class = 'overall-form'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                # Div(InlineRadios('sex')),
                # Column(Div(InlineRadios('doctor'))),
                Column('year', css_class='form-group col-md-2 mb-0'),
                Column('ajbtno', css_class='form-group col-md-1 mb-0'),
                Column('doctor', css_class='form-group col-md-2 mb-0'),
                Column('surgery', css_class='form-group col-md-3 mb-0'),
                Column('sergno', css_class='form-group col-md-2 mb-0'),
                Column('idno', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('name', css_class='form-group col-md-2 mb-0'),
                Column('sex', css_class='form-group col-md-1 mb-0'),
                Column('regage', css_class='form-group col-md-1 mb-0'),
                Column('birthday', css_class='form-group col-md-2 mb-0'),
                Column('address', css_class='form-group col-md-2 mb-0'),
                Column('phone1', css_class='form-group col-md-2 mb-0'),
                Column('phone2', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('ptype', css_class='form-group col-md-2 mb-0'),
                Column('distype', css_class='form-group col-md-2 mb-0'),
                Column('axis', css_class='form-group col-md-2 mb-0'),
                Column('tent', css_class='form-group col-md-2 mb-0'),
                Column('class_field', css_class='form-group col-md-2 mb-0'),
                Column('cc', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('symptoms', css_class='form-group col-md-2 mb-0'),
                Column('neusign', css_class='form-group col-md-2 mb-0'),
                Column('signs', css_class='form-group col-md-2 mb-0'),
                Column('mental', css_class='form-group col-md-2 mb-0'),
                Column('kps', css_class='form-group col-md-2 mb-0'),
                Column('csremark', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('qolscore', css_class='form-group col-md-2 mb-0'),
                Column('pfhx', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            # Radiology
            Row(
                Column('ictday', css_class='form-group col-md-2 mb-0'),
                Column('ictlesno', css_class='form-group col-md-2 mb-0'),
                Column('ictsite', css_class='form-group col-md-2 mb-0'),
                Column('icthydr', css_class='form-group col-md-2 mb-0'),
                Column('icthemo', css_class='form-group col-md-2 mb-0'),
                Column('ictcalc', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('ictsize', css_class='form-group col-md-2 mb-0'),
                Column('ictfind', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            # Radiology (preop Initial MR Findings)
            Row(
                Column('imrday', css_class='form-group col-md-1 mb-0'),
                Column('imrlesno', css_class='form-group col-md-2 mb-0'),
                Column('imrsite', css_class='form-group col-md-2 mb-0'),
                Column('imrhydr', css_class='form-group col-md-2 mb-0'),
                Column('imrhemo', css_class='form-group col-md-2 mb-0'),
                Column('imrsize', css_class='form-group col-md-2 mb-0'),
                Column('imrfind', css_class='form-group col-md-1 mb-0'),
                css_class='form-row'
            ),
            # Radiology (preop Initial SPECT Findings)
            Row(
                Column('spectday', css_class='form-group col-md-2 mb-0'),
                Column('thallium', css_class='form-group col-md-2 mb-0'),
                Column('mibi', css_class='form-group col-md-2 mb-0'),
                Column('specfind', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            # Radiology (preop Initial PET Findings)
            Row(
                Column('ipetday', css_class='form-group col-md-2 mb-0'),
                Column('ipetri', css_class='form-group col-md-2 mb-0'),
                Column('ipet', css_class='form-group col-md-2 mb-0'),
                Column('ipetfind', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            # Radiology (preop Initial Angiography Findings)
            Row(
                Column('angioday', css_class='form-group col-md-2 mb-0'),
                Column('angiocom', css_class='form-group col-md-2 mb-0'),
                Column('angiofin', css_class='form-group col-md-2 mb-0'),
                Column('othraday', css_class='form-group col-md-2 mb-0'),
                Column('othrad', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', '저장'),
        )

class FollowupForm(forms.ModelForm):
    class Meta:
        model = Followup
        fields = '__all__'


class NetumorForm(forms.ModelForm):
    class Meta:
        model = Netumor
        fields = '__all__'


class PittumorForm(forms.ModelForm):
    class Meta:
        model = Pittumor
        fields = '__all__'


class MeningtumorForm(forms.ModelForm):
    class Meta:
        model = Meningtumor
        fields = '__all__'


class SchtumorForm(forms.ModelForm):
    class Meta:
        model = Schtumor
        fields = '__all__'


class OthersForm(forms.ModelForm):
    class Meta:
        model = Others
        fields = '__all__'

class TumorSurgeryForm(forms.ModelForm):
    class Meta:
        model = TumorSurgery
        fields = '__all__'

class SubSurgeryForm(forms.ModelForm):
    class Meta:
        model = SubSurgery
        fields = '__all__'

class AdjuvantTherapyForm(forms.ModelForm):
    class Meta:
        model = AdjuvantTherapy
        fields = '__all__'

class ChemotherapyForm(forms.ModelForm):
    class Meta:
        model = Chemotherapy
        fields = '__all__'

class RecurrenceForm(forms.ModelForm):
    class Meta:
        model = Recurrence
        fields = '__all__'

class ResultsForm(forms.ModelForm):
    class Meta:
        model = Results
        fields = '__all__'
