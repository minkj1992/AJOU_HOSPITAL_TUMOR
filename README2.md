# Tumor
알바

## 0401
- 기본환경 setting
- DB 모델에 대하여 설명들음
- 코드 구조 학습 및 사용된 라이브러리 검색 

## 0402
- `models.py` 수정 작업
  - Overall class 분리( pk,fk 생성)
    - `Overall`
    - `TumorSurgery`(1:1 = Overall : Tumor)
    - `SubSurgery` (1:N = TumorSurgery : Subsurgery)
    - `AdjuvantTherapy` (1:1 = Overall : AdjuvantTherapy)
      - Radiation therapy
      - Radio surgery
      - Threarpeutic trial
    - `Chemotherapy` (1:N = AdjuvantTherapy : Chemotherapy)
  - Followup class 분리 
    - `Followup` (1:N = Overall : Followup)
    - `Recurrence` (1:N = Overall : Recurrence)
    - `Results` (1:1 = Overall : Results)
  - `migration error` 처리
    - 50개의 migration이 SQl Query화 되다 보니, 쿼리 끼리의 에러가 발생하여 모두 삭제
    - 이후 `makemigrations`, `migrate`
    
추후의 모델링 수정 작업은 각 모델 끼리의 관계와 모델의 역활을 의논하고 진행해야 될 것 같다.

## 0403

- index.html(home page 생성) 
  - 처음 들어갔을때 main화면 생성
  - Trauma or Tumor 선택하도록함.


- 코드 분석
  - `path('advanced_filters/', include('advanced_filters.urls'))`
    - `django-advanced-filters 1.1.1`를 사용하여 필터링을 하고자 하였으나 적용 x
  - 페이지
    - 1. Trauma or Tumor page (선택시 patient_list로 간다)
    - 2. 환자 목록(patient_lists)
    - 3. 새로운 환자 입력 (wizard.html + wizard_view)
  - views.py
    - `getattr(object, name[, default])`
    - `collections.namedtuple('Mode', 'model model_and_form steps descriptions')`
    - `if isinstance(step, int) or mode == 'tumor'`
    - `if object_id is None:` # object_id 가 None 이라는 말은 목록이 아니라 1:1 관계를 이루는 테이블임
      - 이게 무슨말이지 (181 line)
    - `wizard_view`는 tumor/trauma에 따라 model을 보여주고, 각 상황에 맞게 error 처리및 rendering, form에 관해서는 save 외에는 없다.

- form 변형 시키기
  - `col-md-3`: bootstrap은 grid 12가 1 row, md는 중간크기, 3은 12중 3-size
  - `m`: margin
  - `mb`: margin-bottom 
  - `mb-0` : 
  - `forms.py`의 `overallform` 재생성 (한 화면에 작게 레이아웃 적용, compact하게 보여짐)




> 내일 할일
- inlineformset_factory 사용하여 fk로 엮인 모델 한 form에서 보여주기 [미완]


