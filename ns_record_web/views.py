import collections

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied, FieldError
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from djqscsv import render_to_csv_response

from .filters import PatientFilter, OverallFilter
from .forms import PatientForm, TraumaForm, CombineForm, HistoryForm, GCSForm, DiagnosisForm, InjuryForm, MonitorForm, \
    SurgeryForm, TreatmentForm, AssessmentForm, NonSurgicalTreatmentForm, OverallForm, FollowupForm, NetumorForm, \
    PittumorForm, MeningtumorForm, SchtumorForm, OthersForm
from .models import Patient, Trauma, Combine, History, GCS, Diagnosis, Injury, Monitor, Treatment, Assessment, Surgery, \
    NonSurgicalTreatment, Overall, Followup, Netumor, Pittumor, Meningtumor, Schtumor, Others


def index(request, exception=None):
    """
    Trauma와 Tumor 전환하는 index 페이지 렌더링
    :param request:
    :param exception:
    :return: status 와 함께 index.html 반환
    """

    status = 403 if exception else None

    return render(request, 'index2.html', status=status)

def index2(request,exception=None):
    status = 403 if exception else None
    return render(request, 'index.html',status=status)

@login_required
def patient_list(request, mode):
    # mode에 맞는 권한이 없거나 staff 유저가 아니면 접속할 수 없음
    if not (request.user.groups.filter(name=mode).exists() or request.user.is_staff):
        raise PermissionDenied()

    # namedtuple 을 이용해서 쉽게 모드별로 attribute 설정
    Mode = collections.namedtuple('Mode', 'model steps filter_class')

    modes = {
        'trauma': Mode(model=Patient, steps=(
            3, 'trauma', 'combine', 'history', 'gcs', 'diagnosis', 'injury', 'monitor', 'surgery_set', 'nonsurgicaltreatment',
            'treatment', 'assessment_set'), filter_class=PatientFilter),
        'tumor': Mode(model=Overall,
                      steps=('Overall', 'Followup', 'NeTumor', 'PitTumor', 'MeningTumor', 'SchTumor', 'Others'),
                      filter_class=OverallFilter)
    }

    current_mode = modes[mode]  # 현재 모드
    queryset = current_mode.model.objects.all()  # 현재 모드의 모델에 해당하는 쿼리셋
    # 환자 검색을 위한 필터 객체 생성 (django-filter)
    # 위의 쿼리셋 및 사용자의 입력을 통해 쿼리셋을 뽑아낸다.
    patient_filter = current_mode.filter_class(request.GET, queryset=queryset)

    if 'csv-download' in request.GET:  # csv-download 버튼을 클릭해씅ㄹ 경우
        return render_to_csv_response(patient_filter.qs, streaming=True)

    paginator = Paginator(patient_filter.qs, 10)  # patient_filter 의 쿼리셋을 pagination
    page = request.GET.get('page')

    patients = paginator.get_page(page)
    steps = current_mode.steps

    # check 변수 별로 색깔을 지정하기 위함
    color_by_check = {
        1: 'red',
        2: 'darkgray',
        3: 'green'
    }

    for patient in patients:
        patient.checks = []

        for step in steps:
            # step 이 int 인 것은 따로 check field 가 존재하지 않거나 목록형태라는 것을 의미
            if isinstance(step, int) or mode == 'tumor':
                patient.checks.append(color_by_check.get(step, step))
            else:
                try:
                    # 만약 patient instance 에 step 이 존재하면 그것의 check 를 넣어줌
                    if 'set' in step:
                        patient.checks.append(getattr(patient, step).count())
                    else:
                        patient.checks.append(color_by_check[getattr(patient, step).check])
                except getattr(Patient, step).RelatedObjectDoesNotExist:
                    # 만약 없다면 그냥 1을 넣어줌
                    patient.checks.append('red')

    context = {
        'patient_filter_form': patient_filter.form,
        'patients': patients,
        'search_count': patient_filter.qs.count(),
        'count': queryset.count(),
        'mode': mode
    }

    return render(request, 'patient_list.html', context)

@login_required
def profile(request):
    context = {
        'groups': request.user.groups.all()
    }

    return render(request, 'profile.html', context=context)


