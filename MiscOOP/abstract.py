from abc import ABC, abstractmethod

class Handler(ABC): # abstract handler class
    def __init__(self, succesor):
        self._successor = succesor
    
    def handle(self, request):
        handled = self._handle(request) # if handled stop here

        if not handled:
            self._successor.handle(request)
    
    # all subclasses are now forced to implement this
    @abstractmethod
    def _handle(self, request):
        pass

class ConcreteHandler1(Handler):

    def _handle(self, request):
        if 0 < request <=10:
            print(f"Reqeust {request} ,handled in handler1")
            return True

class DefaultHandler(Handler):

    def _handle(self, request):
        print("End of chain. No handler for ", request)
        return True


class Client:
    def __init__(self):
        # Creaete handlers and use then in a sequence you want
        self.handler = ConcreteHandler1(DefaultHandler(None))
    
    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)

c = Client()

requests = [2,5,30]

c.delegate(requests)
