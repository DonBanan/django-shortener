# django-shortener
----------------
### Install
1. git clone https://github.com/DonBanan/django-shortener.git
2. Add to urls.py path('', include('apps.shortener.urls')),
3. In your settings define SHORTEN_LENGTH_URL = int
4. manage.py migrate shortener

### Usage
1. Create short url
    ```python
    post = Post.objects.get(id=1)
    shortener.create(post)
    ```
    return ZiyAG
2. Go to exaample.com/ZiyAG (ZiyAG - short url)
3. Redirect to exaample.com/posts/1/
    

### Conditions
All objects must have get_absolute_url()