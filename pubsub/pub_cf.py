from google.cloud import pubsub_v1

import os
import requests

def pub_cf(request):

    if list(request.args.keys()):
        parameters = request.args
    else:
        parameters = request.get_json()

    url_to_file = parameters.get('url_to_file', None)

    if url_to_file:
        content = requests.get(url_to_file).content.decode()

        publisher = pubsub_v1.PublisherClient()
        topic_name = 'projects/{project_id}/topics/{topic}'.format(
            project_id=os.getenv('PROJECT_ID'),
            topic=os.getenv('TOPIC')
        )

        for line in content.split('\n'):
            publisher.publish(topic_name, line.encode('utf-8'))

        return 'Complete'
    return 'Failed'