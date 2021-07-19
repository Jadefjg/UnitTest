import pytest

from src.blog.commands import CreateArticleCommand,AlreadyExists

from src.blog.models import Article

def test_create_article():
    """
        GIVEN CreateArticleCommand with a valid properties author,title and context
        WHEN the execute method is called
        THEN a new Aticle must exist in the database with the same atttibute
    """

    cmd = CreateArticleCommand(
        author = 'john@doe.com',
        title = 'New Article',
        content = 'Super awesome article'
    )

    article = cmd.excute()

    db_article = Article.get_by_id(article.id)

    assert db_article.id == article.id
    assert db_article.author == article.author
    assert db_article.title == article.title
    assert db_article.content == article.content


    def test_create_article_with_mock(monkeypatch):
        """
           GIVEN CreateArticleCommand with valid properties author, title and content
           WHEN the execute method is called
           THEN a new Article must exist in the database with same attributes
        """
        article = Article(
            author='john@doe.com',
            title='New Article',
            content='Super awesome article'
        )
        monkeypatch.setattr(
            Article,
            'save',
            lambda self: article
        )
        cmd = CreateArticleCommand(
            author='john@doe.com',
            title='New Article',
            content='Super awesome article'
        )

        db_article = cmd.execute()

        assert db_article.id == article.id
        assert db_article.author == article.author
        assert db_article.title == article.title
        assert db_article.content == article.content


    def test_create_article_already_exists():
        """
        GIVEN CreateArticleCommand with a title of some article in database
        WHEN the execute method is called
        THEN the AlreadyExists exception must be raised
        """

        Article(
            author='jane@doe.com',
            title='New Article',
            content='Super extra awesome article'
        ).save()

        cmd = CreateArticleCommand(
            author='john@doe.com',
            title='New Article',
            content='Super awesome article'
        )

        with pytest.raises(AlreadyExists):
            cmd.execute()
