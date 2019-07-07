import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/**
 * Simple implementation of a Bag
 * 
 * @author pugh
 */
public class Bag<E> {
    final Map<E, Integer> map;

    public Bag() {
        map = new HashMap<E, Integer>();
    }

    public Bag(Map<E, Integer> map) {
        this.map = map;
    }

    public boolean add(E e) {
        Integer v = map.get(e);
        if (v == null)
            map.put(e, 1);
        else
            map.put(e, v + 1);
        return true;
    }

    public boolean add(E e, int count) {
        Integer v = map.get(e);
        if (v == null)
            map.put(e, count);
        else
            map.put(e, v + count);
        return true;
    }

    public Set<E> keySet() {
        return map.keySet();
    }

    public Collection<Map.Entry<E, Integer>> entrySet() {
        return map.entrySet();
    }

    public int getCount(E e) {
        Integer v = map.get(e);
        if (v == null)
            return 0;
        else
            return v;
    }

}
