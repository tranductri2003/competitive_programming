import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        while (t-- > 0) {
            int n = scanner.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = scanner.nextInt();
            }
            long[] dp = new long[n];
            for (int i = 0; i < n; i++) {
                dp[i] = -1;
            }

            long result = findMinimumSteps(a, dp, 0);
            System.out.println(result);
        }
    }

    public static long findMinimumSteps(int[] a, long[] dp, int p) {
        int n = a.length;
        if (p == n) {
            return 0;
        }
        if (dp[p] != -1) {
            return dp[p];
        }

        long r = Long.MAX_VALUE;
        r = Math.min(r, 1 + findMinimumSteps(a, dp, p + 1));
        if (p + a[p] < n) {
            r = Math.min(r, findMinimumSteps(a, dp, p + a[p] + 1));
        }
        dp[p] = r;
        return r;
    }
}
