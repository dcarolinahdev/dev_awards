# Platzi awards app

---

> ***v1.1*** - This is an base project in a learning path; a poll app based on official Django documentation, it includes topics as:

*Some features*

- The views in this project are function-based and class-based views.

- It uses templates with template inheritance based on jinja 2.

- It uses different types of forms (forms.Form and form.ModelForm).

- It doesn't uses media file management.

- Model registrations on the admin site have basic customization.

- The project includes unit tests like:
    - assertEqual
    - assertIs
    - assertTrue / assertFalse
    - assertQuerysetEqual
    - assertContains

- The project uses sqlite3 (currently) as the database.

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
