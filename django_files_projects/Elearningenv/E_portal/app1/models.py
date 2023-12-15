from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape,mark_safe
from django.contrib.auth import get_user_model
from embed_video.fields import EmbedVideoField

# Create your models here.

class User(AbstractUser):
    is_learner=models.BooleanField(default=False)
    is_instructor=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to='',default='no-img.jpg',blank=True,null=True)
    first_name=models.CharField(max_length=255, default='')
    last_name=models.CharField(max_length=255, default='')
    email=models.EmailField(default='none@email.com')
    phonenumber=models.CharField(max_length=255, blank=True,null=True)
    birth_date=models.DateField(default='1975-12-12')
    bio=models.TextField(default='')
    city=models.CharField(max_length=255, default='')
    state=models.CharField(max_length=200, default='')
    country=models.CharField(max_length=200,default='')
    favorite_animal=models.CharField(max_length=200, default='')
    hobby=models.CharField(max_length=300, default='')

    def __str__(self):
        return self.user.username


class Announcement(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    posted_at=models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.content



class Course(models.Model):
    name=models.CharField(max_length=30)
    color=models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name
    
    def get_html_badge(self):
        name=escape(self.name)
        color=escape(self.color)
        html='<span class="badge badge-primary" style="background-color:#808080"; ></span>'
        return mark_safe(html)
    

class Tutorial(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    thumb=models.ImageField(upload_to='',null=True, blank=True)
    course=models.ForeignKey(Course, on_delete=models.CASCADE, default='Math')
    created_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    video=EmbedVideoField(blank=True,null=True)


class Notes(models.Model):
    title=models.CharField(max_length=500)
    file=models.FileField(upload_to='',null=True, blank=True)
    cover=models.ImageField(upload_to='',blank=True,null=True)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.file.delete()
        self.cover.delete()
        super().delete(*args,**kwargs)


class Quiz(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE, related_name='')
    name=models.CharField(max_length=300)
    course=models.ForeignKey(Course, on_delete=models.CASCADE, related_name='')

    def __str__(self):
        return self.name
    

class Question(models.Model):
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='')
    text=models.CharField('Question', max_length=255)

    def __str__(self):
        return self.text
    


class Answer(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE, related_name='')
    text=models.CharField('Answer', max_length=255)
    is_correct=models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text
    

class Learner(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes=models.ManyToManyField(Quiz,through='TakenQuiz')
    interests=models.ManyToManyField(Course,related_name='interested_learner')


  """   def get_unanswered_questions(self,quiz):
        answered_questions=self.quiz_answers\
                .filter(answer_question_quiz=quiz)\
                .values_list('answer_question_pk',flat=True)
        questions=quiz.questions.exclude(pk_in=answered_questions).order()
        return questions """