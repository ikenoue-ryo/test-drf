from rest_framework import serializers
from .models import Article, Writer
from rest_framework.serializers import SerializerMethodField


class WriterSerializer(serializers.ModelSerializer):
    articles = SerializerMethodField()

    class Meta:
        model = Writer
        fields = ('id', 'name', 'articles')

    def get_articles(self, obj):
        try:
            article_abstruct_contents = ArticleSerializer(Article.objects.all().filter(writer = Writer.objects.get(id=obj.id)), many=True).data
            print('1', article_abstruct_contents)
            return article_abstruct_contents
        except:
            article_abstruct_contents = None
            print('2', article_abstruct_contents)

            return article_abstruct_contents

class ArticleSerializer(serializers.ModelSerializer):
    writer = WriterSerializer()

    class Meta:
        model = Article
        fields = ('__all__')
    
    def create(self, validated_data):
        writer = Writer(**validated_data.pop('writer'))
        writer.save()
        return super(ArticleSerializer, self).create(dict(validated_data, **{'writer': writer}))