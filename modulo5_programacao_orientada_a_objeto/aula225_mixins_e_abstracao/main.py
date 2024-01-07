# from log import LogFileMixin, LogPrintMixin
from eletronico import Smartphone

# lf = LogFileMixin()
# lf.log_error('qualquer coisa')
# lf.log_success('Que legal')


galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')

galaxy_s.ligar()
iphone.desligar()
