# test_observer.py

import unittest
from observer import ConcretePublisher, ConcreteSubscriber

class TestObserverPattern(unittest.TestCase):
    def setUp(self):
        self.publisher = ConcretePublisher()
        self.subscriber1 = ConcreteSubscriber("Subscriber 1")
        self.subscriber2 = ConcreteSubscriber("Subscriber 2")

    def test_add_subscriber(self):
        self.publisher.add_subscriber(self.subscriber1)
        self.assertIn(self.subscriber1, self.publisher.subscribers)

    def test_remove_subscriber(self):
        self.publisher.add_subscriber(self.subscriber1)
        self.publisher.remove_subscriber(self.subscriber1)
        self.assertNotIn(self.subscriber1, self.publisher.subscribers)

    def test_notify_subscribers(self):
        self.publisher.add_subscriber(self.subscriber1)
        self.publisher.add_subscriber(self.subscriber2)
        self.publisher.state = "Test Message"
        self.assertEqual(self.subscriber1.state, "Test Message")
        self.assertEqual(self.subscriber2.state, "Test Message")

if __name__ == "__main__":
    unittest.main()
