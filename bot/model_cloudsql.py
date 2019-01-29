# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


builtin_list = list


db = SQLAlchemy()


def init_app(app):
    # Disable track modifications, as it unnecessarily uses memory.
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    db.init_app(app)


def from_sql(row):
    """Translates a SQLAlchemy model instance into a dictionary"""
    data = row.__dict__.copy()
    data['id'] = row.id
    data['user'] = row.user 
    data['timestamp'] = row.timestamp 
    data['query_text'] = row.query_text 
    data['original_file_url'] = row.original_file_url
    data['bucket_file_url'] = row.bucket_file_url
    data['file_type'] = row.file_type
    data['json'] = row.json 
    data.pop('_sa_instance_state')
    return data


# [START model]
class Request(db.Model):
    __tablename__ = 'requests'

    id = db.Column(db.String(255), primary_key=True)
    user = db.Column(db.String(255))
    timestamp = db.Column(db.String(255))
    query_text = db.Column(db.String(4096))
    original_file_url = db.Column(db.String(255))
    bucket_file_url = db.Column(db.String(255))
    file_type = db.Column(db.String(255))
    json = db.Column(db.String(4096))

    def __repr__(self):
        return "<Request(id='%s', user=%s)" % (self.id, self.user)
# [END model]


# [START list]
def list(limit=10, cursor=None):
    cursor = int(cursor) if cursor else 0
    query = (Request.query
             .order_by(Request.timestamp)
             .limit(limit)
             .offset(cursor))
    requests = builtin_list(map(from_sql, query.all()))
    next_page = cursor + limit if len(requests) == limit else None
    return requests, next_page
# [END list]


# [START read]
def read(id):
    result = Request.query.get(id)
    if not result:
        return None
    return from_sql(result)
# [END read]


# [START create]
def create(data):
    request = Request(**data)
    db.session.add(request)
    db.session.commit()
    return from_sql(request)
# [END create]


# [START update]
def update(data, id):
    request = Request.query.get(id)
    for k, v in data.items():
        setattr(request, k, v)
    db.session.commit()
    return from_sql(request)
# [END update]


def delete(id):
    Request.query.filter_by(id=id).delete()
    db.session.commit()


def _create_database():
    """
    If this script is run directly, create all the tables necessary to run the
    application.
    """
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    init_app(app)
    with app.app_context():
        db.create_all()
    print("All tables created")


if __name__ == '__main__':
    _create_database()
