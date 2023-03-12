import java.util.HashMap;

class ListNode 
{
    int val;
    ListNode next;
    ListNode(int x) 
    {
        val = x;
        next = null;
    }
}

public class nhap
{
    public boolean hasCycle(ListNode head) 
    {
        HashMap<ListNode,Integer> check = new HashMap<ListNode,Integer>();
        
        while (head!=null)
        {
            if (check.getOrDefault(head, 0)==0)
            {
                check.put(head, 1);
                head=head.next;
            }
            else
            {
                return true;
            }
        }
        return false;
    }
}