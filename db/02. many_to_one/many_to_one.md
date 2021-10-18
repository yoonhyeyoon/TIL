# 02. many_to_one

> 2021.10.18



## Django Relationship fields

> https://docs.djangoproject.com/ko/3.1/ref/models/fields/#module-django.db.models.fields.related



## ForeignKey (1:N Relation)

> A many-to-one relationship

**개념**

* 외래 키 (외부 키)

- 외래 키는 참조하는 테이블에서 1개의 키(속성 또는 속성의 집합)에 해당하고, 참조하는 측의 관계 변수는 참조되는 측의 테이블의 키를 가리킨다.
- 하나(또는 복수) 다른 테이블의 기본 키 필드를 가리키는 데이터의 참조 무결성(Referential Integrity)를 확인하기 위하여 사용된다. 즉, 허용된 데이터 값만 데이터베이스에 저장되는 것이다.

> [참조 무결성] 2개의 테이블 간의 일관성을 말함

**특징**

- 외래 키를 사용하여 **부모 테이블의 유일한 값을 참조**한다. (ex. PK )
- 외래 키의 값이 부모 테이블의 기본 키 일 필요는 없지만 **유일**해야 한다.



**comment 모델 정의**

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```

- 한 테이블에 있는 두 개 이상의 레코드가 다른 테이블에 있는 하나의 레코드를 참조할 때, 두 모델 간의 관계를 일대다 관계라고 한다.
- Article : Comment = 1 : N -> 하나의 게시글에는 여러 개의 댓글이 달릴 수 있다.

##### `on_delete`

> https://docs.djangoproject.com/en/3.2/ref/models/fields/#database-representation

- ForeignKey의 필수 인자
- ForeignKey가 참조하고 있는 부모(Article) 객체(=게시글)가 사라졌을 때 달려 있는 댓글들을 어떻게 처리할 지 정의

> [데이터 무결성] 데이터의 정확성과 일관성을 유지하고 보증하는 것

- Database Integrity(데이터 무결성)을 위해서 매우 중요한 설정이다.
  - **개체 무결성**: 식별자는 NULL 혹은 중복일 수 없다. (PK / NOT NULL)
  - 참조 무결성: FK 값이 데이터베이스의 특정 테이블의 PK 값을 참조하는 것
  - 범위 / 도메인 무결성 : 컬럼은 지정된 형식을 만족해야한다. 



**possible values for `on_delete`**

- `CASCADE` : **부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제**한다.
- `PROTECT` : 부모 객체를 삭제할 때 참조하는 객체가 하나라도 있으면 삭제 불가
- `SET_NULL` : 부모객체가 삭제 됐을 때 모든 값을 NULL로 치환. (NOT NULL 조건시 불가능)
- `SET_DEFAULT` : 모든 값이 DEFAULT 값으로 치환 
- `SET()` : 특정 함수 호출
- `DO_NOTHING` : 아무것도 하지 않음
- `RESTRICT` : PROTECT 의 약한 버전. 적용 범위가 더 좁다. 직접적인 관계일 때는 부모 객체 삭제 가능



**데이터베이스 표현**

- Django는 필드 이름에 `_id`를 추가하여 데이터베이스 열 이름을 만듦



**Table 직접 확인하기**

- `article_id` 라는 컬럼이 생성되었다. 우리가 댓글을 작성하면 댓글이 해당하는 글이 **몇 번째 게시 글의 댓글인지 알아야 하기 때문**
- 만약 ForeignKey 를 article 이라고 하지 않고 `abcd = models.ForeignKey(..)` 형태로 생성 했다면 `abcd_id` 로 만들어진다. 이렇게되면 모델 관계를 파악하는 것이 어렵기 때문에 **부모 클래스명의 소문자(단수형)로 작성하는 것이 바람직하다.**

**1 : N 관계 manager**

- Article(1) : Comment(N) : `comment_set`
  - `article.comment` 형태로는 가져올 수 없다.
  - 게시글에 몇 개의 댓글이 있는지 Django ORM이 보장할 수 없기 때문 (본질적으로는 애초에 Article 클래스에 Comment 와의 어떠한 관계도 연결하지 않음)
  - article 는 comment 가 있을 수도 있고, 없을 수도 있기 때문
- Comment(N) : Article(1) : `article`
  - 그에 반해 댓글의 경우 `comment.article` 식의 접근이 가능한 이유는 어떠한 댓글이든 반드시 자신이 참조하고 있는 게시글이 있으므로 이와 같이 접근할 수 있다.

##### `related_name`

> https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.ForeignKey.related_name

- 위에서 확인한 것처럼 부모 테이블에서 역으로 참조할 때(the relation from the related object back to this one.) `모델이름_set` 이라는 형식으로 참조한다. (**역참조**)

- related_name 값은 django 가 기본적으로 만들어 주는 `_set` 명령어를 임의로 변경할 수 있다.

  ```python
  # articles/models.py
  
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    ...
  ```

- 위와 같이 변경하면 `article.comment_set` 은 더이상 사용할 수 없고 `article.comments` 로 대체된다.

- 1:N 관계에서는 거의 사용하지 않지만 M:N 관계에서는 반드시 사용해야 할 경우가 발생한다.



------



## Comment

### CREATE

- CommentForm 작성

  ```python
  # forms.py
  
  from .models import Article, Comment
  
  class CommentForm(forms.ModelForm):
  
      class Meta:
          model = Comment
          fields = '__all__'
  ```

- detail 에서 commentform 보여주기

  ```python
  from .forms import ArticleForm, CommentForm
  
  def detail(request, pk):
      article = Article.objects.get(pk=pk)
      comment_form = CommentForm()
      context = {
          'article': article,
          'comment_form': comment_form,
      }
      return render(request, 'articles/detail.html', context)
  ```

- **detail page 에 댓글 작성 form 추가**

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    ...
    <a href="{% url 'articles:index' %}">back</a>
    <hr>
    <form action="" method="POST">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit">
    </form>
  {% endblock %}
  ```

