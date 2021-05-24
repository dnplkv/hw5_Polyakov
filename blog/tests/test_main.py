from django.apps import apps
from django.test import TestCase
from django.urls import reverse
from main.apps import MainConfig
from main.models import Contacts, Post


class MainConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(MainConfig.name, 'main')
        self.assertEqual(apps.get_app_config('main').name, 'main')


def test_home_page(client):
    response = client.get(reverse('home_page'))
    assert response.status_code == 200


def test_about(client):
    response = client.get(reverse('about'))
    assert response.status_code == 200


def test_posts_all(client):
    response = client.get(reverse('posts_all'))
    assert response.status_code == 200


def test_posts_list(client):
    response = client.get(reverse('posts_list'))
    assert response.status_code == 200


def test_posts_create(client):
    response = client.get(reverse('posts_create'))
    assert response.status_code == 200


def test_csv(client):
    response = client.get(reverse('download_posts_xlsx'))
    assert response.status_code == 200


def test_json(client):
    response = client.get(reverse('json_data'))
    assert response.status_code == 200


def test_api_author(client):
    response = client.get(reverse('api_authors_new'))
    assert response.status_code == 200


def test_api_authors_all(client):
    response = client.get(reverse('api_authors_all'))
    assert response.status_code == 200


def test_api_subscribe(client):
    response = client.get(reverse('api_subscribers_all'))
    assert response.status_code == 200


def test_email_all(client):
    response = client.get(reverse('email_to_all_subs'))
    assert response.status_code == 302


def test_api_subs_all(client):
    response = client.get(reverse('api_subscribers_all'))
    assert response.status_code == 200


def test_api_categories_all(client):
    response = client.get(reverse('categories_all'))
    assert response.status_code == 200


def test_author_delete(client):
    response = client.get(reverse('authors_all'))
    assert response.status_code == 200


def test_subs_all(client):
    response = client.get(reverse('subscribers_all'))
    assert response.status_code == 200


def test_authors_new(client):
    response = client.get(reverse('authors_new'))
    assert response.status_code == 302


def test_contact_us_post_empty_form(client):
    response = client.post(reverse('contact-us-create'))
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email_to': ['Обязательное поле.'],
        'topic': ['Обязательное поле.'],
        'text': ['Обязательное поле.']
    }


def test_contact_us_post_wrong_email(client):
    response = client.post(reverse('contact-us-create'), data={
        'email_to': 'not-valid-email_to'
    })
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email_to': ['Введите правильный адрес электронной почты.'],
        'topic': ['Обязательное поле.'],
        'text': ['Обязательное поле.']
    }


def test_contact_us_correct_form(client):
    response = client.post(reverse('contact-us-create'), data={
        'email_to': 'test@mail.com',
        'topic': 'subj',
        'text': 'msg',
    })
    assert response.status_code == 302


# def test_contact_us_correct_form_check_count(client):
#     count_before = Contacts.objects.count()
#     response = client.post(reverse('contact-us-create'), data={
#         'email_to': 'test@mail.com',
#         'topic': 'subj',
#         'text': 'msg',
#     })
#     assert response.status_code == 302
#     assert Contacts.objects.count() == count_before + 1

def test_contact_us_correct_form_check_count(client, fake_fixt):
    count_before = Contacts.objects.count()
    response = client.post(reverse('contact-us-create'), data={
        'email_to': fake_fixt.email(),
        'topic': fake_fixt.word(),
        'text': fake_fixt.word(),
    })
    assert response.status_code == 302
    assert Contacts.objects.count() == count_before + 1


def test_acc(acc_fixt):
    print(acc_fixt)


def test_sub_correct_form(client):
    response = client.post(reverse('subscribers_new'), data={
        'email_to': 'test@mail.com',
        'author_id': 'subj',
    })
    assert response.status_code == 200


def test_post_correct_form(client):
    response = client.post(reverse('posts_create'), data={
        'title': 'test@mail.com',
        'description': 'subj',
        'content': 'subj',
    })
    assert response.status_code == 302


def test_book_correct_form(client):
    response = client.post(reverse('books_all'), data={
        'title': 'test@mail.com',
        'author': 'subj',
        'category': 'subj',
    })
    assert response.status_code == 200


def test_post_correct_form_check_count(client, fake_fixt):
    count_before = Post.objects.count()
    response = client.post(reverse('posts_create'), data={
        'title': fake_fixt.word(),
        'description': fake_fixt.word(),
        'content': fake_fixt.word(),
    })
    assert response.status_code == 302
    assert Post.objects.count() == count_before + 1
