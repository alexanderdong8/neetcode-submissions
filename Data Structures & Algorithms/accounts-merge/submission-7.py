class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        index to emails

        emails to index

        if i see an email ive seen before i map that index to the other index 
        1, 3
        3, 5
        connections map
        '''

        index_to_emails = defaultdict(list)
        email_to_index = {}
        index_to_name = {}
        connections = defaultdict(list)

        for index, account in enumerate(accounts):
            index_to_name[index] = account[0]
            for email in account[1:]:
                index_to_emails[index].append(email)
                if email in email_to_index:
                    old_index = email_to_index[email]
                    connections[old_index].append(index)
                    connections[index].append(old_index)
                else:
                    email_to_index[email] = index

        print(connections)
        def dfs(index):
            
            for email in index_to_emails[index]:
                arr.add(email)

            for new_index in connections[index]:
                if new_index not in seen_index:
                    seen_index.add(new_index)
                    dfs(new_index)

        seen_index = set()
        res = []
        for index in range(len(accounts)):
            arr = set()

            if index not in seen_index:
                seen_index.add(index)
                dfs(index)
                arr = list(arr)
                arr.sort()
                name = index_to_name[index]
                res.append([name, *arr])

        return res



                



