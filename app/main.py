from flask import Flask, render_template, redirect, url_for, request, flash
from flask_admin import Admin
from sqlalchemy import select
from flask_login import login_user, logout_user, login_required

from app.settings import Config
from app.models import Teacher, News
from app.admin import login_manager, SecureAdminIndexView, AdminUser, NewsModelView, TeacherModelView
from app.database import session_local

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = '170dcfee-6d7c-416f-a2b5-25788465f54a'
app.config.from_object(Config)

login_manager.init_app(app)
admin = Admin(app, name='Администрирование', index_view=SecureAdminIndexView(), template_mode='bootstrap3')
admin.add_view(TeacherModelView(Teacher, session_local(), name='Преподаватели'))
admin.add_view(NewsModelView(News, session_local(), name='Новости'))

@app.route('/')
def home():
	return redirect(url_for('info'))


@app.route('/info')
def info():
	return render_template('info.html')


@app.route('/teachers')
def teachers():
	with session_local() as session:
		query = select(Teacher)
		result = session.execute(query)
		teachers_list = result.scalars().all()
		return render_template('teachers.html', teachers=teachers_list)


@app.route('/news')
def news():
	with session_local() as session:
		query = select(News)
		result = session.execute(query)
		news_list = result.scalars().all()
		return render_template('news.html', news=news_list)


@app.route('/contacts')
def contacts():
	return render_template('contacts.html')


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')

		# Проверка логина/пароля (замените на свою логику)
		if username == 'admin' and password == 'password':
			user = AdminUser(1)
			login_user(user)
			return redirect(url_for('admin.index'))
		else:
			flash('Неверные учетные данные', 'error')

	return render_template('admin/login.html')


@app.route('/admin/logout')
@login_required
def admin_logout():
	logout_user()
	return redirect(url_for('admin_login'))


if __name__ == '__main__':
	app.run(debug=True, port=5000)
