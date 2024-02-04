from collections import deque

printter_queue = deque()
printter_queue.append("TaylorSwiftTickets.pdf")
printter_queue.append("MarketingNotes.docx")

document = printter_queue.popleft()
print(f'Printing {document}')