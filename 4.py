import random

tickets = set()
while len(tickets) < 100:
    ticket = str(random.randomchoice())
    tickets.add(ticket)

lucky_tickets = random.sample(tickets, 2)

print(lucky_tickets)
