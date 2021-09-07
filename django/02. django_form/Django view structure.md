# Django view structure

> create & update view의 경우, 작성은 GET 부터 하는데,
> 왜 구조 상 조건 분기에서는 `request.method == 'POST'`를 먼저 작성할까?

## GET 먼저 분기 했을 때

### CASE 1

```python
if request.method == 'GET':
	form = ArticleForm()
	context = {
		'form': form,
	}
	return render(request, 'articles/index.html', context)
else:
	form = ArticleForm(request.POST)
	if form.is_valid():
		form.save()
		return redirect('articles:index')
	else:
		context = {
			'form': form
		}
		return render(request, 'articles/index.html', context)
```

* 불필요한 반복

### CASE 2

> 그럼 CASE 1 코드가 반복이라면 이렇게 해보면 어떨까 ?

```python
if request.method == 'GET':
	form = ArticleForm()
else:
	# 하지만 이렇게 하면 여기서 POST가 아니라 PUT, PATCH, DELETE 등
    # 다른 메서드로 요청이 와도 여기가 실행되는 문제가 생김 !
    form = ArticleForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('articles:index')
context = {
	'form': form,
}
return render(request, 'articles/index.html', context)
```

* 잠깐 그건 원래 작성하던 방식대로해도 같은 이야기 아닐까?

```python
if request.method == 'POST':
    form = ArticleForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('articles:index')
else:
    # 여기도 GET이 아닌 다른 메서드로 요청이 오면 동작 된다.
    form = ArticleForm()
context = {
	'form': form,
}
return render(request, 'articles/index.html', context)
```

* 둘 다 맞는 이야기 !
* 다만 if 문을 지나 else 문이 실행 될 때의 2가지 상황을 잘 생각해보자
  * ( else 일 경우에 집중)

```python
# 1
if request.method == 'GET':
	form = ArticleForm()
else:
    form = ArticleForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('articles:index')
```

* 여기서 else 구문은 http method가 GET이 아닐 때(POST, PUT, DELETE 등 다른 메서드) 수행

```python
# 2
if request.method == 'POST':
    form = ArticleForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('articles:index')
else:
	form = ArticleForm()
```

* 여기서 else 구문은 http method가 POST이 아닐 때(GET, PUT, DELETE 등 다른 메서드) 수행됩니
  다.



* 여기서 중요한 점은 else 구문이 수행될 때의 코드의 차이

* 첫번째 코드에서의 else는 save() 가 있는 즉, DB에 무언가 조작을 하는 코드

* 그런데 두번째 코드에서의 else는 단순히 form 인스턴스를 생성하는 코드

* 의미론적으로 생각해보자

  > "만약 사용자가 내가 고려한 조건과 다른 method로 요청했을 때
  > 단순히 form 인스턴스를 생성하는 코드를 수행하게 하실건가요,
  > 아니면 DB를 조작하는 코드를 수행하게 하실 건가요?"