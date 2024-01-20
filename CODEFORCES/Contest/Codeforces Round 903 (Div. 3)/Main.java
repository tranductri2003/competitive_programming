import java.util.*;

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
            Map<Integer, Integer> f = new HashMap<>();
            for (int x : a) {
                while (x > 1) {
                    if (f.containsKey(lpf[x])) {
                        f.put(lpf[x], f.get(lpf[x]) + 1);
                    } else {
                        f.put(lpf[x], 1);
                    }
                    x /= lpf[x];
                }
            }
            boolean isPossible = true;
            for (Map.Entry<Integer, Integer> entry : f.entrySet()) {
                if (entry.getValue() % n != 0) {
                    isPossible = false;
                    break;
                }
            }
            if (isPossible) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }

    public static void init() {
        for (int i = 2; i < N; i++) {
            if (lpf[i] == i) {
                for (int j = i; j < N; j += i) {
                    lpf[j] = i;
                }
            }
        }
    }

    static int N = 1000001;
    static int[] lpf = new int[N];
}
