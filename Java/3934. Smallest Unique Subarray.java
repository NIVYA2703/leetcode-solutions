
import java.util.*;

class Solution {
    public int smallestUniqueSubarray(int[] nums) {
        int n = nums.length;

        long[] keys = new long[n];
        int[] rank = nums.clone();
        int[] newRank = new int[n];
        int[] sa = new int[n];

        int k = 1;

        while (true) {
            for (int i = 0; i < n; i++) {
                int second = (i + k < n) ? rank[i + k] : -1;

                keys[i] = ((long)(rank[i] + 1) << 40)
                        | ((long)(second + 1) << 20)
                        | i;
            }

            Arrays.sort(keys);

            for (int i = 0; i < n; i++) {
                sa[i] = (int)(keys[i] & ((1 << 20) - 1));
            }

            newRank[sa[0]] = 0;

            for (int i = 1; i < n; i++) {
                int a = sa[i - 1];
                int b = sa[i];

                int a1 = rank[a];
                int b1 = rank[b];

                int a2 = (a + k < n) ? rank[a + k] : -1;
                int b2 = (b + k < n) ? rank[b + k] : -1;

                newRank[b] = newRank[a];

                if (a1 != b1 || a2 != b2) {
                    newRank[b]++;
                }
            }

            int[] temp = rank;
            rank = newRank;
            newRank = temp;

            if (rank[sa[n - 1]] == n - 1 || k >= n)
                break;

            k *= 2;
        }

        int[] pos = new int[n];
        int[] lcp = new int[n];

        for (int i = 0; i < n; i++) {
            pos[sa[i]] = i;
        }

        int h = 0;

        for (int i = 0; i < n; i++) {
            int r = pos[i];

            if (r == 0) {
                h = 0;
                continue;
            }

            int j = sa[r - 1];

            while (i + h < n && j + h < n &&
                   nums[i + h] == nums[j + h]) {
                h++;
            }

            lcp[r] = h;

            if (h > 0) h--;
        }

        int ans = n;

        for (int i = 0; i < n; i++) {
            int maxLcp = lcp[i];

            if (i + 1 < n) {
                maxLcp = Math.max(maxLcp, lcp[i + 1]);
            }

            int len = maxLcp + 1;

            if (len <= n - sa[i]) {
                ans = Math.min(ans, len);
            }
        }

        return ans;
    }
}
