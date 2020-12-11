# gcloud functions deploy buildNotificationConsumer [--source gcf] --trigger-topic cloud-builds \
#   --runtime python37 --region europe-west2 --entry-point on_message
import base64
import json

def on_message(event, context):
  """Cloud Function that inspects a Cloud Build notification PubSub message.
  
  If the notification indicates a SUCCESSful build, inspect the individual 
  steps of the build. If the steps indicate that infrastructure has been
  changed, trigger InSpec.
  """
  
  if 'attributes' not in event:
    return
  
  status = event['attributes']['status']
  if status != 'SUCCESS':
    print('Ignoring intermediate status: %s', status)
    return
  
  print("""This Function was triggered by messageId {} published at {}
  """.format(context.event_id, context.timestamp))

  if 'data' in event:
    data_str = base64.b64decode(event['data']).decode('utf-8')
    # print('Data: %s' % data_str)
    data = json.loads(data_str)
    steps = data['steps']
    for step in steps:
      print('Build step name: %s,  id: %s' % (step['name'], step['id']))
