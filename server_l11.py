def test_question_manager(self):
    from qa.models import Question
    from qa.models import QuestionManager
    mgr = Question.objects
    assert isinstance(mgr, QuestionManager), "Question.objects is not an QuestionManager"
    assert hasattr(mgr, 'new'), "QuestionManager has no 'new' queryset method"
    assert hasattr(mgr, 'popular'), "QuestionManager has no 'popular' queryset method"


class TestAnswer(unittest.TestCase):
    def test_answer(self):
        from qa.models import Answer
        from qa.models import Question
        try:
            text = Answer._meta.get_field('text')
        except FieldDoesNotExist:
            assert False, "text field does not exist in Answer model"
        assert isinstance(text, TextField), "text field is not TextField"
        try:
            question = Answer._meta.get_field('question')
        except FieldDoesNotExist:
            assert False, "question field does not exist in Answer model"
        assert isinstance(question, ForeignKey), "question field is not ForeignKey"
        assert question.related.parent_model == Question, "question field does not refer Question model"
        try:
            added_at = Answer._meta.get_field('added_at')
        except FieldDoesNotExist:
            assert False, "added_at field does not exist in Answer model"
        assert isinstance(text, DateField) or isinstance(added_at, DateField), "added_at field is not Date TimeField"
try:
    author = Answer._meta.get_field('author')
except FieldDoesNotExist:
    assert False, "author field does not exist in Answer model"
assert isinstance(author, ForeignKey), "author field is not ForeignKey"
assert author.related.parent_model == User, "author field does not refer User model"
user, _ = User.objects.get_or_create(username='x', password='y')
question = Question.objects.create(title='qwe', text='qwe', author=user)
try:
    answer = Answer(text='qwe', question=question, author=user)
    question.save()
except:
    assert False, "Failed to create answer model, check db connection"

suite = unittest.TestLoader().loadTestsFromTestCase(globals().get(sys.argv[1]))
unittest.TextTestRunner(verbosity=0).run(suite)