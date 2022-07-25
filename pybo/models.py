# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    # author 필드는 User 모델을 ForeignKey로 적용하여 선언
    # User 모델은 django.contrib.auth 앱이 제공하는 사용자 모델로 회원 가입시 데이터 저장에 사용했던 모델이다.
    # on_delete=models.CASCADE는 계정이 삭제되면 이 계정이 작성한 질문을 모두 삭제하라는 의미
    modify_date = models.DateTimeField(null=True, blank=True) #먼저 질문이나 답변이 언제 수정되었는지 확인
    subject = models.CharField(max_length=200)  # 질문 제목
    content = models.TextField()  # 질문내용
    create_date = models.DateTimeField()  # 질문의 작성일자
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 질문
    content = models.TextField()  # 답변의 내용
    create_date = models.DateTimeField()  # 답변일시
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')
    # null=True는 데이터베이스에서 modify_date 칼럼에 null을 허용한다는 의미
    # blank=True는 form.is_valid()를 통한 입력 데이터 검증 시 값이 없어도 된다는 의미
    # null=True, blank=True는 어떤 조건으로든 값을 비워둘 수 있음을 의미
    # 수정일시는 수정한 경우에만 생성되는 데이터이므로 null=True, blank=True를 지정
