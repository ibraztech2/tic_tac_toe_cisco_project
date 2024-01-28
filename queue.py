class QueueError(Exception):
    def __init__(self,value):
        self.value = value



class Queue:
    def __init__(self,):
        self.list = []
        list = self.list

    def put(self,value):
        self.value = value
        self.list.append(self.value)
        __value = self.value

    def get(self):
        val = self.list[0]
        del self.list[0]
        return val
    def get_list(self):
        return self.list
class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def put(self,value):
        self.value = value
        self.list.append(value)

    def get(self):
        val = self.list[0]
        del self.list[0]
        return  val

    def isempty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

queue = SuperQueue()
queue.put("man")
queue.put(False)
queue.put("i")
# raise QueueError
for i in range(5):
    try:
        if not queue.isempty():
          print(queue.get())
        else:
            print("Queue is empty ")

    except QueueError as qr:
        print(qr)