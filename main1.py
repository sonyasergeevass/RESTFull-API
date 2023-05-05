from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__) #обращаемся к стандартному классу Flask и передаем ему туда наш рабочий файл(created our app)
api = Api(app) #объект на основе класса Api
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database1.db'
db = SQLAlchemy(app)


class AccountModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"AccountModel(firstName={self.firstName}, lastName={self.lastName}, email={self.email}, password={self.password})"

# with app.app_context():
#     db.create_all()
#     db.session.execute(text('ALTER TABLE account_model ADD COLUMN password VARCHAR(100)'))
#     db.session.commit()

account_put_args = reqparse.RequestParser()
account_put_args.add_argument("firstName", type=str, help="Name of the firstName is required!", required=True)
account_put_args.add_argument("lastName", type=str, help="Name of the lastName is required!", required=True)
account_put_args.add_argument("email", type=str, help="Name of the email is required!", required=True)
account_put_args.add_argument("password", type=str, help="Name of the password is required!", required=True)

resource_fields = {
    'id': fields.Integer,
    'firstName': fields.String,
    'lastName': fields.String,
    'email': fields.String,
}

class Account(Resource):
    @marshal_with(resource_fields)
    def get(self, accountid):
        result = AccountModel.query.filter_by(id=accountid).first()
        if not result:
            abort(404, message='Could not find video with that id...')
        # elif accountid <= 0 and accountid == None:
        #     abort(400, message='Syntax error')
        # # elif accountid <= 0 and accountid == None:
        # #     abort(401, message='Incorrect authorization data')
        # elif result:
        #     abort(200, message='The request was successfully completed')
        return result, 200

    @marshal_with(resource_fields)
    def gett(self, from1, size, firstname=None, lastname=None, emaill=None):
        result = AccountModel.query.filter(AccountModel)

    @marshal_with(resource_fields)
    def put(self, accountid):
        args = account_put_args.parse_args()
        result = AccountModel.query.filter_by(id=accountid).first()
        if result:
            abort(409, message='Video id has taken...')
        account = AccountModel(id=accountid, firstName=args['firstName'], lastName=args['lastName'],
                               email=args['email'], password=args['password'])
        db.session.add(account)  # add an instance of VideoModel to database
        db.session.commit()  # commit any changes(фиксирует любые изменения) in db and make it permonent(и делает их постоянными)
        return account, 201  # 201-запрос выполнен успешно, ресурс был создан


    def delete(self, accountid):
        result = AccountModel.query.filter_by(id=accountid).first()
        if result:
            db.session.delete(result)
            db.session.commit()
            abort(200, message='The request was successfully completed, video has been deleted')
        else:
            abort(404, message='Could not find the video with that id')

api.add_resource(Account, "/api/accounts/<int:accountid>") #добавляем ресурс на обработку
api.init_app(app)#инициализируем приложение

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="127.0.0.1") #любые ошибку будут выводиться в терминале
