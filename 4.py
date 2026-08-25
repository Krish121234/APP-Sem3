class Blog:
    def __init__(self, name):
        self.name = name
        self._subscribers = []
        self._latest_post = None

    def subscribe(self, subscriber):
        if subscriber not in self._subscribers:
            self.subscribers.append(subscriber)
            print(f"✓ {subscriber.email} subscribed to {self.name}")

    def unsubscribe(self, subscriber):
        if subscriber in self._subscribers:
            self.subscribers.remove(subscriber)
            print(f"✗ {subscriber.email} unsubscriber to {self.name}")

    def notify_all(self):
        print(f"\nNotifying {len(self._subscribers)} subscribers")
        for subscriber in self._subscribers:
            subscriber.recieve_notification(self.name, self._latest_post)