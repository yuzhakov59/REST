from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson, Course
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.course = Course.objects.create(name="1")
        self.lesson = Lesson.objects.create(name="химия", сourse=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrive(self):
        url = reverse("materials:lesson-retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), self.lesson.name
        )

    def test_lesson_create(self):
        url = reverse("materials:lesson-create")
        data = {
            "name": "английский",
            "video_url": "http://www.youtube.com/watch?v=xh4AyiP6YYs",
            "сourse": 1,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("materials:lesson-update", args=(self.lesson.pk,))
        data = {
            "name": "английский",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "английский")

    def test_lesson_delete(self):
        url = reverse("materials:lesson-destroy", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("materials:lesson-list")
        response = self.client.get(url)
        data = response.json()
        rezult ={
    "count": 1,
    "next": None,
    "previous": None,
    "results": [
        {
            "id": self.lesson.pk,
            "name": "химия",
            "description": None,
            "picture": None,
            "video_url": None,
            "сourse": 3,
            "owner": 3
        }]}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, rezult)


