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

from __future__ import absolute_import

import datetime
import re
import requests

from flask import current_app
from google.cloud import storage
from werkzeug import secure_filename
from werkzeug.exceptions import BadRequest


def _get_storage_client():
    return storage.Client(
        project=current_app.config['PROJECT_ID'])


def _check_extension(filename, allowed_extensions):
    if ('.' not in filename or
            filename.split('.').pop().lower() not in allowed_extensions):
        raise BadRequest(
            "{0} has an invalid name or extension".format(filename))


def _safe_filename(filename):
    """
    Generates a safe filename that is unlikely to collide with existing objects
    in Google Cloud Storage.

    ``filename.ext`` is transformed into ``filename-YYYY-MM-DD-HHMMSS.ext``
    """
    filename = secure_filename(filename)
    date = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H%M%S")
    basename, extension = filename.rsplit('.', 1)
    return "{0}-{1}.{2}".format(basename, date, extension)


def upload_from_url(url):
    """
    Upload the user-uploaded file to Google Cloud Storage and retrieve its
    publicly-accessible URL.
    """
    filename = _safe_filename(_get_filename_from_url(url))

    r = requests.get(url, allow_redirects=True)

    public_url = _upload_file(
        r.content,
        filename,
        'application/octet-stream'
    )

    current_app.logger.info(
        "Uploaded file %s as %s.", filename, public_url)

    return public_url


def _get_filename_from_url(url):
    try:
        filename = re.search('/([\w.-]+)\?', url).group(1)
    except Exception as e:
        current_app.logger.info('ERROR: %s', e)
        filename = 'no-name.unk'
    return filename


def upload_file(file):
    """
    Upload the user-uploaded file to Google Cloud Storage and retrieve its
    publicly-accessible URL.
    """
    if not file:
        return None

    public_url = _upload_file(
        file.read(),
        file.filename,
        file.content_type
    )

    current_app.logger.info(
        "Uploaded file %s as %s.", file.filename, public_url)

    return public_url


def _upload_file(file_stream, filename, content_type):
    """
    Uploads a file to a given Cloud Storage bucket and returns the public url
    to the new object.
    """
    # _check_extension(filename, current_app.config['ALLOWED_EXTENSIONS'])
    filename = _safe_filename(filename)

    client = _get_storage_client()
    bucket = client.bucket(current_app.config['CLOUD_STORAGE_BUCKET'])
    blob = bucket.blob(filename)

    blob.upload_from_string(
        file_stream,
        content_type=content_type)

    public_url = 'gs://{bucket}/{filename}'.format(bucket=current_app.config['CLOUD_STORAGE_BUCKET'],
                                                   filename=filename)
    return public_url
