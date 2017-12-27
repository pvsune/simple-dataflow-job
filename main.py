from __future__ import absolute_import
import logging

from bottle import get, run, request

import pipelines.wordcap as wordcap


logger = logging.getLogger(__name__)


@get('/pipeline')
def index():
    if request.get_header('x-pipeline-cron', None) == 'True':
        return 'You are not allowed to do this!'

    input_ = 'gs://test-pez-ai/mydataflow_2017-12-19T08:55:00.000Z-2017-12-19T09:00:00.000Z-pane-0-last-00-of-01'
    output = 'gs://test-pez-ai/mydataflow'
    project = 'panoptez'
    tmp_dir = 'gs://test-pez-ai/tmp/'

    try:
        wordcap.run(input_, output, project, tmp_dir)
        return 'DataFlow job started.'
    except Exception:
        logger.exception('Something went wrong.')
        return 'Something went wrong while starting the job.'

run(host='0.0.0.0', port=8080)
