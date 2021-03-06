import logging
from abc import abstractmethod, ABCMeta
from cbpi.api.extension import CBPiExtension




class CBPiSensor(metaclass=ABCMeta):

    def __init__(self, cbpi, id, props):
        self.cbpi = cbpi
        self.id = id
        self.props = props
        self.logger = logging.getLogger(__file__)
        self.data_logger = None
        self.state = False
        self.running = False

    def init(self):
        pass

    def log_data(self, value):
        self.cbpi.log.log_data(self.id, value)

    @abstractmethod
    async def run(self):
        self.logger.warning("Sensor Init not implemented")

    def get_state(self):
        pass

    def get_value(self):
        pass

    def get_unit(self):
        pass

    def push_update(self, value):
        try:
            self.cbpi.ws.send(dict(topic="sensorstate", id=self.id, value=value))
        except:
            logging.error("Faild to push sensor update")

    async def start(self):
        self.running = True

    async def stop(self):
        
        self.running = False