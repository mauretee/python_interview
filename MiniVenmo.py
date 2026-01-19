

class User:
    def __init__(self, user_id, initial_balance=0):
        self.user_id = user_id
        self.balance = initial_balance
        self.credit_card = None
        self.activity = []
        self.friends = set()
    
    def link_credit_card(self, card_number):
        self.credit_card = card_number

    def pay(self, amount, user, description=""):
        if amount <= self.balance:
            self.balance -= amount
            user.balance += amount
            self.activity.append(f"{self.user_id} paid {user.user_id} ${amount} for ${description}")
        elif amount > self.balance and self.credit_card is None:
            raise ValueError("Insufficient funds.")
        else:
            credit_card_value = amount - self.balance
            self.credit_card.charge(credit_card_value)
            self.activity.append(f"{self.user_id} paid {user.user_id} ${amount} for ${description}")
            self.balance -= amount
            user.balance += amount
 

    def retrieve_activity(self):
        return self.activity
    
    def add_friend(self, user):
        if user.user_id in self.friends:
            raise ValueError("User is already a friend.")
        else:
            self.activity.append(f"{self.user_id} added {user.user_id} as a friend")
            self.friends.add(user.user_id)


class MiniVenmo:
    def __init__(self):
        self.users = []

    def create_user(self,user: User):
        self.users.append(user)
    

    def render_feed(self):
        # Placeholder for feed rendering logic
        for user in self.users:
            for activity in user.retrieve_activity():
                print(activity)

if __name__ == "__main__":
    # 1
    alice = User("alice", 100)

    mv = MiniVenmo()
    mv.create_user(alice)

    # 2
    bob = User("bob", 0)
    alice.pay(50, bob, "cake")
    assert alice.balance == 50
    assert bob.balance == 50

    # 3
    mv.render_feed()

    # 4
    alice = User("alice", 20)
    bob = User("bob", 0)
    alice.add_friend(bob)

    mv.render_feed()




