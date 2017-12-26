from http import HTTPStatus

import tornado.web
import tornado.gen
import utils
import forms


class LoginRequiredMixin(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get_current_user(self):
        user_id = self.get_secure_cookie(
            self.application.settings['user_cookie_key']
        )
        if not user_id:
            self.send_error(
                status_code=401,
                reason='Not authenticated user'
            )
            return None
        user = yield self.application.settings['db'].users.find_one({
            'username': user_id.decode()
        })
        return user

    @tornado.gen.coroutine
    def check_authenticated(self):
        user = yield self.get_current_user()
        if not user:
            self.redirect(self.reverse_url('login'))


class IndexHandler(LoginRequiredMixin):
    """
    Dashboard index page.
    """

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        cursor = self.settings['db'].categories.find({})
        categories = []
        while (yield cursor.fetch_next):
            category = cursor.next_object()
            categories.append(category)
        self.render('index.html', categories=categories)


class ReportHandler(LoginRequiredMixin):
    """
    Report handler.
    Would be used for report to csv.
    """

    @tornado.gen.coroutine
    def get(self, pk: str):
        yield self.check_authenticated()
        # self.write('report')


class LoginHandler(tornado.web.RequestHandler):
    """
    Login handler.
    Would be used for report to csv.
    """

    @tornado.gen.coroutine
    def get(self):
        form = forms.LoginForm()
        self.render('login.html', form=form)

    @tornado.gen.coroutine
    def post(self):
        form = forms.LoginForm(data={
            'username': self.get_body_argument('username', None),
            'password': self.get_body_argument('password', None)
        })
        if not form.validate():
            self.send_error(
                status_code=HTTPStatus.UNAUTHORIZED
            )
            return
        username = form.data.get('username')
        password = form.data.get('password')

        user = yield self.settings['db'].users.find_one({
            'username': username
        })
        if user is None:
            self.send_error(
                status_code=HTTPStatus.UNAUTHORIZED
            )
            return

        if not (
        yield utils.check_password(password, user['password'].decode())):
            self.send_error(status_code=HTTPStatus.UNAUTHORIZED)
            return

        self.set_secure_cookie(self.settings['user_cookie_key'],
                               user['username'])
        self.redirect(self.reverse_url('index'))


class LogoutHandler(LoginRequiredMixin):
    """
    Login handler.
    Would be used for report to csv.
    """

    def get(self):
        self.clear_cookie(self.settings['user_cookie_key'])
        self.redirect(self.reverse_url('login'))
