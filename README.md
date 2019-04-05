# ns-record-website
이 프로젝트는 신경외과에서 엑셀 및 엑세스로 입력하던 데이터를 웹상에서 한 번에 관리하고
검색을 용이하게 하기 위해 개발되었습니다. 

Trauma 데이터와 Tumor 데이터를 입력하록 되어 있으며 담당 교수님은 다음과 같습니다.
- Trauma : 신경외과 유남규 교수님 (실무자 : 담당간호사 서숙진 선생님)
- Tumor : 신경외과 김세혁 과장님

## 설치
- Python 3.6 사용
- virtualenv 로 파이썬 가상환경 구축 및 활성화
- 인터넷이 되는 환경일 경우 `pip install -r requirements.txt` 수행하면 패키지들 설치 됩니다.
- 인터넷이 되지 않을 경우 인터넷이 되는 컴퓨터에서 `requirements.txt` 에 명시된 패키지와 버전을 https://pypi.org/ 에서 검색합니다.
- 패키지가 검색이 되면 `Download Files` 라는 메뉴가 있을 텐데 거기서 `whl` 파일이나 없으면 `tar.gz` 혹은 `zip` 파일을 다운로드합니다.
- 다운로드한 파일들을 설치할 컴퓨터로 옮기고 나서 역시 가상환경을 활성화한 상태로 pip 로 설치합니다.  `pip install <파일이름>` 으로 설치하면 됩니다.
- 모든 패키지를 설치하면 데이터베이스 연동을 수행해야 합니다.
- 현재 이 프로젝트는 Microsoft SQL Server 최신버전에 맞추어 개발되었습니다. SQL Server 를 설치해주세요.
- `ns_record_web/settings/` 폴더에는 개발 / 배포 환경 별로 데이터베이스 설정 파일이 분리되어 있습니다.
- 개발시에는 SQL Server를 설치하고 `python manage.py migrate --settings ns_record_web.settings.local` 명렁어로 테이블을 생성하세요.