- 그런데 외래키를 직접 입력한다. Comment

  ```python
  class CommentForm(forms.ModelForm):
  
      class Meta:
          model = Comment
          exclude = ['article',]
  ```

```python
# articles/urls.py

path('<int:pk>/comments/', views.comments_create, name='comments_create'),
save()
```



**save method**

> https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/#the-save-method

- 우리가 `models.py` 에서 `Comment` 클래스를 정의 했을 때 필드(컬럼)을 `article`과`content` 2개를 설정했다. 데이터 무결성의 원칙에 따라 해당 필드는 레코드가 없는 NULL 일 상태 일 수 없기 때문에 값을 넣어 주어야 한다.

  ```python
  # articles/views.py
  
  @require_POST
  def comments_create(request, pk):
      article = Article.objects.get(pk=pk)
      comment_form = CommentForm(request.POST)
      if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.article = article
          comment.save()
          return redirect('articles:detail', article.pk)
      context = {
          'comment_form': comment_form,
          'article': article,
      }
      return render(request, 'articles/detail.html', context)
  ```

  ```django
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
  ```

  - 댓글을 작성한 후 admin 페이지 혹은 sqlite 확장에서 확인



### READ

- 특정 article에 있는 모든 댓글을 가져온 후 template 으로 전달한다.

  ```python
  # articles/views.py
  
  from .models import Article, Comment
  
  def detail(request, pk):
      article = Article.objects.get(pk=pk)
      comment_form = CommentForm()
      comments = article.comment_set.all()
      context = {
          'article': article,
          'comment_form': comment_form,
          'comments': comments,
      }
      return render(request, 'articles/detail.html', context)
  ```

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    ...
    <a href="{% url 'articles:index' %}">back</a>
    <hr>
    <h4>댓글 목록</h4>
    {% for comment in comments %}
      <li>{{ comment.content }}</li>
    {% endfor %}
    <hr>
    ...
  {% endblock %}
  ```



### DELETE

```django
# articles/urls.py

path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
# articles/views.py

@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
<!-- articles/detail.html -->

{% extends 'base.html' %}

{% block content %}
  ...
  <h4>댓글 목록</h4>
  {% for comment in comments %}
    <li>
      {{ comment.content }}
      <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" class="d-inline">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
    </li>
  {% endfor %}
  <hr>
	...
{% endblock %}
```

- comment update 페이지의 경우 JS를 사용하지 않으면 흐름이 부자연스럽다.



------



## Comment 관련 추가 사항

### 댓글 개수 출력

1. {{ comments|length }}

2. {{ article.comment_set.all|length }}

3. {{ comments.count }} 

```django
<!-- articles/detail.html -->

<h4>댓글 목록</h4>
{% if comments|length %}
  <p><b>{{ comments|length }}개의 댓글이 있습니다.</b></p>
{% endif %}
```



### 댓글이 없는 경우 다른 문장 출력

- `for empty` 활용

  ```django
  <!-- articles/detail.html -->
  
  {% for comment in comments %}
    <li>
      {{ comment.content }}
      <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" class="d-inline">
        {% csrf_token %}
        <button>댓글삭제</button>
      </form>
    </li>
  {% empty %}
    <p><b>댓글이 없어요..</b></p>
  {% endfor %}
  ```

