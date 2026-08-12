class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        map from name to emails
        map from emails to name 
        email to name 
        map from index to name 
        index to emails
        emails to index
        iterate through the 
        '''
        index_to_email = defaultdict(list)
        index_to_name = {}
        email_to_index = defaultdict(list)

        for index, account in enumerate(accounts):
            index_to_name[index] = account[0]
            for x in range(1, len(account)):
                index_to_email[index].append(account[x])
                email_to_index[account[x]].append(index)

        res = []
        seen = set()
        seen_id = set()

        def dfs(index):
            print(index)
            for email in index_to_email[index]:
                print(email, index)
                if email not in seen:
                    seen.add(email)
                    arr.append(email)
                    for index in email_to_index[email]:
                        print(index)
                        if index not in seen_id:
                            seen_id.add(index)
                            dfs(index)
                            seen_id.remove(index)



        for key, value in index_to_email.items():
            arr = []
            print(key, value, "start")
            seen_id.add(key)
            dfs(key)
            seen_id.remove(key)
            if len(arr) == 0:
                continue
            arr.sort()
            arr.insert(0, index_to_name[key])
            res.append(arr)

        return res