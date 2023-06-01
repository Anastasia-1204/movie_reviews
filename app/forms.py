from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed


class ReviewForm(FlaskForm):
    name = StringField('Ваше имя',
                       validators=[DataRequired(message='Поле не должно быть пустым')])
    text = TextAreaField('Текст отзыва',
                         validators=[DataRequired(message='Поле не должно быть пустым')])
    score = SelectField('Оценка',
                        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    submit = SubmitField('Добавить отзыв')


class MovieForm(FlaskForm):
    title = StringField('Название',
                        validators=[DataRequired(message='Поле не должно быть пустым')])
    description = TextAreaField('Описание',
                                validators=[DataRequired(message='Поле не должно быть пустым')])
    image = FileField('Изображение',
                      validators=[FileRequired(message='Поле не должно быть пустым'),
                                  FileAllowed(['jpg', 'jpeg', 'png'], message='Неверный формат файла')])
    submit = SubmitField('Добавить фильм')
