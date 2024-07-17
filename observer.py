# observer.py

# Define the Publisher class
class Publisher:
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def notify_subscribers(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

# Define the Subscriber class
class Subscriber:
    def update(self, message):
        pass

# Implement Concrete Classes for Publisher and Subscriber
class ConcretePublisher(Publisher):
    def __init__(self):
        super().__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify_subscribers(value)

class ConcreteSubscriber(Subscriber):
    def __init__(self, name):
        self.name = name
        self.state = None

    def update(self, message):
        self.state = message
        print(f"{self.name} received message: {message}")
#ohadhklaklhakla
# Example usage
if __name__ == "__main__":
    publisher = ConcretePublisher()

    subscriber1 = ConcreteSubscriber("Subscriber 1")
    subscriber2 = ConcreteSubscriber("Subscriber 2")

    publisher.add_subscriber(subscriber1)
    publisher.add_subscriber(subscriber2)

    publisher.state = "New State"

    publisher.remove_subscriber(subscriber2)

    publisher.state = "Another State"
