class Solution {
public:
	int uniqueMorseRepresentations(vector<string>& words) {
		string arr[26] = { ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.." };

		set<string> ans;


		for (int i = 0; i < words.size(); i++) {

			string temp = "";

			for (int j = 0; j < words[i].length(); j++) {
				temp += arr[words[i][j] - 'a'];
			}

			ans.insert(temp);

		}

		return ans.size();

	}
};