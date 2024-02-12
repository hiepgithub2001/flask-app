class MQMeta:
    _instance = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]  

class MQ(metaclass=MQMeta):
    def sending(topic, body):
        return
        
    def receving():
        return    