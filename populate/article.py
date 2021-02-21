from populate import base
from article.models import Article, Comment

Tiltes = ['如何像電腦科學家一樣靠杯', '10分鐘學好', '學習簡單jungle']
Comments = ['好棒棒', '不知道不想要', '牛肉炒飯', '框架很難我知道']

def populate():
    print('populating Article and Comment...', end='')
    Article.objects.all.delete()
    Comment.objects.all.delete()

    for this_tilte in Tiltes:
        article_Obj = Article()
        article_Obj.title = this_tilte
        for j in range(20):
            article_Obj.content += this_tilte + '\n'
        article_Obj.save()
        for this_comment in Comments:
            Comment.objects.create(article=article_Obj, content=this_comment)
    print('done')

if __name__ == '__main__':
    populate()