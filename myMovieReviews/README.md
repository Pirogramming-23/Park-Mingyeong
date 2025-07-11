# My Movie Reviews - 영화 리뷰 관리 시스템

개인 영화 리뷰를 작성하고 관리할 수 있는 Django 웹 애플리케이션입니다.

## 🎬 주요 기능

### 📝 리뷰 리스트 페이지
- 작성한 모든 리뷰들의 개요 표시
- 영화 제목, 개봉년도, 장르, 별점 정보 제공
- 영화 제목 클릭 시 해당 리뷰의 디테일 페이지로 이동
- '리뷰 작성' 버튼으로 새 리뷰 작성 페이지 이동

### 📖 리뷰 디테일 페이지
- 해당 리뷰의 전체 내용 표시
- 영화 제목, 감독, 주연, 장르, 별점, 러닝타임, 리뷰 내용 포함
- 'My Movie Reviews' 클릭 시 리뷰 리스트 페이지로 이동
- '수정' 버튼으로 해당 리뷰 수정 페이지 이동
- '삭제' 버튼으로 해당 리뷰 삭제

### ✏️ 리뷰 작성 & 수정 페이지
- 새 리뷰 작성 시: 빈 폼 제공
- 리뷰 수정 시: 기존 정보로 폼 자동 채움
- 영화 제목, 감독, 주연, 장르, 별점, 러닝타임, 리뷰 내용 입력
- 새 리뷰 작성 후 저장 시 리뷰 리스트 페이지로 이동
- 리뷰 수정 후 저장 시 해당 리뷰 디테일 페이지로 이동

## 🛠️ 기술 스택

- **Backend**: Django 5.2.4
- **Database**: SQLite
- **Frontend**: Bootstrap 5.3.0, Font Awesome 6.0.0
- **Language**: Python 3.x

## 🚀 설치 및 실행

### 1. 프로젝트 클론
```bash
git clone <repository-url>
cd myMovieReviews
```

### 2. 가상환경 활성화
```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. 의존성 설치
```bash
pip install -r requirements.txt
```

### 4. 데이터베이스 마이그레이션
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. 슈퍼유저 생성 (선택사항)
```bash
python manage.py createsuperuser
```

### 6. 개발 서버 실행
```bash
python manage.py runserver
```

### 7. 브라우저에서 접속
- 메인 페이지: http://127.0.0.1:8000/
- 관리자 페이지: http://127.0.0.1:8000/admin/

## 📁 프로젝트 구조

```
myMovieReviews/
├── movie_reviews/          # Django 프로젝트 설정
│   ├── settings.py        # 프로젝트 설정
│   ├── urls.py           # 메인 URL 설정
│   └── wsgi.py           # WSGI 설정
├── reviews/              # 영화 리뷰 앱
│   ├── models.py         # MovieReview 모델
│   ├── views.py          # 뷰 (CRUD 기능)
│   ├── forms.py          # 폼 클래스
│   ├── urls.py           # 앱 URL 설정
│   ├── admin.py          # 관리자 설정
│   └── templates/        # 템플릿 파일들
│       └── reviews/
│           ├── base.html              # 기본 레이아웃
│           ├── review_list.html       # 리뷰 목록
│           ├── review_detail.html     # 리뷰 상세
│           ├── review_form.html       # 리뷰 작성/수정
│           └── review_confirm_delete.html # 삭제 확인
├── manage.py             # Django 관리 스크립트
└── README.md            # 프로젝트 설명서
```

## 🎯 CRUD 기능 구현

### Create (생성)
- `MovieReviewCreateView`: 새 리뷰 작성
- URL: `/create/`
- 메서드: GET (폼 표시), POST (저장)

### Read (읽기)
- `MovieReviewListView`: 리뷰 목록 조회
- `MovieReviewDetailView`: 리뷰 상세 조회
- URL: `/` (목록), `/<id>/` (상세)

### Update (수정)
- `MovieReviewUpdateView`: 기존 리뷰 수정
- URL: `/<id>/update/`
- 메서드: GET (폼 표시), POST (저장)

### Delete (삭제)
- `MovieReviewDeleteView`: 리뷰 삭제
- URL: `/<id>/delete/`
- 메서드: GET (확인 페이지), POST (삭제 실행)

## 🎨 UI/UX 특징

- **반응형 디자인**: 모바일, 태블릿, 데스크톱 지원
- **모던한 디자인**: Bootstrap 5와 그라데이션 배경
- **직관적인 네비게이션**: 명확한 버튼과 아이콘
- **사용자 친화적**: 한글 인터페이스와 직관적인 레이아웃
- **시각적 피드백**: 별점 표시, 장르 배지, 호버 효과

## 🔧 관리자 기능

- Django 관리자 페이지에서 모든 리뷰 관리
- 필터링, 검색, 정렬 기능
- 일괄 편집 및 삭제 가능

## 📝 라이선스

이 프로젝트는 개인 학습 목적으로 제작되었습니다.

## 👨‍💻 개발자

개발자: [이름]
과제: Django CRUD 개인 과제 