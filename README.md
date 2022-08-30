# Platzi awards app

a poll app based on official Django documentation, it includes topics as:

- Models
- Views (function base views and class based views)
- Templates (with template inheritance based on jinja 2)
- Forms (forms.Form and form.ModelForm)
- Static Files
- Media files
- Django admin
- Django authentication
- Unit test

***v1.1***

## Requirements and versions

- ***Django=3.2.9***

## How to run locally?

```
python3 manage.py createsuperuser

i.e.
    admin
    admin1234.

python3 manage.py makemigrations

python3 manage.py migrate
```
```
python3 manage.py runserver
```

## Endpoints

| route | meaning |
| --- | --- |
| /admin/ | django admin site |
| / | poll list |
| /poll/{poll_id}/detail/ | show a poll |
| /poll/{poll_id}/results/ | show results for a poll |
| /poll/{question_id}/vote/ | vote a poll |

## Notes

- Remember run test as `python3 manage.py test <app_name>`

```
python3 manage.py test polls
```

- TO-DO: tests for ResultsView.

    * test_question_not_exist
    * test_future_question
    * test_past_question

- TO-DO: tests for Questions without Choices.

---
---

# Bibliography

- [Curso Django Platzi 2022](https://platzi.com/cursos/django/)

- [My own note taking about python](https://github.com/dcarolinahdev/notes/blob/master/python.md)

- [My own note taking about django](https://github.com/dcarolinahdev/notes/blob/master/django.md)
