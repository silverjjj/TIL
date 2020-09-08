def solution(tickets):
    adj = {}
    answer = []
    for a, b in tickets:
        if a not in tuple(adj.keys()):
            adj[a] = [b]
        else:
            adj[a].append(b)
    for k in adj.keys():
        adj[k].sort(reverse = True)
    s = ['ICN']
    while s:
        st = s[-1]
        if st not in adj.keys() or len(adj[st]) == 0:
            answer.append(s.pop())
        else:
            s.append(adj[st][-1])
            adj[st].pop()
    answer.reverse()
    return answer

tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
# tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
solution(tickets)