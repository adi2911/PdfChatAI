from queue import Queue
from flask import current_app
from threading import Thread
from app.chat.callbacks.stream import StreamingHandler

class StreamableChain:
    def stream(self, input):
        queue = Queue()
        handler = StreamingHandler(queue)

        def task(app_context):
            app_context.push()
            self(input, callbacks=[handler])

        #We need to provide thread the flask app context , as flask does not allow to run anything that it is not able to read.
        #Giving the app context to Thread make it accessible to flask.
        Thread(target=task,args=[current_app.app_context()]).start()
        
        while True:
            token = queue.get()
            if token is None:
                break
            yield token