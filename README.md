
# Django Blog Project

## Baseline Features (Required)
- Django project/app setup, venv, migrations
- URLconf basics: path(), route converters
- Views: CBVs (ListView, DetailView, CreateView)
- Templates: DTL, inheritance, blocks, includes
- Forms: ModelForm, CSRF, validation
- Models: Post model, FK to User
- Admin: enabled, model registered
- Static/media files, settings, sessions, logging

## Good Features (🟨)
1. **Named URLs & reversing**: All URLs use `name` and `{% url %}`/`reverse()`
2. **CBVs and Generic CBVs**: Uses `ListView`, `DetailView`, `CreateView`
3. **Template inheritance/partials**: Uses `{% extends %}`, `{% block %}`, `{% include %}`
4. **FormView with success redirect and CSRF**: Post creation uses `CreateView`, ModelForm, and CSRF

## Better Features (🟧)
1. **Custom template tag/filter**: `highlight` filter in `templatetags/blog_extras.py`
2. **ModelForm mapping 1:1 to a model**: Post creation/edit uses ModelForm

## Best Features (🟥)
1. **Performance: Simple caching for list view**: `@method_decorator(cache_page(...))` on `PostListView`

---

## How to Score This Project
- All Baseline items are implemented (70%)
- 4× Good features (80%)
- 2× Better features (85%)
- 1× Best feature (90%)
- Remaining 10%: Synthesis, code quality, and documentation

---

## Improvements & Suggestions
- Add more tests in `blog/tests.py` (e.g., for views, forms)
- Add user registration and profile pages
- Add more custom template tags/filters
- Add image/file upload to posts (MEDIA_URL/ROOT ready)
- Add deployment settings (DEBUG=False, ALLOWED_HOSTS, etc.)
- Add health check or logging middleware for observability
- Add static/media file collection for production (`collectstatic`)
- Add more advanced permissions (e.g., only author can edit/delete)

---

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Run migrations: `python manage.py migrate`
3. Create superuser: `python manage.py createsuperuser`
4. Run server: `python manage.py runserver`

---

# Eric Ocansey
