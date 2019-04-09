# coding: utf-8 
import logging 
from flask_spyne import Spyne
from spyne.protocol.soap import Soap11
from spyne.model.primitive import Unicode, Integer, String
from spyne.model.complex import Iterable, Array
from spyne import srpc, Application, ServiceBase
 
from ..models import User 
class SomeSoapService(ServiceBase):
    __service_url_path__ = '/soap/someservice'
    __target_namespace__ = 'custom_namespace'
    __in_protocol__ = Soap11(validator='lxml')
    __out_protocol__ = Soap11()
    __wsse_conf__ = {
        'username': 'myusername',
        'password': 'mypassword'  # never store passwords directly in sources!
    }

    @srpc(Unicode, Integer, _returns=Iterable(Unicode))
    def echo(str, cnt):
        print(str, cnt)
        for i in range(cnt):
            yield str

    @srpc(Unicode, _returns=Unicode)
    def users(str):  
        user = User.objects.get(username=str) 
        return u''+user.username 
        #yield user.username
        #yield user.password


def create_soap_app(flask_app):
    """Creates SOAP services application and distribute Flask config into
    user can defined context for each method call.
    """
    application = Application(
        [SomeSoapService], 'spyne.examples.flask',
        # The input protocol is set as HttpRpc to make our service easy to call.
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11(),
    )

    return application