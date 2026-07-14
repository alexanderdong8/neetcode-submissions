#include <queue>
#include <functional>
#include <vector>
class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        vector<vector<int>> task_list;
        for (int x = 0; x < tasks.size(); x++) {
            task_list.push_back(vector<int>{tasks[x][0], tasks[x][1], x});
        }
        sort(task_list.begin(), task_list.end());

        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> minHeap;
        vector<int> res;
        int x = 0;
        int curr_time = 0;
        for (auto& v : task_list){
            cout << v[0] << v[1] << v[2] << endl;
        }
        while (x < task_list.size()) {
            if (minHeap.empty()) {
                res.push_back(task_list[x][2]);
                curr_time = task_list[x][0] + task_list[x][1];
                x += 1;

                while (x < task_list.size() && curr_time >= task_list[x][0]) {
                    int index = task_list[x][2], start = task_list[x][0], time = task_list[x][1];
                    minHeap.push(vector<int>{time, index, start});
                    x += 1;
                }
            }
            cout << "ran" << endl;
            while (!minHeap.empty()) {
                vector<int> vec = minHeap.top();
                minHeap.pop();
                int time = vec[0], index = vec[1], start = vec[2];
                curr_time += time;
                res.push_back(index);
                while (x < task_list.size() and curr_time >= task_list[x][0]) {
                    int index = task_list[x][2], start = task_list[x][0], time = task_list[x][1];
                    minHeap.push(vector<int>{time, index, start});
                    x += 1;
                }
                
            }
        }
        return res;
    }
};