@login_required
def wizard_view(request, step_number, patient_id, mode, object_id=None):
    #  index 사용하는
    Mode = collections.namedtuple('Mode', 'model model_and_form steps descriptions')

    modes = {
        'trauma': Mode(model=Patient,
                       model_and_form=((Patient, PatientForm), (Trauma, TraumaForm), (Combine, CombineForm),
                                       (History, HistoryForm), (GCS, GCSForm), (Diagnosis, DiagnosisForm),
                                       (Injury, InjuryForm),
                                       (Monitor, MonitorForm), (Surgery, SurgeryForm),
                                       (NonSurgicalTreatment, NonSurgicalTreatmentForm),
                                       (Treatment, TreatmentForm),
                                       (Assessment, AssessmentForm)),
                       steps=(3, 'trauma', 'combine', 'history', 'gcs', 'diagnosis', 'injury', 'monitor', 0,
                              'nonsurgicaltreatment','treatment', 0),
                       descriptions=(
                           'Patient Information', 'Trauma History', 'Combined Injury', 'Medical History',
                           'Neurological Assessment', 'Diagnosis', 'Injury Severity Score', 'Invasive Monitoring',
                           'Surgery',
                           'Non-Surgical Treatment', 'Treatment', 'Assessment of Result')),
        # namedTuple을 활용하여 Mode라는 class 생성
        'tumor': Mode(model=Overall,
                      # model과 form을 부착해준다
                      model_and_form=((Overall, OverallForm), (Followup, FollowupForm), (Netumor, NetumorForm),
                                      (Pittumor, PittumorForm), (Meningtumor, MeningtumorForm),
                                      (Schtumor, SchtumorForm), (Others, OthersForm)),
                      #  페이지 위에 보여질 setps들
                      steps=('Overall', 'Followup', 'NeTumor', 'PitTumor', 'MeningTumor', 'SchTumor', 'Others'),
                      descriptions=('Overall', 'Followup', 'NeTumor', 'PitTumor', 'MeningTumor', 'SchTumor', 'Others'))
    }

    # request 받은 mode로 현재 mode 설정 및 기타 내용들 변수화
    current_mode = modes[mode]
    models_and_forms = current_mode.model_and_form
    # step_number 가 1이면 환자를 새로 생성해야 하므로 오브젝트를 받아올 필요가 없음
    patient = get_object_or_404(current_mode.model, pk=patient_id) if step_number >= 2 else ''
    patient_info = str(patient)

    steps = current_mode.steps
    descriptions = current_mode.descriptions
    step_descriptions = []

    for idx, step in enumerate(steps):
        desc = descriptions[idx]

        # if isinstance(step, int) or mode == 'tumor':
        #  mode==tumor 넣으신 이유가 디버깅 떄문일까?
        if isinstance(step, int) or mode == 'tumor':
            step_descriptions.append((desc, step))
        else:
            try:
                # 만약 patient instance 에 step 이 존재하면 그것의 check 를 넣어줌
                #  getattr(object, name[, default])
                step_descriptions.append((desc, getattr(patient, step).check))
            except (getattr(current_mode.model, step).RelatedObjectDoesNotExist, AttributeError):
                # 만약 없다면 그냥 1을 넣어줌
                step_descriptions.append((desc, 1))

    context = {
        'step_number': step_number,
        'step_descriptions': step_descriptions,
        'patient_id': patient_id,
        'patient_info': patient_info,
        'mode': mode
    }

    try:
        model_class, form_class = models_and_forms[step_number - 1]
    except IndexError:
        raise Http404('Step does not exist')

    try:
        if object_id is None:  # object_id 가 None 이라는 말은 목록이 아니라 1:1 관계를 이루는 테이블임
            if step_number in (9, 12) and mode == 'trauma':
                # 트라우마이면서 9, 12 번 스텝이면 MultipleObjectsReturned 해서 아래로 넘어감
                raise model_class.MultipleObjectsReturned
            else:
                try:
                    # 일단 patient_id 필드로 오브젝트를 조회해본다
                    exist_object = model_class.objects.get(patient_id=patient_id)
                except FieldError:
                    # patient_id 필드가 없었을 경우 두가지 경우가 있다
                    if step_number == 1:
                        # Patient 는 환자 id column 이름이 patient_id 가 아니고 기본키라서
                        exist_object = model_class.objects.get(pk=patient_id)
                    else:
                        # For tumor
                        exist_object = model_class.objects.filter(idno=patient_id).first()
        else:
            # object_id가 있으면 그냥 pk로 조회하면 됨
            exist_object = model_class.objects.get(pk=object_id)
    except model_class.MultipleObjectsReturned:
        # 여러 오브젝트가 있으므로 object_list 를 렌더링 할 수 있도록 컨텍스트를 준비한다.
        objects = model_class.objects.filter(patient_id=patient_id)
        context['objects'] = objects
        context['class_name'] = model_class.__name__

        return render(request, 'object_list.html', context=context)
    except (model_class.DoesNotExist, model_class.MultipleObjectsReturned):
        # 오브젝트가 존재하지 않는 다는 것은 새로 만들어야 한다는 뜻이므로
        # 각 상황에 따라서 exist_object 를 생성해준다.
        if step_number > 1:
            if mode == 'trauma':
                exist_object = model_class(patient_id=patient_id)
            else:
                exist_object = model_class(idno=patient_id)
        else:
            exist_object = None

    try:
        # 위에서 만든 exist_object를 이용해서 form을 만든다.
        form = form_class(request.POST or None, instance=exist_object)
    except AttributeError:
        form = None

    if form.is_valid():
        # 폼이 유효하다는 것은 사용자가 제출을 했다는 것
        obj = form.save()

        if step_number == len(models_and_forms):
            # step_number 가 models_and_forms 의 갯수와 같다는 것은 마지막 스텝이라는 걸 의미하므로
            # redirect 해야함
            return redirect('trauma')
        else:
            # 마지막 스텝이 아닐 경우 redirect 할 준비
            if mode == 'trauma':
                id_ = 'patient_id'  # trauma 일 때 id
            else:
                if step_number == 1:
                    id_ = 'id'  # patient 모드일떄 id
                else:
                    id_ = 'idno'  # tumor 일 때 id

            return redirect('wizard', mode=mode, step_number=step_number + 1, patient_id=getattr(obj, id_))

    context['form'] = form

    return render(request, 'wizard.html', context=context)

