from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"



class CourseSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()

    def get_lesson_count(self, course):
        return course.сour.count()

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    сour = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ("name", "description", "picture", "сour")


