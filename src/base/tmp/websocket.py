import logging
from websocket_server import WebsocketServer

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(' %(module)s -  %(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Callback functions

def new_client(client, server):
  logger.info('New client {}:{} has joined.'.format(client['address'][0], client['address'][1]))

def client_left(client, server):
  logger.info('Client {}:{} has left.'.format(client['address'][0], client['address'][1]))

def message_received(client, server, message):
  logger.info('Message "{}" has been received from {}:{}'.format(message, client['address'][0], client['address'][1]))
  reply_message = 'Hi! ' + message
  server.send_message(client, reply_message)
  logger.info('Message "{}" has been sent to {}:{}'.format(reply_message, client['address'][0], client['address'][1]))

# Main
if __name__ == "__main__":
  server = WebsocketServer(port=12345, host='127.0.0.1', loglevel=logging.INFO)
  server.set_fn_new_client(new_client)
  server.set_fn_client_left(client_left)
  server.set_fn_message_received(message_received)
  server.run_forever()

