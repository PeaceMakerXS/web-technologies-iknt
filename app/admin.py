from flask import redirect, url_for
from flask_login import UserMixin, LoginManager, current_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

login_manager = LoginManager()
login_manager.login_view = 'admin_login'


class AdminUser(UserMixin):
	def __init__(self, _id):
		self.id = _id


@login_manager.user_loader
def load_user(user_id):
	return AdminUser(user_id)


class SecureAdminIndexView(AdminIndexView):
	def is_accessible(self):
		return current_user.is_authenticated

	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for('admin_login'))


class SecureModelView(ModelView):
	def is_accessible(self):
		return current_user.is_authenticated

	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for('admin_login'))


class TeacherModelView(SecureModelView):
	column_labels = dict(title='ФИО', description_teacher='Описание', img='Аватар')


class NewsModelView(SecureModelView):
	column_labels = dict(title='Заголовок', description_new='Содержание', img='Изображение')
