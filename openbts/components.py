"""openbts.components
manages components in the OpenBTS application suite
"""

from openbts.core import BaseComponent

class OpenBTS(BaseComponent):
  """Manages communication to an OpenBTS instance.

  Args:
    address: tcp socket for the zmq connection
  """

  def __init__(self, address='tcp://127.0.0.1:45060'):
    super(OpenBTS, self).__init__()
    self.socket.connect(address)


class SIPAuthServe(BaseComponent):
  """Manages communication to the SIPAuthServe service.

  Args:
    address: tcp socket for the zmq connection
  """

  def __init__(self, address='tcp://127.0.0.1:45064'):
    super(SIPAuthServe, self).__init__()
    self.socket.connect(address)

  def create_subscriber(self, name, imsi, msisdn, ki=''):
    """Add a subscriber.

    If the 'ki' argument is given, OpenBTS will use full auth.  Otherwise the
    system will use cache auth.  The values of IMSI, MSISDN and ki will all
    be cast to strings before the message is sent.

    Args:
      name: name of the subscriber
      imsi: IMSI of the subscriber
      msisdn: MSISDN of the subscriber
      ki: authentication key of the subscriber
    """
    message = {
      'command': 'subscribers',
      'action': 'create',
      'fields': {
        'name': name,
        'imsi': str(imsi),
        'msisdn': str(msisdn),
        'ki': str(ki)
      }
    }
    response = self._send_and_receive(message)
    return response

  def delete_subscriber(self, imsi=None, msisdn=None):
    """Delete a subscriber by IMSI or MSISDN.

    You should pass only the IMSI or the MSISDN (not both) or a SyntaxError
    will be raised.  If neither the IMSI or the MSISDN is passed, a syntax
    error is also raised.

    Args:
      IMSI: find the subscriber to delete by IMSI
      MSISDN: find the subscriber to delete by MSISDN

    Raises:
      Syntax error if neither IMSI or MSISDN are specified, or if both are
          specified simultaneously
    """
    if imsi and msisdn:
      raise SyntaxError
    if imsi:
      match_value = {'imsi': str(imsi)}
    elif msisdn:
      match_value = {'msisdn': str(msisdn)}
    else:
      raise SyntaxError
    message = {
      'command': 'subscribers',
      'action': 'delete',
      'match': match_value
    }
    response = self._send_and_receive(message)
    return response


class SMQueue(BaseComponent):
  """Manages communication to the SMQueue service.

  Args:
    address: tcp socket for the zmq connection
  """

  def __init__(self, address='tcp://127.0.0.1:45063'):
    super(SMQueue, self).__init__()
    self.socket.connect(address)
