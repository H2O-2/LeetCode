#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> currentNums;
        vector<vector<int>> sol;

        combinationSumUtil(sol, currentNums, candidates, 0, target);

        return sol;
    }
private:
    void combinationSumUtil(vector<vector<int>>& sol, vector<int>& currentNums, const vector<int>& candidates, int current, int target) {
        if (current == target) {
            sol.emplace_back(currentNums);
            return;
        }

        if (current > target) {
            return;
        }

        for (int i = 0; i < candidates.size(); ++i) {
            int candidate = candidates[i];

            if (candidate > target) break;

            currentNums.push_back(candidate);

            combinationSumUtil(sol, currentNums, vector<int>(candidates.begin() + i, candidates.end()), current + candidate, target);

            currentNums.pop_back();
        }
    }
};

int main() {
    Solution s = Solution();
    vector<int> candidates = {2,3,5};
    vector<vector<int>> sol = s.combinationSum(candidates, 8);

    return 0;
}
